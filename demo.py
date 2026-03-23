from src.logger import logging
from src.exception import MyException
import sys
import os   

# try:
#     a = 1 + 'z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline
from src.logger import logging as custom_logger

pipline = TrainPipeline()
pipline.run_pipeline()

if __name__ == "__main__":
    try:
        logging.info("Starting the application...") # This forces the file/folder creation
        print("Log message sent. Checking for folder...")
        
        # This will tell you exactly where Python is looking
        print(f"Current Working Directory: {os.getcwd()}")
        
    except Exception as e:
        print(f"An error occurred: {e}")