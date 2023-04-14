import logging

logging.basicConfig(filename="error.log",
                    format='%(asctime)s:%(name)s: %(levelname)s: %(message)s',
                    filemode='a',
                    level=logging.ERROR)

logger = logging.getLogger()
