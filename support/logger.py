import logging

# Determine which log messages are actually written to the log file
# logging.DEBUG will capture and log message at all levels, including DEBUG, INFO, WARNING, ERROR, and CRITICAL.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# FileHandler is an object that define how log messages should be written to a file.
# Create a file handler that will write log message to a file named 'test_automation.log'
handler = logging.FileHandler('./test_automation.log')
handler.setLevel(logging.DEBUG)

# Define the format for long messages, including timestamp, logger name, log level, and the actual message
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
