import os

totalsize=0

for filename in os.listdir('c:\\'):
    if not os.path.isfile(os.path.join('C:\\Users\\anis.sayyad\\PycharmProjects\\Git_Migration-master', filename)):
        continue
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\Users\\anis.sayyad\\PycharmProjects\\Git_Migration-master', filename))

print(totalsize)

currenrdir= os.getcwd() #To get Current working directory.
print(currenrdir)

getsize= os.path.getsize("C:\\Users\\anis.sayyad\\PycharmProjects\\Git_Migration-master\\bitbucket_to_git_migration.py")
print(getsize)