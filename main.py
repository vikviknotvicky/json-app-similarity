from src.argparser import parser
from src.logger import logger
from src.similarity_search import find_best_match


if __name__ == '__main__':
    args = parser.parse_args()

    logger.info(f"Find the best matching app for {args.input}")

    find_best_match(
      input_json=args.input,
      apps_json_path=args.apps_json
    )

    logger.info(f"Process completed!")
