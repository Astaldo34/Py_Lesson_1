import os

folders = {'my_project': ['settings', {'mainapp': ['templates', 'main']}, {'adminapp': ['templates', 'main']}, 'authapp']}

for main, dr in folders.items():
    os.makedirs(f'{main}', exist_ok=True)
    for folder in dr:
        if type(folder) is dict:
            for parent, child in folder.items():
                os.makedirs(f'{main}\\{parent}', exist_ok=True)
                for cld in child:
                    os.makedirs(f'{main}\\{parent}\\{cld}', exist_ok=True)
        else:
            os.makedirs(f'{main}\\{folder}', exist_ok=True)