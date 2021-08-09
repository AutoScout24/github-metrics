#!/usr/bin/env python
from github.PaginatedList import PaginatedList
from github_api import GithubClient
import boto3

def handler(event, context):
    github_client = GithubClient("98a768fi3u9844aal98345jx73nf6xo2nt9cy4bb5", "Autoscout24")
    cloudwatch = boto3.client('cloudwatch')

    teams: PaginatedList = github_client.get_teams()
    cloudwatch.put_metric_data(
    MetricData = [
            {
                'MetricName': 'Teams',
                'Unit': 'Count',
                'Value': teams.totalCount
            },
        ],
        Namespace='Github'
    )

    members: PaginatedList = github_client.get_members()
    cloudwatch.put_metric_data(
    MetricData = [
            {
                'MetricName': 'Members',
                'Unit': 'Count',
                'Value': members.totalCount
            },
        ],
        Namespace='Github'
    )
