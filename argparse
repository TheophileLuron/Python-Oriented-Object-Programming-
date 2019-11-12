import argparse
from logging import init_logger


try:
        logger.info('Infos execution')
        parser = argparse.ArgumentParser(description='execution_one')

        parser.add_argument('--input-dir', required=True,
                            help='Files .txt')

        parser.add_argument('--output-dir', required=True,
                            help='Folder to store')

        parser.add_argument('--proxy', required=True,
                            help='Kind of proxy used. Possible values: "none" or "scraperapi"')

        args = parser.parse_args()

except Exception as e:
        logger.critical(f'Critical error during scraping: {str(e)}')
