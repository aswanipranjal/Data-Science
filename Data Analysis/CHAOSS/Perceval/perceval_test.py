from perceval.backends.core.git import Git

repo_url = 'https://github.com/aimacode/aima-python.git'
repo_dir = '/tmp/aima-python.git'

repo = Git(uri=repo_url, gitpath=repo_dir)

# fetch all commits as an iterator, and iterate it printing each hash
commits = 0
for commit in repo.fetch():
	print(commit['data']['commit'])
	commits += 1
print(commits)