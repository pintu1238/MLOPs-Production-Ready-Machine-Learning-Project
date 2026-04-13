from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys
# logging.info("This is a info message")

try:
   a=2/0
except Exception as e:
    logging.info("This is an error message")
    raise USvisaException(e, sys)