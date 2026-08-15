import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO)

Project_name = "ML_Project"

list_of_files = [
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/components/data_ingestion.py",
    f"src/{Project_name}/components/data_transformation.py",
    f"src/{Project_name}/components/model_training.py",
    f"src/{Project_name}/components/model_monitering.py",
    f"src/{Project_name}/pipelines/__init__.py",
    f"src/{Project_name}/pipelines/training_pipeline.py",
    f"src/{Project_name}/pipelines/prediction_pipeline.py",
    f"src/{Project_name}/exception.py",
    f"src/{Project_name}/logger.py",
    f"src/{Project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating Empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")