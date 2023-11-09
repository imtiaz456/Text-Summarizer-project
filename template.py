import os
from pathlib import Path
import logging  # to log all ther information

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

# All we need here is to write the corresponding files and folders.it will create automatically
#  not to create manualy.

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",  # for every local package this(__init__.py) constrctor is needed
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", # here we will write all the utilities
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",  # inside .yaml we will mention all the commands for   CI/CD deployment
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb" # it will contain all the notebook experiments.. now we create trail notebook
    ]

# logic to create all these files and folders

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)   # it will split folders and file respectively

    if filedir != "": # if filesize is not empty then we will not change the file
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}") # FOLDER creation is done

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):# if file is not found or 0 size
        with open(filepath, 'w') as f:                                   # then we will create new one.
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")