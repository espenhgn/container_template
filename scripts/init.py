"""init.py

After creating this project from the containers_template repository, 
run this interactive script once to initialize your personal repository
"""

import os
import sys
from copy import copy

if __name__ == '__main__':
    name = input('What is your GitHub organization or username hosting this project? ')
    print(f'your GitHub organization/username is: {name}')

    project = input('What is the name of this project? ')
    print(f'your GitHub organization/username is: {project}')
    print(f'I shall assume the project is hosted at https://github.com/{name}/{project}')

    oldname = 'espenhgn'

    oldproject = 'container_template'

    while True:
        response = input('Is this correct (yes/no)? ')
        if response in ['Y', 'y', 'yes', 'Yes', 'N', 'n', 'no', 'No']:
            break
        else:
            print(f'{response} is not a valid response. Try again.\n')
    
    if response in ['N', 'n', 'no', 'No']:
        print('Exiting. No file changes were applied.\n')
    else:
        print('Converting repository....\n')

        # walk files and replace occurrences of `oldproject` by `project`` ID,
        # and `oldname` by `name` (github org/user) as supplied by the user.

        forbiddendirs = ['.git', '.pytest_cache']
        exclude = set(['__pycache__'])
        forbiddenfiles = []
        for root, dirs, files in os.walk('.', topdown=True):
            dirs[:] = [d for d in dirs if d not in exclude]
            # iterate over files
            for filename in files:
                if root != '.':
                    if root.split(os.path.sep)[1] in forbiddendirs:
                        print(f'skipping {os.path.join(root, filename)}')
                        continue
                
                
                # modify file contents:
                with open(os.path.join(root, filename), 'r', encoding="utf8") as f :
                    filedata = f.read()

                newfiledata = copy(filedata)
                newfiledata = filedata.replace(oldname, name)
                newfiledata = newfiledata.replace(oldproject, project)

                if newfiledata != filedata:
                    print(f'rewriting {os.path.join(root, filename)}')
                    with open(os.path.join(root, filename), 'w', encoding="utf8") as f:
                        f.write(filedata)

                # modify file names:
                if filename.rfind(oldproject) > 0:
                    newfilename = filename.replace(oldproject, project)
                    print(f'renaming {os.path.join(root, filename)} {os.path.join(root, newfilename)}')
                    os.rename(filename, newfilename)
                            
            # iterate over directories
            for directory in dirs:
                if root.split(os.path.sep)[1] in forbiddendirs:
                    print(f'skipping {directory}')
                    continue
                
                if directory.rfind(oldproject) > 0:
                    newdir = directory.replace(oldproject, project)
                    print(f'renaming {directory} {newdir}')
                    os.rename(directory, newdir)
            
            
        # copy ./scripts/PROJECT_README.md over ./README.md
        os.remove('README.md')
        os.rename(os.path.join('scripts', 'PROJECT_README.md'), 'README.md')

        print('The repository has been converted.\n', 
        'Commit and push all changes to the remote by issuing \n', 
        '``git commit -a -m "initial setup"; git push``')