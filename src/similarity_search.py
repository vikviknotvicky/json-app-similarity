import numpy as np
import pandas as pd

from sentence_transformers import SentenceTransformer

from src.config import config
from src.logger import logger
from src.json_reader import read_json_app
from src.utils import preprocess_app_json, cosine_similarity


def find_best_match(input_json, apps_json_path=None) -> str:
    """_summary_

    Args:
        input_json (_type_): _description_
        apps_json_path (_type_, optional): _description_. Defaults to None.

    Returns:
        str: Index of the best-match application
    """
    new_json_app = read_json_app(input_json)

    if apps_json_path:
        current_apps_json_path = apps_json_path
    else:
        current_apps_json_path = config['input']['original_apps_json']

    current_apps_json = read_json_app(current_apps_json_path)

    apps_search_values = pd.DataFrame.from_dict(current_apps_json).T.reset_index()

    model = SentenceTransformer("all-mpnet-base-v2")
    new_app_embeddings = preprocess_app_json(model, new_json_app)[0]
    current_apps_embeddings = preprocess_app_json(model, current_apps_json)

    similarity_scores = []
    for app in current_apps_embeddings:
        
        field_similarity_scores = []
        for new_field in new_app_embeddings:
            temp_scores = []
            for app_field in app:
                temp_similarity_score = cosine_similarity(new_field, app_field)
                temp_scores.append(temp_similarity_score)

            field_similarity_scores.append(np.max(temp_scores))
        
    similarity_scores.append(np.mean(field_similarity_scores))

    best_match_idx = np.argmax(similarity_scores)
    best_match_app_index = apps_search_values.iloc[best_match_idx]['index']

    info_msg = ("Best matching app with average similarity score = "
            f"{np.max(similarity_scores):.4f} --> "
            f"{best_match_app_index} "
            f"({apps_search_values.iloc[best_match_idx]['ai_dict']['name']})")
    logger.info(info_msg)

    return best_match_app_index
