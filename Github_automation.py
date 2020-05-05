from github import Github

# login panel
g=Github("username","password")

# to search repos of a spesific language all over github
repos=g.search_repositories(query="language:any language")
for repo in repos:
	print(repo)

# to get users all repositories
for repo in g.get_user().get_repos():
	print(repo.name)

# to get info of a specific repo
repo=g.get_repo("username/repo_name")

#to see no. of stars in a repo
repo.stargazers_count

# to see no. of traffic on a repo
traff=repo.get_views_traffic()
traff

# to see contents present in  a repo
content=repo.get_contents("")
for content_fil in content:
	print(content_fil)

user=g.get_user()

# to cerate a new repo on oyur profile
repo=user.create_repo('name of repository')

# to push content to the repo
repo.cerate_file("filename","commit msg","content if not present")

# to delete files form a repo
cont=repo.get_contents("filename")
repo.delete_file(cont.path,"msg",cont.sha,branch='your barnch/master')
