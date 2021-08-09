# Github Metrics

> A simple solution to track Github usage by an organisation.

## Stack

The deployment stack is build with [AWS CDK](https://github.com/aws/aws-cdk). It consists of
- A simple lambda to call Github API and send Github metrics to CloudWatch
- A CloudWatch event to call lambda everyday

## Lambda

Lambda is written in Python3.7 and uses [PyGithub](https://github.com/PyGithub/PyGithub) library to easily call Github API. The metrics are extracted from the data and sent to CloudWatch everyday.