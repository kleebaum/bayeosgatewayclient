# bayeosgatewayclient
A Python package to transfer client (sensor) data to a BayEOS Gateway.

![](https://github.com/kleebaum/writer-sender.png)

## Installation
You can either use the setup.py script, the Python Package Index (PIP) or a Linux binary to install the package.

### Setup.py
Do the following steps to install the package via the setup.py script:
- git clone request ```git clone git://github.com/kleebaum/bayeosgatewayclient.git```
- find the right directory ```cd bayeosgatewayclient```
- run ```python setup.py install``` as root

### PIP
- run ```pip2.7 install bayeosgatewayclient```

### Linux Binary (for Debian)
- add the following repositories to /etc/apt/sources.list ```deb http://www.bayceer.uni-bayreuth.de/repos/apt/debian wheezy main```
- install key ```wget -O - http://www.bayceer.uni-bayreuth.de/repos/apt/conf/bayceer_repo.gpg.key | apt-key add -```
- ```apt-get update```
- ```apt-get install python-bayeosgatewayclient```

Alternatively:
- run ```dpkg -i python-bayeosgatewayclient_0.1-1_all.deb``` as root

## Example usage
Import the package ```import bayeosgatewayclient```.

### Writer
A simple writer looks like this:
```
from time import sleep
from bayeosgatewayclient import BayEOSWriter

writer = BayEOSWriter('/tmp/bayeos-device1/')
writer.save_msg('BayEOS Writer was started.')

while True:
    print 'adding frame\n'
    writer.save([2.1, 3, 20.5])
    sleep(1)
```

A BayEOSWriter constructor takes the following arguments:
```
PATH = '/tmp/bayeos-device1/'	# directory to store .act and .rd files
MAX_CHUNK = 2000				# file size in bytes
MAX_TIME = 60					# time when a new file is started in seconds
writer = BayEOSWriter(path=PATH, max_chunk=MAX_CHUNK, max_time=MAX_TIME)
```

The following methods could also be of interest:
- save integer values: ```writer.save(values=[1,2,3], value_type=0x22)```
- save with channel indices: ```writer.save([[1,2.1], [2,3], [3,20.5]], value_type=0x41)``` or
  ```writer.save({1: 2.1, 2: 3, 3: 20.5}, value_type=0x41)```
- save with channel offset: ```writer.save([2.1, 3, 20.5], value_type=0x02, offset=2)```
- save origin: ```writer.save([2.1, 3, 20.5], origin='Writer-Example')```
- save error message: ```writer.save_msg('error message', error=True)```

### Sender
A simple sender looks like this:
```
from time import sleep
from bayeosgatewayclient import BayEOSSender

sender = BayEOSSender('/tmp/bayeos-device1/', 
					  'Test-Device', 
					  'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat')

while True:
    res = sender.send()
    if res > 0:
        print 'Successfully sent ' + str(res) + ' frames.'
    sleep(5)
```

A BayEOSSender constructor takes the following arguments:
```
PATH = '/tmp/bayeos-device1/'	# directory to look for .rd files
NAME = 'Test-Device'
URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'
USER = 'import'					# user name to access the BayEOS Gateway
PASSWORD = 'import'				# password to access the BayEOS Gateway
BACKUP_PATH = '/home/.../' 		# backup path to store file if a) sending does not work 
								  or b) sending was successful but files but files 
								  shall be kept (renamed from .rd to .bak extension)

sender = BayEOSSender(path=PATH, 
					  name=NAME, 
					  url=URL, 
					  password=PASSWORD,
					  user=USER,
					  absolute_time=True, # if true writer, else sender time is used
					  remove=True,		  # .rd files deleted after successfully sent
					  backup_path=BACKUP_PATH)
```

The following methods could also be of interest:
- substitute the loop: ```sender.run(sleep_sec=5)```
- start sender as a separate thread ```sender.start(sleep_sec=5)```
- start sender as a separate process ```sender.start(sleep_sec=5, thread=False)```

### Connect writer and sender
Usually, the writer and sender are operating concurrently, although they are not
linked directly, i. e., they only share the same directory. 

A simple script to connect one writer-sender pair looks like this:
```
from bayeosgatewayclient import BayEOSWriter, BayEOSSender

PATH = '/tmp/bayeos-device/'
NAME = 'Writer-Sender-Example'
URL = 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat'

writer = BayEOSWriter(PATH)
writer.save_msg('Writer was started.')

sender = BayEOSSender(PATH, NAME, URL)
sender.start() 	# sender runs in a concurrent thread

while True:
    print 'adding frame'
    writer.save([2.1, 3, 20.5])
    sleep(5)
```

Another way to combine writer-sender pairs is using the BayEOSGatewayClient class:
```
from bayeosgatewayclient import BayEOSGatewayClient

OPTIONS = {'bayeosgateway_url' : 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat',
           'bayeosgateway_password' : 'import',
           'bayeosgateway_user' : 'import'}

NAMES = ['PythonTestDevice1', 'PythonTestDevice2', 'PythonTestDevice3']

class PythonTestDevice(BayEOSGatewayClient):
    """Creates both a writer and sender instance for every NAME in NAMES. Implements BayEOSGatewayClient."""
    def read_data(self):
    	"""Must be overwritten."""
        if self.name == 'PythonTestDevice1':
            return (2.1, 3, 20.5)
        else:
            return (42)
        
    def save_data(self, data=0, origin=''):
    	"""Can be overwritten."""
        if self.name == 'PythonTestDevice1':
            self.writer.save(data, origin='origin')
            self.writer.save_msg('Overwritten method.')
        elif self.name == 'PythonTestDevice2':
            self.writer.save(data)

client = PythonTestDevice(NAMES, OPTIONS)

client.run()
```