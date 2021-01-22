#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author：QIU
Created date：2020-01-16
Updated date：2020-01-16
Objective：用于测试batch的开发代码雏形
"""

from conf.my_batch_conf import MyBatchConf
import logging
import os
import sys
# import pprint
import click
import numpy as np
from pathlib import Path


print(MyBatchConf.key1)
# 親ディレクトリをアプリケーションのホーム(${app_home})に設定
app_home = str(Path(__file__).parents[1])
# 执行命令 python bin/batch.py - m SpecifiedValue
# parents[0]的时候返回bin
# parents[1]的时候返回. 当前目录
# parents[2]的时候边界溢出错误
# pathlib可以分析当前文件的路径并返回对应的位置
# print("__file__=", str(Path(__file__).parents[0]))

# ${app_home}をライブラリロードパスに追加
# 把.这个路径加入到lib导入搜索路径里面去，这样在导入一个自己制作的库的时候优先搜索.这个路径下面是否有
sys.path.append(app_home)
# pprint.pprint(sys.path)
# 自前のライブラリをロード
# 这里用到的就是.下面的lib目录，然后导入里面的MyLib库文件
# from lib.my_lib import MyLib

# 設定クラスのロード


# コマンドライン引数のハンドリング. must_argは必須オプション、optional_argは任意オプション
# 通过click来进行命令的检测，如果发现must arg参数没有写入就会报错
@ click.command()
# required = True表明是必须参数，必须要提交
@ click.option('--must_arg', '-m', required=True)
@ click.option('--optional_arg', '-o', default="DefaultValue")
def cmd(must_arg, optional_arg):
    # 自身の名前から拡張子を除いてプログラム名(${prog_name})にする os.path.splitext就是获取自身的文件名和扩展名
    prog_name = os.path.splitext(os.path.basename(__file__))[0]
    # print("prog_name=", os.path.basename(__file__))
    # ロガーの設定

    # フォーマット
    log_format = logging.Formatter("%(asctime)s [%(levelname)8s] %(message)s")
    # レベル
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 標準出力へのハンドラ
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(log_format)
    logger.addHandler(stdout_handler)
    # ログファイルへのハンドラ
    file_handler = logging.FileHandler(os.path.join(
        app_home, "log", prog_name + ".log"), "a+")
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # 処理開始
    try:
        # ログ出力
        logger.info("start")
        logger.info("qiulongquan")
        # コマンドライン引数の利用
        logger.error(f"must_arg = {must_arg}")
        logger.error(f"optional_arg = {optional_arg}")

        # ライブラリ呼び出し
        # mylib = MyLib()
        # logger.info(mylib.get_name())

        # 設定値の利用
        logger.info(MyBatchConf.key1)
        logger.info(MyBatchConf.key2)

        # 例外が発生しても・・・
        raise Exception("My Exception")
        logger.info("qiu_error")
    except Exception as e:
        # キャッチして例外をログに記録
        logger.exception(e)
        # sys.exit(1)


def divide_else():
    while True:
        a = int(input("a数は: "))
        b = int(input("b数は: "))
        try:
            print(a / b)
            print("processing end")
        except ZeroDivisionError as e:
            # 有异常发生
            print('catch ZeroDivisionError:', e)
        except ValueError:
            print("数字を入力してください")
            continue
        else:
            # 正常结束
            print('finish (no error)')
            # 不管是正常结束还是异常结束都会执行finally部分
        finally:
            print('all finish')


# 异常判断然后正常情况下在判断再异常处理
def process1():
    kill = [1, 2, 5, 6]

    while True:
        try:
            kill_count = input("キル数は: ")
        except EOFError:
            print('終了します')
            break

        if not kill_count:
            print('入力してください')
            continue

        try:
            kill_count = int(kill_count)
        except ValueError:
            print('整数値を入力してください')
            continue

        kill_tmp = kill + [kill_count]
        print(f'平均キル数: {sum(kill_tmp) / len(kill_tmp)}')


def except_test_for():
    l1 = np.arange(0, 5, 1)
    print(l1)
    for i in l1:
        try:
            print(1.0 / int(i))
        except ZeroDivisionError as e:
            # 有异常发生
            print('catch ZeroDivisionError:', e)
        finally:
            print('本次结束，进行下一次计算')


if __name__ == '__main__':
    # cmd()

    # 下面是调用异常处理模块，正常结束的时候和非正常结束的表现
    # divide_else()

    # 异常判断然后正常情况下在判断再异常处理
    # process1()

    # 使用for进行循环然后for里面使用try except进行异常判断，可以正常输出异常并继续下一次运行
    except_test_for()
