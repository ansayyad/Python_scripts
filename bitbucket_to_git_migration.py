import os
import requests
import json
import subprocess
import shutil

# Access stored environmental variables for username and password
Bitbucket_User = os.environ['BITBUCKET_USER']
Bitbucket_Pass = os.environ['BITBUCKET_PASS']
Git_User = os.environ['GIT_USER']
Git_Token = os.environ['GIT_TOKEN']

team_id = 0
empty_git_repo_list = []
github_existing_team_list = []
bitbucket_git_repo_list = []
repo_project_mapping = {}
bitbucket_project_list = []
bitbucket_nongit_repo_list = []
git_repo_team_mapping = {}

# Create a list of existing bitbucket repo names

bitbucket_url = 'https://api.bitbucket.org/2.0/repositories/edgenuity?pagelen=100'
headers = {'Content-Type':'application/json'}
response = requests.get(url=bitbucket_url,headers=headers,auth=(Bitbucket_User,Bitbucket_Pass))
response_json = json.loads(response.text)
for repo in response_json['values']:
    if 'project' in repo:
        repo_project_mapping[repo['slug'].encode("utf-8")] = repo['project']['name'].encode("utf-8")
    if repo['project']['name'] not in bitbucket_project_list:
        bitbucket_project_list.append(repo['project']['name'])
    if repo['scm']!= "git":
        bitbucket_nongit_repo_list.append(repo['slug'].encode("utf-8"))
    else:
        bitbucket_git_repo_list.append(repo['slug'].encode("utf-8"))

while True:
    if "next" in response_json:
        print "More repos exist"
        bitbucket_url = response_json["next"]
        headers = {'Content-Type':'application/json'}
        response = requests.get(url=bitbucket_url,headers=headers,auth=(Bitbucket_User,Bitbucket_Pass))
        response_json = json.loads(response.text)
        for repo in response_json['values']:
            if 'project' in repo:
                repo_project_mapping[repo['slug'].encode("utf-8")] = repo['project']['name'].encode("utf-8")
            if repo['project']['name'] not in bitbucket_project_list:
                bitbucket_project_list.append(repo['project']['name'])
            if repo['scm']!= "git":
                bitbucket_nongit_repo_list.append(repo['slug'].encode("utf-8"))
            else:
                bitbucket_git_repo_list.append(repo['slug'].encode("utf-8"))
    else:
        print "All repos covered"
        break

print bitbucket_project_list
#print repo_project_mapping
#print bitbucket_git_repo_list
print bitbucket_nongit_repo_list
print len(bitbucket_project_list)
print len(bitbucket_nongit_repo_list)
print len(bitbucket_git_repo_list)

git_repo_url = 'https://api.github.com/orgs/edgenuity/repos'
git_team_url = 'https://api.github.com/orgs/edgenuity/teams'
git_add_repo_to_team_url = 'https://api.github.com/teams'
git_headers = {'Content-Type':'application/json','Authorization':'token '+ Git_Token}
git_team_repo_mapping_headers = {'Content-Type':'application/json','Authorization':'token '+ Git_Token,'Accept':'application/vnd.github.hellcat-preview+json'}

