import os

project_name = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

os.makedirs(project_name, exist_ok=True)

for folder in folders:
    os.makedirs(f'{project_name}\\{folder}', exist_ok=True)