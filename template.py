import os
from pathlib import Path


list_of_files = [

    f"__init__.py",
    f"experiments/__init__.py",
    f"experiments/mynotebook.ipynb",  
    f"src/__init__.py",
    f"src/data_preprocessing.py",
    f"src/data_ingestion.py",
    f"src/model_building.py",
    f"src/model_evaluation.py",
    f"src/feature_engineearing.py",
    "dvc.yaml",
    "params.yaml",
    "projectflow.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass