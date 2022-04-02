import os
import shutil

os.makedirs('my_project\\templates', exist_ok=True)

for dr in os.listdir('my_project'):
    for cld in os.listdir(os.path.join('my_project', dr)):
        if cld == 'templates':
            print(f'{dr}\\{cld}')
            shutil.copytree(f'my_project\\{dr}\\{cld}', 'my_project\\templates', dirs_exist_ok=True)
