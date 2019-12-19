import os
import requests
import json

# Access stored environmental variables for username and password
Git_User = os.environ['GIT_USER']
Git_Token = os.environ['GIT_TOKEN']

github_existing_teamid_list = []
git_team_id_mapping = {}
git_repo_list = []
git_exclude_list = ["RenaissanceService-GH","AuthoringPortalService-GH","AuthoringPortal-GH","LearnosityTools-GH","SLE-GH","QE-PrideRock-UI-GH","QE-PrideRock-Service-GH","Player-GH","lms-GH","Authentication-GH","ContentEngine-GH","NWEAService-GH","ECS_Terraform-GH","DataPlatform-GH","cookbook_edge_skeletons-GH","DataPlatformFrontend-GH","cookbook_edge_chef_client-GH","cookbook_edge_join_domain-GH","cookbook_edge_win_sql_clustering-GH","cookbook_edge_windows_os_hardening-GH","Chef_Cookbooks-GH","cookbook_edge_al_agent-GH","GitHub-Training","Kyle-Github-Training-","Git_Migration"]

git_repo_url = 'https://api.github.com/orgs/edgenuity/repos'
git_team_url = 'https://api.github.com/orgs/edgenuity/teams'
git_repo_delete_url = 'https://api.github.com/repos/edgenuity'
git_team_delete_url = 'https://api.github.com/teams'
git_headers = {'Content-Type':'application/json','Authorization':'token '+ Git_Token}


# Check if team exists on github, if not, create it
response = requests.get(url=git_team_url+'?per_page=100',headers=git_headers)
response_json = json.loads(response.text)
print len(response_json)
for team in response_json:
            if team['name'] not in git_team_id_mapping:
                git_team_id_mapping[team['name'].encode("utf-8")]=team['id']
                github_existing_teamid_list.append(team['id'])
        
print git_team_id_mapping
print github_existing_teamid_list

for i in range (1,8):
    print i
    response = requests.get(url=git_repo_url+'?page='+str(i)+'&per_page=100',headers=git_headers)
    response_json = json.loads(response.text)
    print len(response_json)
    for repo in response_json:
        git_repo_list.append(repo["name"].encode("utf-8"))
print git_repo_list
print len(git_repo_list)


for team_id in github_existing_teamid_list:
    response = requests.delete(url=git_team_delete_url+"/"+str(team_id),headers=git_headers)
    print response.status_code

for repo in git_repo_list:
    if repo in git_exclude_list:
        print "Got exclude repo: "+repo
    else:
        print "Repo to be deleted is: "+repo
        print "We will be deleting " +repo
        
        response = requests.delete(url=git_repo_delete_url+"/"+repo,headers=git_headers)
        print response.status_code
