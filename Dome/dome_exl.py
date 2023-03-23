import logging

logging.basicConfig(format="%(asctime)s-%(name)s-%(levelname)s-",level="DEBUG")
l = logging.getLogger("hua")
logging.info("This is Error!")
logging.info("This is Fatal!")
