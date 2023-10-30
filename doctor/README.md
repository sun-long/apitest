## 设计原则：
##### 1）关注业务流程，覆盖正常/异常场景
  测试用例为业务逻辑case，不仅仅覆盖主流程
##### 2）用例和接口分离，用例和用例分离
  解决用例之间的依赖关系，便于case维护、造数据
##### 3）通过命令行执行自动化测试
  支持自定义参数，指定测试环境，指定目录、文件、或函数方法执行用例
##### 4）结构清晰，支持扩展
  减少层级关系，简单灵活，方便其他业务线扩展

## 目录结构：

##### commonlib: 测试环境数据、 通用代码库
##### core: 核心代码
##### result: 测试结果，包括测试报告、测试日志、其他结果文件
##### postman: postman导出的json数据库，为接口自动生成功能提供数据
##### subjectlib: 项目产品库，各个业务线的接口、默认请求、参数
##### testcase: 测试用例库，按业务线划分 TODO
##### tools: 公共工具目录
##### conftest.py: pytest的全局设置、配置文件
##### pytest.ini: 修改pytest默认设置、日志相关设置、自定义标签注册

## 执行测试
>cd apitest
>pytest


## 主要功能
1. 支持postman导出的json文件、 目前支持get、post、delete、put（完成）
2. 支持postman导出的env文件 TODO
3. 支持多数据库的调用 mysql、mongodb 等 TODO
4. 支持CI，接入jenkins TODO


## pytest功能
参考pytest文档

/home/SENSETIME/wangan/.pyenv/versions/3.6.8/bin/python -m pytest --config=argus test_devicemanagerV2.py::TestDeviceManagerReal



pip install protoc-gen-swagger
pip install paramiko
pip install scpclient

## swagger3.0 converter swagger2.0 
sudo npm install -g api-spec-converter
sudo npm install -g n
sudo n v10
api-spec-converter --from=openapi_3 --to=swagger_2 --syntax=json parking3.0.json_bak > parking.json