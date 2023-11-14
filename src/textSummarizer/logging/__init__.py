# This is a custom log we will make. then we will execute it through main.py file.

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"
log_dir = "logs" # here I created one directory called logs directory
log_filepath = os.path.join(log_dir, "running_logs.log") # Inside directiry I create one file called running_logs.log
os.makedirs(log_dir, exist_ok=True) # it will create a directory.


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers = [
        logging.FileHandler(log_filepath), # it will create a log file
        logging.StreamHandler(sys.stdout) # it will also show in the terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")  # we can give any name here.


# This is a custom log we made. Now we want to execute it , lets go to main.py file.