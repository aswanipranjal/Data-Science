import argparse

from perceval.backends.core.github import GitHub

parser = argparse.ArgumentParser(description='Simple parser for GitHub issues and pull requests')
parser.add_argument('-t', '--token', help='GitHub token')
parser.add_argument('-r', '--repo', help='GitHub repository, as \'owner/repo\'')
args = parser.parse_args()