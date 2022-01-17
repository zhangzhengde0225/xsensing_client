
#### 本仓库是Xsensing统一AI接口客户端(Unified Artificial Intelligence Interface Client, UAIC)代码和使用说明。

本仓库提供客户端、API。

# 1 About UAIC

Xsensing的统一AI接口(Unified Artificial Intelligence Interface, UAII)分为服务端UAIS和客户端UAIC。

+ 服务端UAIS运行在GPU服务器上，统一调度不同算法模块、管理模型库，执行AI计算任务；
+ 客户端UAIC运行在应用服务器上，通过Socket与UAIS通讯，可远程查看UAIS运行情况；自定义处理流程、管道和模块；管理UAIS；获取UAIS的输出。
# 2 Getting Started
## 2.1 安装
### 源码安装
```python
git clone https://github.com/zhangzhengde0225/xsensing_client.git
cd xsensing_client
python setup.py install
```
### pip安装
```python
pip install xsensing_client
```

# 2.2 样例

Client Examples，下面是一个简单的客户端代码。

```python
import xsensing_client

uaic = xsensing_client.UAIC(url='http://127.0.0.1:5000')  # 连接到UAIS服务器

uaic.ps()  # 查看服务器流、管道和模块的状态

uaic.stop(stream=None, pipeline=None, module=None)  # 停止流，无参数时，停止全部；指定流时停止指定的流；指定管道或模块时，停止与之相关的所有流
uaic.get_cfg()  # 从服务器读取各流、管道、模块的默认配置文件，保存到本地。
uaic.configure(config_file='config.py')  # 上传服务端的流、管道和模块配置文件，更新服务端配置。
uaic.start(stream=None)  # 启动流，无参数是启动所有流；指定流时启动指定的流；启动流的同时调起所有相关管道和模块。

uaic.scan(pipeline=None)  # 窥视指定管道的输出。

```

# 3 详细文档

[客户端文档](https://github.com/zhangzhengde0225/xsensing_client/blob/master/docs/client_doc.md)


