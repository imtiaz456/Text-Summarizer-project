# update the components

import os
import urllib.request as request # Using it to download my data from url
import zipfile                   # to perform unzip operation
from textSummarizer.logging import logger  # import from common.py file
from textSummarizer.utils.common import get_size  # import from common.py file
from pathlib import Path
from textSummarizer.entity import (DataIngestionConfig)

# i just copied code from 01_data_ingestion.ipynb file and pasted here

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config   # here i am initializing the config

# two methods 1. download data from url and 2. unzip the file
    
    def download_file(self):         
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,  # its the url we defined in config.yml
                filename = self.config.local_data_file  # it shows where i am downloading this file(local_data_file).
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  
          # i also want to see the size of the file. therefore using get_size method.
        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir # unzip into unzip_dir.
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  # i am extracting in unzip file