for repo_name in bitbucket_git_repo_list:
    create = True     
    if repo_name in repo_project_mapping:
        print repo_name
        team_name = repo_project_mapping[repo_name]
        print team_name
        # Check if team exists on github, if not, create it
        response = requests.get(url=git_team_url+'?per_page=100',headers=git_headers)
        response_json = json.loads(response.text)
        print len(response_json)
        for team in response_json:
            if team['name'] not in github_existing_team_list:
                github_existing_team_list.append(team['name'].encode("utf-8"))
            if team_name == team['name']:
                team_id = team['id']
                print team_id
                create = False
                break
        #print github_existing_team_list
        #print len(github_existing_team_list)
        if create == True:
            print "Team not present, creating it"
            try:
                team_create_data = {'name': team_name,'description': 'This is '+team_name+' team','privacy': 'secret'}
                # Create team on github having same name as that of bitbucket project
                response = requests.post(url=git_team_url,headers=git_headers,data=json.dumps(team_create_data))
                print response.text
                response_json = json.loads(response.text)
                if 'errors' in response_json:
                    if response_json['errors'][0]['message'] == "Name has already been taken":
                        raise ValueError("Duplicate team name")
                else:
                    # Store team id for future purposes
                    global team_id
                    team_id = response_json['id']
                    print team_id
   
            except ValueError as e:
                print str(e)
                continue
        try:      
            repo_create_data = {'name': repo_name,'description': 'This is '+repo_name+' repository','homepage': 'https://github.com/edgenuity/'+repo_name,'private': True,'has_issues': True,'has_projects': True,'has_wiki': True}
    	    # Create an empty Git repo having same name as the bitbucket repo
    	    response = requests.post(url=git_repo_url,headers=git_headers,data=json.dumps(repo_create_data))
    	    print response.text
            # If repo is already present on Github, there is every chance that code will also be present so skpping next steps to speed up execution
            if int(response.status_code)!= 422:
    	        # Clone existing bitbucket repo
    	        clone_cmd = "git clone --mirror https://"+Bitbucket_User+":"+Bitbucket_Pass+"@bitbucket.org/edgenuity/"+repo_name+".git"
    	        subprocess.call(clone_cmd,shell=True)
    	        working_dir = os.getcwd()
    	        os.chdir(repo_name+".git")
    	        # Rename existing Git remote connection to bitbucket
    	        rename_origin_cmd = "git remote rename origin bitbucket"
    	        subprocess.call(rename_origin_cmd,shell=True)
   	        # Add remote origin as Git's newly created repo
    	        add_git_origin_cmd = "git remote add origin https://"+Git_User+":"+Git_Token+"@github.com/edgenuity/"+repo_name+".git"
    	        subprocess.call(add_git_origin_cmd,shell=True)
    	        # Set remote git url
    	        set_git_url_cmd = "git remote set-url --push origin https://"+Git_User+":"+Git_Token+"@github.com/edgenuity/"+repo_name+".git"
    	        subprocess.call(set_git_url_cmd,shell=True)
    	        # Push all branches in the repo
    	        git_push_branches_cmd = "git push --mirror"
    	        subprocess.call(git_push_branches_cmd,shell=True)
    	        # Remove remote bitbucket origin
    	        remove_bitbucket_origin_cmd = "git remote rm bitbucket"
    	        subprocess.call(remove_bitbucket_origin_cmd,shell=True) 
    	        os.chdir(working_dir)
    	        # Remove cloned bitbucket repo after pushing code to free up space
    	        shutil.rmtree(repo_name+".git")
            # Add github repository to team
            response = requests.put(url=git_add_repo_to_team_url+"/"+str(team_id)+"/repos/edgenuity/"+repo_name,headers=git_team_repo_mapping_headers)
            print response.text
            if int(response.status_code) == 204:
                print "Repo successfully added to team"
            else:
                raise ("Repo could not be added to the team")
        except Exception as e:
            print str(e)

print "Teams on Github are: " +str(github_existing_team_list)
print "Number of teams on Github are: " +str(len(github_existing_team_list))

# Get a list of almost empty Git repos which are almost empty due to either code not getting pushed into it or source repo did not have any code
# Iterating for 7 times as repo number is between 600 to 700
for i in range (1,8):
    print i
    response = requests.get(url=git_repo_url+'?page='+str(i)+'&per_page=100',headers=git_headers)
    print response.text
    response_json = json.loads(response.text)
    print len(response_json)
    for repo in response_json:
        if int(repo['size']) == 0:
            empty_git_repo_list.append(repo['name'].encode("utf-8"))

print "Almost empty Github repo names are:" +str(empty_git_repo_list)
print "Number of almost empty Github repo names are:" +str(len(empty_git_repo_list))

