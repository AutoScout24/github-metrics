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

    # https://pygithub.readthedocs.io/en/latest/github_objects/Organization.html#github.Organization.Organization.get_repos
    # OPTIONAL param type: all, public, private, forks, sources, member, internal 
    def get_repos(self, type='all'): # type is 'all' by default
        return self.organization.get_repos(type)