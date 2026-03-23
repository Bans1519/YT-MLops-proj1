import sys
from src.exception import MyException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("Starting Data Ingestion...")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Data Ingestion completed successfully.")
            return data_ingestion_artifact
        except Exception as e:
            raise MyException(e, sys) from e

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            # Next steps (Validation, Transformation, etc.) go here
            
        except Exception as e:
            # Log the full custom exception message
            logging.error(str(e))
            # RE-RAISE so the system (Docker/GitHub Actions) sees the failure
            raise MyException(e, sys) from e