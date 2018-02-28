import argparse

from perceval.backends.core.github import GitHub

parser = argparse.ArgumentParser(description='Simple parser for GitHub issues and pull requests')
parser.add_argument('-t', '--token', help='GitHub token')
parser.add_argument('-r', '--repo', help='GitHub repository, as \'owner/repo\'')
args = parser.parse_args()

(owner, repo) = args.repo.split('/')
repo = GitHub(owner=owner, repository=repo, api_token=args.token)

for item in repo.fetch():
	if 'pull_request' in item['data']:
		kind = 'Pull Request'
	else:
		kind = 'Issue'
	print(f'{item['data']['number']} : {kind}')