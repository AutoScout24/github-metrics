import { App } from "aws-cdk-lib";
import { ServiceStack } from "../lib/service";

const app = new App();

const serviceName = "github-metrics";

export const service = new ServiceStack(app, serviceName, {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: "eu-west-1",
  },
  description: "Metrics about github usage",
  stackName: serviceName,
});
