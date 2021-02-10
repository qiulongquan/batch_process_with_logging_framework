#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Batch Name：framework test batch
Created date：2020-01-16
Updated date：2020-01-22
Author：QIU
Objective：远程docker容器中debug测试程序

# 先配置launch.json文件,下面是一个写好的例子
{
    "version": "0.2.0",
    "configurations": [

        {
            "name": "Attach (Remote Debug)",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "0.0.0.0",
                "port": 5678
            },
            "localRoot": "${workspaceRoot}",
            "remoteRoot": "${workspaceRoot}"
        }
    ]
}
# 然后启动这个debug test程序，然后在vscode的debug里面点击绿色的小箭头启动
# vscode底下会变成黄色，说明启动成功可以调试了
"""
import sys
import numpy as np

import ptvsd
print("waiting...")
ptvsd.enable_attach(address=("0.0.0.0", 3000))
ptvsd.wait_for_attach()

print('hello python!')

for i in range(3):
    print("aaaa")
    pass

print('python version:' + str(sys.version_info))

print('numpy version:' + np.version.full_version)
