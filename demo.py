from us_visa.logger import logging
#logging.info('Welcome developers to mlops project')

import sys
from us_visa.exception import USvisaException

try:
    a = 1 / "10"

except Exception as e:
    logging.info(e)
    raise USvisaException(e,sys) from e