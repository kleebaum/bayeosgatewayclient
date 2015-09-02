"""Creates an example sender."""

# from time import sleep
from bayeosgatewayclient import BayEOSSender

PATH = '/tmp/bayeos-device1/'
BACKUP_PATH = '/tmp/backup_path/'
NAME = 'Python-Test-Device'
URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'
#URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveMatrix'
sender = BayEOSSender(PATH, NAME, URL, 'import', 'import', backup_path = BACKUP_PATH)

sender.run()

# while True:
#     res = sender.send()
#     if res > 0:
#         print 'Successfully sent ' + str(res) + ' frames.\n'
#     sleep(5)