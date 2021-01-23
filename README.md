### batch 开发框架带日志输出

1.这个是带日志输出的 batch 处理框架代码。使用了 docker-compose 构筑基本服务（包含 postgres，pgadmin4，python3）。  
2.main 调用各个 function 处理。function 包含子 function 处理。  
3.使用了 logging 来输出 batch log 和 error log。  
4.通过读取 conf 配置信息来设定 logging 的各种参数。  
5.在各个子 function 中加入了异常处理获取 traceback 信息并写入 logging 的例子。  
6.采用文字一览表在 conf 配置文件中定义错误信息的具体内容。  
7.记录模块执行的时间。  
8.'shell.sh' 是 shell 文件可以在 crontab 里面设定定时启动。  
9.'shell.sh' 里面定义了同时只能有一个 batch 文件执行，如果上一次的 batch 还没有完成就不执行 batch 文件。  
10.构筑文件 docker-compose.yml 导入了 3 个服务。

### 将继续添加新功能

<br>

### 程序整体文件结构(未完成，继续更新中)

```
│  .gitignore
│  docker-compose.yml
│  README.md
│
├─docker
│  └─python
│          Dockerfile
│
├─document
│      3.236.223.144   NG
│      DDL_sample.txt
│      logging的实现.txt
│      在AWS 上面安装 docker和docker-compose.txt
│      简单使用说明.txt
│
└─storage
    ├─pgadmin
    ├─postgres
    │  └─init
    │          1_create.sql
    │
    └─python
        └─my_batch
            │  shell.sh
            │
            ├─bin
            │      batch.py
            │      data_parse_batch.py
            │      data_parse_batch_v1.1.py
            │      data_parse_batch_v1.2.py
            │      data_parse_batch_v1.3.py
            │
            ├─conf
            │      batch_conf.py
            │      batch_conf_2021_01_22.py
            │
            ├─lib
            │      customization_lib.py
            │
            ├─log
            │      20210122_232912_batch.log
            │      20210122_232912_error.log
            │
            └─tests
                    test_customization_lib.py
```
