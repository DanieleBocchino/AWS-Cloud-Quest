

# list of README files to update
YAML_FILE = 'badges.yaml'
README_FILES = ['Analyzing Network Traffic/README.md',
                'API with Database/README.md', 
                'Automation with CloudFormation/README.md', 
                'Backing up Data/README.md'
                ]

MAIN_DIR = '/Volumes/BackUp/AWS/AWS-Cloud-Quest/'


import os
import yaml
from jinja2 import Environment, FileSystemLoader

# load the variables from a YAML file
with open(YAML_FILE) as f:
    variables = yaml.safe_load(f)

# load the README.md template from a file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('README.md')

# directory to search for .md files
directory = 'my_directory/'

# loop over all .md files in the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            # full path of the current .md file
            file_path = os.path.join(root, file)

            # render the template with the variables
            markdown = template.render(variables)

            # write the resulting markdown to the .md file
            with open(file_path, 'w') as f:
                f.write(markdown)
