"""init.py

After creating this project from the containers_template repository, 
run this interactive script once to initialize your personal repository
"""

import os
import sys

if __name__ == '__main__':
    name = input('What is your GitHub organization or username hosting this project? ')
    print(f'your GitHub organization/username is: {name}')

    project = input('What is the name of this project? ')
    print(f'your GitHub organization/username is: {project}')
    print(f'I shall assume the project is hosted at https://github.com/{name}/{project}')

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


        print('The repository has been converted.',
              'Commit and push all changes by issuing ``git commit -a -m "initial setup"; git push``')