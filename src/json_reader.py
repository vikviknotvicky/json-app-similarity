import json
import os
import sys
from src.logger import logger


def read_json_app(input_json):
    """_summary_

    Args:
        input_json (_type_): _description_

    Raises:
        FileNotFoundError: _description_

    Returns:
        _type_: _description_
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

