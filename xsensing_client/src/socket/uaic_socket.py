"""
提供基础的类，提供socket通信能力
"""


import os
import time
import socketio


class UAICSocket(socketio.Client):
    debug = False

    def __init__(self, *args, **kwargs):
        super(UAICSocket, self).__init__(*args, **kwargs)


# debug = False
# sio = socketio.Client(logger=debug, engineio_logger=debug)
sio = UAICSocket(logger=UAICSocket.debug, engineio_logger=UAICSocket.debug)

@sio.event
def connect():
    print('Connection established')


@sio.event
def on_process(*args):
    print(f'On process: {len(args)} args: {args}')
    return args


@sio.event
def my_message(data):
    print('Client my_massage的数据', data)
    sio.emit('server_run_func', {'response': data}, callback=on_process)
    return 'xx'


@sio.event
def disconnect():
    print('Disconnected from server')


def build_sio(url):
    try:
        sio.connect(url)
    except Exception as e:
        # print(f'Connection Error')
        raise ConnectionError(f'连接错误，请确保统一接口服务端UAIS已启动。url: {url}.')

    return sio


if __name__ == '__main__':
    sio = build_sio()
    sio.connect('http://127.0.0.1:5000')

    for i in range(10):
        data = {'a': f'{i}'}
        ret = my_message(data)
        print(f'ret: {ret}')
        time.sleep(0.5)

    sio.wait()

