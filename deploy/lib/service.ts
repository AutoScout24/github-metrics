import * as cdk from "@aws-cdk/core";
import { PolicyStatement } from "@aws-cdk/aws-iam";
import { Function, Runtime, Code } from "@aws-cdk/aws-lambda";
import { Rule, Schedule } from "@aws-cdk/aws-events";
import { LambdaFunction } from "@aws-cdk/aws-events-targets";

export type ServiceProps = {
  description: string;
};

export class ServiceStack extends cdk.Stack {
  constructor(app: cdk.App, id: string, props: cdk.StackProps & ServiceProps) {
    super(app, id, props);

    const lambda = new Function(this, "Lambda", {
      functionName: "github-metrics",
      description: props.description,
      runtime: Runtime.PYTHON_3_7,
      timeout: cdk.Duration.seconds(5),
      code: Code.fromAsset("../dist/github-metrics.zip"),
      handler: "handler.handler",
    });

    const statement = new PolicyStatement();
    statement.addActions("cloudwatch:PutMetricData");
    statement.addResources("*");

    lambda.addToRolePolicy(statement);

    const cronExpression = "cron(00 00 * * ? *)";
    const cloudWatchRule = new Rule(this, `Rule`, {
      ruleName: `github-metric-rule`,
      description: "Run every day at 00:00AM UTC",
      schedule: Schedule.expression(cronExpression),
    });

    cloudWatchRule.addTarget(new LambdaFunction(lambda));
  }
}
