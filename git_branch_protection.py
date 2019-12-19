import os
import requests
import json

# Access stored environmental variables for username and password
Git_User = os.environ['GIT_USER']
Git_Token = os.environ['GIT_TOKEN']

lead_team_id = 0
team_id = 0
maintainer_users = []
protected_branch_names = ["master","staging","perf"]
git_team_id_mapping = {}
git_repo_list = []
git_repo_team_mapping = {}
git_team_maintainerrole_mapping = {}

git_repo_url = 'https://api.github.com/orgs/edgenuity/repos'
git_team_url = 'https://api.github.com/orgs/edgenuity/teams'
git_repo_team_mapping_url = 'https://api.github.com/repos/edgenuity'
git_team_member_url = 'https://api.github.com/teams'
git_add_repo_to_team_url = 'https://api.github.com/teams'
git_headers = {'Content-Type':'application/json','Authorization':'token '+ Git_Token}
git_update_branch_protection_headers = {'Content-Type':'application/json','Authorization':'token '+ Git_Token,'Accept':'application/vnd.github.luke-cage-preview+json'}

response = requests.get(url=git_team_url+'?per_page=100',headers=git_headers)
response_json = json.loads(response.text)
for team in response_json:
            if team['name'] not in git_team_id_mapping:
                git_team_id_mapping[team['name'].encode("utf-8")]=team['id']
            if team['name'] == "Leads":
                lead_team_id = team['id']            
print git_team_id_mapping

for i in range (1,8):
    response = requests.get(url=git_repo_url+'?page='+str(i)+'&per_page=100',headers=git_headers)
    response_json = json.loads(response.text)
    for repo in response_json:
        git_repo_list.append(repo["name"].encode("utf-8"))
print git_repo_list

for repo in git_repo_list:
  
    print repo
    print lead_team_id
    '''
    response = requests.put(url=git_add_repo_to_team_url+"/"+str(lead_team_id)+"/repos/edgenuity/"+repo,headers=git_update_branch_protection_headers)
    print response.text
    if int(response.status_code) == 204:
        print "Repo successfully added to team"
    else:
        raise ("Repo could not be added to the team")
    '''
    response = requests.get(url=git_repo_team_mapping_url+'/'+repo+'/teams?per_page=100',headers=git_headers)
    response_json = json.loads(response.text)
    #print response_json
    if int(len(response_json)) != 0:
        for team in response_json:
            print team['name']
            if team['name'] in git_team_id_mapping:
                team_id = git_team_id_mapping[team['name']]
                print team_id            
                response = requests.get(url=git_team_member_url+'/'+str(team_id)+'/members?role=maintainer&per_page=100',headers=git_headers)
                print response.status_code
                response_json = json.loads(response.text)
                print response_json
                if int(len(response_json)) != 0:
                    for user in response_json:
                        print user['login']
                        maintainer_users.append(user['login'].encode("utf-8"))
                    
                    for branch in protected_branch_names:
                        try:
                            branch_protection_data = {'required_status_checks':{'strict':True,'contexts':['continuous-integration/teamcity']},'enforce_admins':False,'required_pull_request_reviews': {'dismissal_restrictions':{},'dismiss_stale_reviews':True,'require_code_owner_reviews':False,'required_approving_review_count': 2},'restrictions': {'users': maintainer_users,'teams':['leads']}}
                            response = requests.put(url=git_repo_team_mapping_url+'/'+repo+'/branches/'+branch+'/protection?per_page=100',headers=git_update_branch_protection_headers,data=json.dumps(branch_protection_data))
                            print response.status_code
                            print response.text
                            response_json = json.loads(response.text)
                            if int(response.status_code)!= 200:
                                if response_json['message'] == "Branch not found":
                                    raise ValueError ("Branch "+branch+" not found")
                                 
                            else:
                                print ("Branch protection updated for branch: "+branch)            
                        except ValueError as e:
                            print str(e)
                            continue
