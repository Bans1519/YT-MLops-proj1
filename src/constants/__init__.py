import os
from datetime import date

# for mongodb connection
DATABASE_NAME = "mlops_vehicle_insu"
COLLECTION_NAME = "vehicle_insu_data"
MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME : str = ""
ARTIFACT_DIR = "artifact" 

MODEL_FILE_NAME = "best_model.pkl"

TARGET_COLUMN = "Response"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"    
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"

"""Data Ingestion related constant start with DATA_INGESTION_VAR_NAME
"""
DATA_INGESTION_COLLECTION_NAME: str =  "vehicle_insu_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

"""Data Validation related constant start with DATA_VALIDATION_VAR_NAME
"""



