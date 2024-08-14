import requests
from os import getenv

# Load your GitHub token from environment variable
token = getenv('GITHUB_TOKEN')

# Set up headers for authentication and API versioning
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json',
    'X-GitHub-Api-Version': '2022-11-28'
}

def fetch_users(url):
    users = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            users.extend(data)
            # Check if there's a next page in the headers
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                url = None
        else:
            print(f"Failed to fetch data from {url}: {response.status_code}, {response.text}")
            break
    return users

def compare_followers_following():
    followers_data = fetch_users('https://api.github.com/user/followers')
    following_data = fetch_users('https://api.github.com/user/following')

    followers = {user['login'] for user in followers_data}
    following = {user['login'] for user in following_data}

    not_following_back = following - followers

    print("Users you are following who do not follow you back:")
    for user in not_following_back:
        print(user)

if __name__ == '__main__':
    compare_followers_following()
