"""Creates an example writer and sender using threads."""
from time import sleep
from bayeosgatewayclient import BayEOSWriter, BayEOSSender
import logging

PATH = '/tmp/bayeos-device/'
NAME = 'Python-Thread-WithLogging'
URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'

writer = BayEOSWriter(PATH,max_time=10,log_level=logging.DEBUG)
writer.save_msg('Writer was started.')

sender = BayEOSSender(PATH, NAME, URL,backup_path='/dev/shm/bayeos-device')
sender.start()

while True:
    writer.save([2.1, 3, 20.5])
    sleep(5)