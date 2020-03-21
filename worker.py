# -*- encoding: utf-8 -*-
"""
@File           : worker.py
@Time           : 2019/12/2 20:13
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : fastapitutorial
@description    : 描述
"""
import os
import sys
import time
import subprocess
from config import *
from threading import Thread
from multiprocessing import Process

# from concurrent.futures.thread import ThreadPoolExecutor
# from concurrent.futures.process import ProcessPoolExecutor

"""
daphne
daphne -b 192.168.1.79 -p 8091 run:app
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

pwd = os.getcwd()


# api 启动统一入口
def start_api(item):
    """
    api 启动统一入口
    :param item:
    :return:
    """
    try:
        cmd = r"{}/{}".format(pwd, item['name'])
        os.chdir(cmd)

        if str(item['wsgi']).lower() == 'uvicorn':
            # uvicorn
            args = """{} {}:{} --host {} --port {} --limit-concurrency 100 --loop asyncio
            --timeout-keep-alive 5 """.format(item['wsgi'], item['module'], item['app'], item['host'], item['port'])
        elif str(item['wsgi']).lower() == 'gunicorn':
            # gunicorn
            args = "{} --workers=4 --bind={}:{} {}:{}".format(item['wsgi'], item['host'], item['port'], item['module'],
                                                              item['app'])
        elif str(item['wsgi']).lower() == 'hypercorn':
            args = "{} --workers=4 --bind={}:{} {}:{}".format(item['wsgi'], item['host'], item['port'], item['module'],
                                                              item['app'])
        else:
            # daphne
            args = "{} -b {} -p {} {}:{}".format(item['wsgi'], item['host'], item['port'], item['module'], item['app'])

        os.system(command=args)

    except Exception as ex:
        print('{}>>{}:{} api 服务启动异常，{}'.format(item['name'], item['host'], item['port'], ex))


def main():
    # print('当前路径 {}'.format(pwd))
    # sub = subprocess.Popen("pipenv shell", shell=True, stdout=subprocess.PIPE)
    # sub.wait()
    # print(sub.read())
    # os.system('pipenv shell')
    # os.system('dir')

    # t1 = Thread(target=start_factory)
    # t1.start()
    # p1 = Process(target=start_factory)
    # p1.start()

    for item in API_LIST:
        if IS_THREAD_RUN_METHOD:
            t = Thread(target=start_api, args=(item,))
            t.start()

        else:
            p = Process(target=start_api, args=(item,))
            p.start()

        time.sleep(1)


if __name__ == '__main__':
    main()
