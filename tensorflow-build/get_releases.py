from github import Github
import datetime
import sys

#Get first parameter from command line
git_token = sys.argv[1]


G = Github(git_token)  # Put your GitHub token here
repo = G.get_repo('MDK-Packs/tensorflow-pack')
releases = repo.get_releases()

releases = releases    

for release in releases:
    if 'nightly' in release.title:
        continue
    print("<release version=\""+release.title+"\" url=\"https://github.com/MDK-Packs/tensorflow-pack/releases/download/"+release.tag_name+"/tensorflow.tensorflow-lite-micro."+release.tag_name+".pack\" date=\""+release.created_at.strftime('%Y-%m-%d')+"\">" + release.body + "</release>")


    

