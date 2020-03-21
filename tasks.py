# -*- encoding: utf-8 -*-
"""
@File           : tasks.py
@Time           : 2020/3/16 13:36
@Author         : Flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : fastapitutorial
@description    : 描述
"""
from datetime import datetime
from invoke import task


@task()
def d(c):
    """
    local task automation debugging tools (fastapi service)
    :param c:
    :return:
    """
    deploy(c)


@task(help={})
def deploy(c):
    """
    local task automation debugging tools (fastapi service)
    :param c:
    :return:
    """
    c.run('echo fastapi service start')
    c.run('echo {}'.format('*' * 100))
    c.run('echo author:flack')
    c.run('echo date:{}'.format(datetime.now()))
    c.run('echo descr:{}'.format('自动化任务调式启动fastapi服务'))
    c.run('echo version:{}'.format('v2.0.1'))
    c.run('echo {}'.format('*' * 100))
    c.run('python worker.py')
    c.run('echo fastapi service stop')
    c.run('echo {}'.format('*' * 100))
