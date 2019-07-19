from github import Github

g = Github("asariakevin","1997kevinasaria")


for repo in g.get_user().get_repos():
    print(repo.name)
