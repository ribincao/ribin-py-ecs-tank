# py-ecs-tank

该项目是基于 ecs 框架复刻的一个单机/联机坦克大战游戏,项目主要用到 pygame 依赖

## 说明

1. 项目中服务端分两层
   - 网络层:负责接受客户端发来的指令以及定时发送快照给客户端同步 world
   - 逻辑层:负责运行整个 world
2. 项目中的客户端简单分了四层:
   - 渲染层:目前使用的是 pygame,用来渲染 behavior.如果将来有更方便的 GUI 库也可以直接替换
   - 表现层:主要是完成逻辑层 entity 和 behavior 的绑定,同时向渲染层提供 behavior 以及 animation 的渲染
   - 逻辑层:和服务端公用一套代码保证逻辑的一致,同时定时接受客户端的快照去较正状态
   - 网络层:负责接受服务端的快照进行同步以及定时向服务端发送指令同步操作

## 使用

1. 安装pygame

```shell
pip3 install pygame
```

2. 导出LogicEntity(每次新增component组件需要在component_manager上注册并重新导出LogicEntity)

```shell
cd ./logic/manager/
python3 component_manager.py

```

3. 单机玩法直接启动client.py

```python
python3 client.py
```

3. 联机玩法需要先启动server.py再启动client.py

```python
python3 server.py
python3 client.py  # 如果想多人联机的话就多开几个终端执行
```

日志: 可以通过修改 common/logger.py 文件里的 log_mode 为 LOG_MODE_CONSOLE/LOG_MODE_FILE 来选择输出日志到终端还是文件

## 玩法

1. n - 创建当前玩家
2. wasd - 对应移动
3. j - 射击
4. t - 创建一个机器敌人
