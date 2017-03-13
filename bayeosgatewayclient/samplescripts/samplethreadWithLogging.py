"""Creates an example writer and sender using threads."""
from time import sleep
from bayeosgatewayclient import BayEOSWriter, BayEOSSender
import logging
import tempfile
from os import path

PATH = path.join(tempfile.gettempdir(),'bayeos-device')
BACKUP_PATH =  path.join(tempfile.gettempdir(),'bayeos-device-backup')
NAME = 'Python-Thread-WithLogging'

URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'

writer = BayEOSWriter(PATH,max_time=10,log_level=logging.DEBUG)
writer.save_msg('Writer was started.')

sender = BayEOSSender(PATH, NAME, URL,backup_path=BACKUP_PATH,log_level=logging.DEBUG)
sender.start()

nr=0
while True:
    writer.save([nr, 3, 20.5])
    #writer.flush()
    nr+=1
    sleep(5)