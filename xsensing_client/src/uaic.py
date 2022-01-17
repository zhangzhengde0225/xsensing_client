
"""
unified ai interface client
"""
import os, sys
import time

from xsensing_client.src.socket import socket_example_client
from .socket import uaic_socket


import logging
logger = logging.getLogger(__file__)


class UnifiedAIClient(object):

    def __init__(self, sio=None, url=None):
        self.sio = sio if sio else uaic_socket.build_sio(url)

        self.timeout = 5
        # recived info
        self._ps_data = None

    def info(self):
        """服务端的信息"""
        return 'xx'

    def ps_callback(self, *args):  # ps callback
        # print(f'ps_cb args: {args}')
        self._ps_data = None if len(args) == 0 else args[0]

    def ps(self, timeout=None):
        """服务端的模块信息"""
        logger.info(msg='psssssss')
        self.sio.emit('ps', {}, callback=self.ps_callback)
        timeout = timeout if timeout else self.timeout
        t0 = time.time()
        while True:
            if self._ps_data:
                return self._ps_data
            if time.time() - t0 > timeout:
                raise TimeoutError(f'timeout. {timeout}')

    def stop(self):
        pass

    def start(self):
        pass

    def get_cfg(self):
        pass

    def configure(self):
        pass

    def scan(self):
        pass


def run(url):
    sio = socket_example_client.build_sio(url)
    uaic = UnifiedAIClient(sio)

    print(f'info: {uaic.info()}')
    ps_info = uaic.ps()
    print(f'ps: {ps_info}')


if __name__ == '__main__':
    urll = 'http://127.0.0.1:5000'
    run(urll)
