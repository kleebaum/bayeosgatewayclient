"""Creates an example writer and sender using threads."""

from time import sleep
from bayeosgatewayclient import BayEOSWriter, BayEOSSender

PATH = '/tmp/bayeos-device/'
NAME = 'Python-Thread-Example2'
URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'

writer = BayEOSWriter(PATH,max_time=10)
writer.save_msg('Writer was started.')

sender = BayEOSSender(PATH, NAME, URL)
sender.start()

while True:
    print 'adding frame'
    writer.save([2.1, 3, 20.5])
    sleep(5)