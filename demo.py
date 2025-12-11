from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

# logging.info("Demo file is run")

try:
    logging.info("Starting the demo.py script")
    a = 1 / 0
except Exception as e:
    raise USvisaException(e, sys)