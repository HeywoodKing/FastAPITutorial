# FastAPI

## 依赖
>python3.5+
>starlette
>pydantic


## 安装
```
fastapi
(uvicorn | daphne | Hypercorn | Gunicorn)
invoke

虚拟环境
pip install poetry

进入pipenv虚拟环境
poetry shell

安装fastapi
poetry add fastapi
poetry add uvicorn
poetry add daphne
poetry add hypercorn
poetry add gunicorn
poetry add invoke

```

## 启动，不用这么麻烦的启动方式
```
进入虚拟环境
poetry shell
进入目录
cd fastapitutorial

启动API有两种方法
第一种：
项目根目录下启动

启动Factory API
uvicorn setup:factory --host 192.168.1.79 --port 8080 --reload


第二种：
进入到各个api模块中启动
cd factory
启动Factory API
uvicorn run:app --host 192.168.1.79 --port 8080 --reload
```
以上嫌繁琐，使用下面命令

## 启动，改进为Python worker.py
```
进入项目根目录
cd fastapitutorial
激活虚拟环境
poetry shell
运行启动命令
python worker.py
```
以上嫌繁琐，使用下面命令

## 启动，改进为自动化工具
```
进入项目根目录
cd fastapitutorial
激活虚拟环境
poetry shell
运行启动命令
invoke deploy
还是有点繁琐，使用下面命令
invoke d
还是有点繁琐，使用下面命令
inv deploy
还是有点繁琐，使用下面命令
inv d
只剩4个字母了，如果还嫌繁琐的话那就割了吧，不用敲键盘了，哈哈
```

