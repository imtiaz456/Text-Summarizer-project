# We copied this code from 01_data_ingestion.ipynb file the cell "4. Update the configuration manager in 
# src config"  as it is and paste here.

from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml
from textSummarizer.utils.common import create_directories
from textSummarizer.entity import (DataIngestionConfig)
from textSummarizer.entity import (DataValidationConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,  # i am taking it from textSummarizer.constants.
        params_filepath = PARAMS_FILE_PATH): # i am taking it from textSummarizer.constants too.

        self.config = read_yaml(config_filepath) # now i am passing this path in read_yaml.and it will read all the
        self.params = read_yaml(params_filepath) # data from the config.yaml file.and i can access all the variables

        create_directories([self.config.artifacts_root]) # by calling create_directories function we will 
     # pass artifacts_root from config.yaml file. It acts like configBox like output. as in eg. trials.ipynb


    

    def get_data_ingestion_config(self) -> DataIngestionConfig: # its a return type of above previous cell.
        config = self.config.data_ingestion    # these are variables below it will return.
    
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    