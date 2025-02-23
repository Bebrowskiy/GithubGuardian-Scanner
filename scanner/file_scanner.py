import requests
import re
from scanner.regex_patterns import TOKEN_PATTERNS

def get_files_from_commit(owner, repo, sha):
    """Fetches file changes from a commit."""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits/{sha}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('files', [])
    else:
        print(f'Error fetching files from commit {sha} ({response.status_code}): {response.json()}')
        return []

def search_for_tokens_in_files(files):
    """Searches for sensitive tokens in modified or added files."""
    for file in files:
        if file['status'] in ['modified', 'added']:
            file_url = file['raw_url']
            try:
                file_content = requests.get(file_url).text
                for pattern in TOKEN_PATTERNS:
                    matches = re.findall(pattern, file_content)
                    if matches:
                        print(f"Found {len(matches)} matches in file {file['filename']}:")
                        for match in matches:
                            print(f"  - {match}")
            except Exception as e:
                print(f"Error loading {file_url}: {e}")
