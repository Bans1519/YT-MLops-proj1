from src.logger import logging
from src.exception import MyException
import sys
import os   
from src.pipline.training_pipeline import TrainPipeline
from src.logger import logging as custom_logger

pipline = TrainPipeline()
pipline.run_pipeline()

