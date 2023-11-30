import requests

# Replace 'YOUR_GITHUB_TOKEN' with your actual GitHub token
GITHUB_TOKEN = ""
ORGANIZATION_NAME = 'NexaAI'

# The GitHub API URL for organization repositories
GITHUB_API_URL = f"https://api.github.com/orgs/{ORGANIZATION_NAME}/repos"

# Create a session to manage and persist settings across requests (headers, auth, etc.)
session = requests.Session()
session.headers.update({'Authorization': f'token {GITHUB_TOKEN}'})

def get_repositories(org, session):
    """Retrieve a list of repositories and their descriptions for a given organization."""
    repos = []
    page = 1
    while True:
        response = session.get(f"{GITHUB_API_URL}?per_page=100&page={page}")
        response.raise_for_status()  # Will halt if the request fails
        page_repos = response.json()
        if page_repos:
            repos.extend({
                'name': repo['name'],
                'description': repo['description']
            } for repo in page_repos)
            page += 1
        else:
            break
    return repos

try:
    repo_list = get_repositories(ORGANIZATION_NAME, session)
    print(f"Repositories in {ORGANIZATION_NAME}:")
    for repo in repo_list:
        print(f"｜ {repo['name']} ｜ {repo['description']} ｜")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")