from textSummarizer.logging import logger # textSummarizer is locale package in setup.py file 
                                          # as SRC_REPO ="textSummarizer",
                                          # Inside textSummarizer there is  logging
                                          # Then import logger(logger is in (__init__.py) we made).

#logger.info("Welcome to our customm log") # to run this file virtual environment must be activated. 

from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline # imported from
                                                      # stage_01_data_ingestion import DataIngestionTraining
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()  # it will call the main method from stage_01_data_ingestion.py file
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main() # it will call the main method from stage_02_data_validation.py file
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e