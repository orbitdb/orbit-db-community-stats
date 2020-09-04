import os
from github import Github

g = Github(os.environ['GITHUB_TOKEN'])

stargazers = set()
contributors = set()
subscribers = set()

for repo in g.get_organization('orbitdb').get_repos():
    for gazer in repo.get_stargazers():
        stargazers.add(gazer)

    for contributor in repo.get_contributors():
        contributors.add(contributor)

    for subscriber in repo.get_subscribers():
        subscribers.add(subscriber)

print("Stargazers: ", len(stargazers))
print("Contributors: ", len(contributors))
print("Subscribers: ", len(subscribers))

# Manually calculated 2020-09-03
print("Used in: ", 1835)
