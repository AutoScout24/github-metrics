#!/usr/bin/env python
from github import Github

class GithubClient:
    def __init__(self, token, organization):
        self.github = Github(token)
        self.organization = self.github.get_organization(organization)

    def get_teams(self):
        return self.organization.get_teams()

    def get_members(self):
        return self.organization.get_members()
