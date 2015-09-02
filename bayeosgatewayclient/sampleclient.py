"""Creates an example client."""

from bayeosgatewayclient import BayEOSGatewayClient
from random import randint

OPTIONS = {'bayeosgateway_url' : 'http://bayconf.bayceer.uni-bayreuth.de/gateway/frame/saveFlat',
           'bayeosgateway_password' : 'import',
           'bayeosgateway_user' : 'import',
           'max_chunk' : 300,
           'writer_sleep_time' : 1,
           'sender' : 'sender',
           'backup_path' : '/tmp/backup_client/'}

NAMES = ['PythonTestDevice1', 'PythonTestDevice2', 'PythonTestDevice3']

class PythonTestDevice(BayEOSGatewayClient):
    """Creates both a writer and sender instance for every NAME. Implements BayEOSGatewayClient."""
    def read_data(self):
        if self.name == 'PythonTestDevice1':
            return (randint(-1, 1), 3, 4)
        else:
            return (randint(-1, 1), 4, 3)
        
    def save_data(self, data=0, origin=''):
        if self.name == 'PythonTestDevice1':
            self.writer.save(data, origin='origin')
            self.writer.save_msg('Overwritten method.')
        elif self.name == 'PythonTestDevice2':
            self.writer.save(data)

client = PythonTestDevice(NAMES, OPTIONS)

client.run()