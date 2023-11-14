# 6. update the pipeline

from textSummarizer.config.configuration import ConfigurationManager # imported from config folder in src
from textSummarizer.components.data_ingestion import DataIngestion # importes from components folder
from textSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()