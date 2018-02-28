import argparse
from perceval.backends.core.git import Git

parser = argparse.ArgumentParser(description='Count commits in a git repository')
parser.add_argument('repo', help='Repository url')
parser.add_argument('dir', help='Directory for cloning the repository')
parser.add_argument('--print', action='store_true', help='Print hashes')
