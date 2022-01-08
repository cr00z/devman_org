import requests
import datetime
import argparse
import getpass


STARS_COLUMN_WIDTH = 5
ISSUES_COLUMN_WIDTH = 6


class APIRateLimitException(Exception):
    pass


class APIBadCredentialsException(Exception):
    pass


def get_github_api_response(api_url, api_query, api_auth):
    api_response = requests.get(api_url, api_query, auth=api_auth)
    if api_response.text.find('API rate limit exceeded') != -1:
        raise APIRateLimitException
    if api_response.text.find('Bad credentials') != -1:
        raise APIBadCredentialsException
    return api_response.json()


def get_trending_repositories(from_date, top_size, api_auth):
    api_url = 'https://api.github.com/search/repositories'
    api_query = {
        'q': 'created:>{}'.format(from_date),
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_size
    }
    return get_github_api_response(api_url, api_query, api_auth)


def get_open_issues_amount(repo_owner, repo_name, api_auth):
    api_url = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )
    issue = get_github_api_response(api_url, None, api_auth)
    return len(issue)


def print_top_repos(repos_for_output):
    max_url_len = max([len(url) for url, stars, issues in repos_for_output])
    print('{} STARS ISSUES'.format('URL'.ljust(max_url_len)))
    for url, stars, issues in repos_for_output:
        print('{} {} {}'.format(
            url.ljust(max_url_len),
            str(stars).rjust(STARS_COLUMN_WIDTH),
            str(issues).rjust(ISSUES_COLUMN_WIDTH)
        ))


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description='Simple GitHub top repository searcher'
    )
    parser.add_argument('--user', help='GitHub username')
    parser.add_argument(
        '--top',
        type=int,
        default=20,
        help='Number of top repositories'
    )
    parser.add_argument(
        '--days',
        type=int,
        default=7,
        help='Number of top repositories'
    )
    return parser.parse_args()


def get_repos_for_output(week_ago, top_repos_num, api_auth):
    repos_for_output = []
    trending_repos = get_trending_repositories(week_ago, top_repos_num, api_auth)
    for repo in trending_repos['items']:
        open_issues = get_open_issues_amount(
            repo['owner']['login'],
            repo['name'],
            api_auth
        )
        repos_for_output.append((
            repo['html_url'],
            repo['stargazers_count'],
            open_issues
        ))
    return repos_for_output


if __name__ == '__main__':
    args = get_cmdline_args()
    api_auth = None
    if args.user:
        password = getpass.getpass('GitHub password:')
        api_auth = requests.auth.HTTPBasicAuth(args.user, password)
    print('Please wait')
    repos_for_output = []
    try:
        repos_for_output = get_repos_for_output(
            datetime.date.today() - datetime.timedelta(days=args.days),
            args.top,
            api_auth
        )
    except (APIRateLimitException, APIBadCredentialsException):
        print('API rate limit exceeded or API bad credentials')
    if repos_for_output:
        print_top_repos(repos_for_output)
