import json
import os
import sys
from src.logger import logger


def read_json_app(input_json):
    """Load an application JSON file. 

    Args:
        input_json (pathname): Text or binary file containing JSON document

    Raises:
        FileNotFoundError: Input file is missing
        JSONDecodeError: Input file is not a valid JSON

    Returns:
        dict: Application(s) schema
    """
    logger.info(f"Reading the {input_json}...")

    try:
        if not os.path.isfile(input_json):
            raise FileNotFoundError
        
        with open(input_json, 'r') as input_json_file:
            input_app_json = json.load(input_json_file)

        logger.info(f"{input_json} is loaded")
        return input_app_json
    
    except FileNotFoundError as e:
        logger.error(f'File {input_json} not found!')
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f'File {input_json} is not a valid JSON!')
        sys.exit(1)


