import requests

def extract_owner_repo(repo_url):
    """Extracts the owner and repository name from a GitHub URL."""
    repo_url = repo_url.rstrip('/')
    parts = repo_url.replace('https://github.com/', '').split('/')
    
    if len(parts) < 2:
        raise ValueError(f"Invalid repository URL: {repo_url}")
    
    return parts[0], parts[1]

def get_commits(owner, repo, page=1):
    """Fetches commit history from the repository."""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits?page={page}&per_page=100'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error fetching commits ({response.status_code}): {response.json()}')
        return []
