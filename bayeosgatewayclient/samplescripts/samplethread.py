"""Creates an example writer and sender using threads."""
from time import sleep
from bayeosgatewayclient import BayEOSWriter, BayEOSSender
import tempfile
from os import path

PATH = path.join(tempfile.gettempdir(),'bayeos-device') 
writer = BayEOSWriter(PATH)

NAME = 'Python-Thread-Example2'
URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'

writer = BayEOSWriter(PATH)
writer.save_msg('Writer was started.')

sender = BayEOSSender(PATH, NAME, URL)
sender.start()

while True:
    writer.save(values={"c1":1.2,"xx":1.7},value_type=0x61)     
    sleep(5)