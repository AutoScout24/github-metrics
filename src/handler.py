#!/usr/bin/env python
from github.PaginatedList import PaginatedList
from github_api import GithubClient
import boto3

def handler(event, context):
    github_client = GithubClient("h776bssf9093hd5588sd827s4mv79cb35ivnskfy9", "Autoscout24")
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

    public_repos: PaginatedList = github_client.get_repos('public')
    print(public_repos)
    public_repos_count = 0
    for repo in public_repos:
        print(repo)
        public_repos_count = public_repos_count + 1
    cloudwatch.put_metric_data(
    MetricData = [
            {
                'MetricName': 'PublicRepos',
                'Unit': 'Count',
                'Value': public_repos_count
            },
        ],
        Namespace='Github'
    )

    private_repos: PaginatedList = github_client.get_repos('private')
    print(private_repos)
    private_repos_count = 0
    for repo in private_repos:
        print(repo)
        private_repos_count = private_repos_count + 1
    cloudwatch.put_metric_data(
    MetricData = [
            {
                'MetricName': 'PrivateRepos',
                'Unit': 'Count',
                'Value': private_repos_count
            },
        ],
        Namespace='Github'
    )

    forked_repos: PaginatedList = github_client.get_repos('fork')
    print(forked_repos)
    forked_repos_count = 0
    for repo in forked_repos:
        print(repo)
        forked_repos_count = forked_repos_count + 1
    cloudwatch.put_metric_data(
    MetricData = [
            {
                'MetricName': 'ForkedRepos',
                'Unit': 'Count',
                'Value': forked_repos_count
            },
        ],
        Namespace='Github'
    )

    internal_repos: PaginatedList = github_client.get_repos('internal')
    print(internal_repos)
    internal_repos_count = 0
    for repo in internal_repos:
        print(repo)
        internal_repos_count = internal_repos_count + 1
    cloudwatch.put_metric_data(
    MetricData = [
            {
                'MetricName': 'InternalRepos',
                'Unit': 'Count',
                'Value': internal_repos_count
            },
        ],
        Namespace='Github'
    )