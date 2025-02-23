from scanner.commit_fetcher import extract_owner_repo, get_commits
from scanner.file_scanner import get_files_from_commit, search_for_tokens_in_files
from utils.helpers import print_banner

def run(repo_url):
    """Main function to execute the scanner."""
    try:
        owner, repo = extract_owner_repo(repo_url)
        print_banner()
        commits = get_commits(owner, repo)

        for commit in commits:
            sha = commit['sha']
            print(f"Processing commit: {sha}")
            files = get_files_from_commit(owner, repo, sha)
            search_for_tokens_in_files(files)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    repo_url = input("Enter GitHub repository URL: ")
    run(repo_url)
