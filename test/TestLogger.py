__author__ = 'Tails'
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='D:\Git\PythonAutomation\Log\Log20150704151553.log',
                filemode='w')

# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')

logger = logging.getLogger()
logger.info('This is info message')