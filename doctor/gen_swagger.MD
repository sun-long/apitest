python main.py gen_swagger -d sptu -i '{"GenieService":"http://staging.argus.sensetime.com/genie-cloud", "IoTService":"http://staging.argus.sensetime.com/argus-iot", "VideoDeviceDirector":"http://staging.argus.sensetime.com/argus-iot-vdd"}'

python main.py gen_swagger -d minos -i '{"account":"http://staging.argus.sensetime.com/minos/mnt", "minos_agent_service":"http://staging.argus.sensetime.com/minos/minos-agent", "minos_ingress_service":"http://staging.argus.sensetime.com/minos/minos-ingress", "service":"http://staging.argus.sensetime.com/minos/audit-service"}'
python main.py gen_swagger -d minos -i '{"account":"https://sensespace-ioc.sensetime.com/minos/mnt", "minos_agent_service":"https://sensespace-ioc.sensetime.com/minos/minos-agent", "minos_ingress_service":"https://sensespace-ioc.sensetime.com/minos/minos-ingress", "service":"https://sensespace-ioc.sensetime.com/minos/audit-service"}'
python main.py gen_all_template -s minos


更新远程主机的swagger方法：
准备：
在swagger目录下创建一个remote_swagger.csv文件：内容格式如下：
parking,https://confluence.sensetime.com/download/attachments/331047888/openapi.json
如果该地址访问需要权限，请在同目录下创建一个cookie文件,使用的时候贴入cookie即可
命令：
python main.py update_swagger_json -d parking

python main.py update_swagger_json -d nebula
python main.py gen_all_template -s nebula


生成nebula测试框架需要的defines及__init__.py
python main.py gen_nebula_template -s nebula

https://sensespace-ioc.sensetime.com/minos/mnt/api/v1/role/list
https://sensespace-ioc.sensetime.com/minos/mnt/api/v1/role/list


aiot_private
python main.py update_swagger_json -d aiot_private
python main.py gen_all_template -s aiot_private