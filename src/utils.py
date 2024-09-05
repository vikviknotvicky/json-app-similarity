import numpy as np
import pandas as pd
from numpy.linalg import norm


def preprocess_app_json(model, app_json) -> list:
    """_summary_

    Args:
        model (_type_): _description_
        app_json (_type_): _description_

    Returns:
        list: _description_
    """
    encoded_app_matrix = []
    for app in app_json.keys():
        app_encoded = pd.json_normalize(
            data=app_json[app]['ai_dict']['tables'],
            meta=['name'],
            record_path='fields',
            meta_prefix='table_',
            errors='warn'
        )[['table_name', 'name', 'type']].values

        encoded_app_matrix.append(np.array(model.encode(app_encoded)))

    return encoded_app_matrix


def cosine_similarity(input_a: np.ndarray, input_b: np.ndarray) -> float:
    """Calculates the cosine similarity between two vectors

    Args:
        input_a (np.ndarray): First vector
        input_b (np.ndarray): Second vector

    Returns:
        float: Cosine similarity score
    """
    return np.dot(input_a, input_b) / (norm(input_a) * norm(input_b))
