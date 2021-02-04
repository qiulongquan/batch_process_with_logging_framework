#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Batch Name：framework test batch
Created date：2020-01-16
Updated date：2020-01-22
Author：QIU
Objective：用于测试batch的开发代码雏形
"""

import sys
from pathlib import Path
# 获取my_batch的绝对路径，然后加入到sys.path系统路径中去，这样系统运行的时候就可以找到conf这个自定义库了
sys.path.append(str(Path(__file__).parents[1]))
from conf.batch_conf import CharacterTransformation
from conf.batch_conf import BatchConf
from logging.handlers import RotatingFileHandler
import pandas as pd
import numpy as np
import datetime
import os
import logging

# import time
# import click


# ロギングのインスタンス定義
def get_logger(logger_disabled, logging_name, level, log_path,
               logging_file_name, maxBytes, backupCount, formatting):
    # 親ディレクトリをアプリケーションのホーム(${app_home})に設定
    app_home = str(Path(__file__).parents[1])
    # logging设定
    logger = logging.getLogger(logging_name)
    logger.setLevel(level=level)
    # error logging conf定義
    # 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大2MB
    # rHandler = RotatingFileHandler(os.path.join(app_home, log_path,
    #                                             logging_file_name),
    #                                encoding="utf-8",
    #                                maxBytes=maxBytes,
    #                                backupCount=backupCount)
    # rHandler.setLevel(level)
    # formatter = logging.Formatter(formatting)
    # rHandler.setFormatter(formatter)
    # logger.addHandler(rHandler)
    # logger.disabled = logger_disabled

    # 还有一种定义是filehandler  这种方式不进行日志回滚
    filehandle = logging.FileHandler(os.path.join(app_home, log_path,
                                                  logging_file_name),
                                     encoding="utf-8")
    filehandle.setLevel(level=level)
    formatter = logging.Formatter(formatting)
    filehandle.setFormatter(formatter)
    logger.addHandler(filehandle)
    return logger


# ロギング対象（logging_batch）作成
logging_batch = get_logger(
    BatchConf.logger_disabled_batch, BatchConf.logging_name_batch,
    BatchConf.level_batch, BatchConf.log_path_batch,
    BatchConf.logging_file_name_batch, BatchConf.maxBytes_batch,
    BatchConf.backupCount_batch, BatchConf.formatting_batch)

# ロギング対象（logging_error）作成
logging_error = get_logger(
    BatchConf.logger_disabled_error, BatchConf.logging_name_error,
    BatchConf.level_error, BatchConf.log_path_error,
    BatchConf.logging_file_name_error, BatchConf.maxBytes_error,
    BatchConf.backupCount_error, BatchConf.formatting_error)


def db_connect():
    print("db_connect runing")
    df = pd.DataFrame(np.array(
        [np.arange(1, 5),
         np.arange(11, 15),
         np.arange(101, 105)]),
                      columns=['帳票分類コード', '会社コード', '基準日', '株主番号'])
    return df


def shareholder_number_change(df):
    starttime = datetime.datetime.now()

    def _do_ocr_result_check():
        print("_do_ocr_result_check runing")
        # 除数为0的时候抛出异常并写入日志文件
        # 抛出一个异常可以是Exception，或者ValueError
        for i in np.array([0, 0, 3, 1, 0]):
            try:
                if i == 0:
                    raise ValueError("error!")
                    # raise Exception
            except ValueError:
                # 有异常发生
                print('when i={} ,ZeroDivisionError'.format(i))
                # 这里需要定义一下输出内容和格式
                logging_error.error('when i={} ,ZeroDivisionError'.format(i))

    def _transform_data():
        print("_transform_data runing")

    def _change_sinkyu_master():
        print("_change_sinkyu_master runing")

    def _change_kabu_master():
        print("_change_kabu_master runing")

    def _input_master_data_sinkyu():
        print("_input_master_data_sinkyu runing")
        for i in np.arange(1, 3):
            try:
                raise IOError
            except IOError as e:
                # 有异常发生
                print('IOError:', e)
                # 这里需要定义一下输出内容和格式
                logging_error.error(CharacterTransformation.e002)
            finally:
                logging.exception('this is warning message')

    def _input_master_data_kabu():
        print("_input_master_data_kabu runing")
        try:
            f = open('myfile.txt')
            s = f.readline()
            print(s)
        except OSError as e:
            print("OS error: {0}".format(e))
            logging_error.error("Exception occurred:{}".format(e))
        except ValueError as e:
            print("Could not convert data to an integer.")
            logging_error.error("Exception occurred:{}".format(e))
        except:
            print("Unexpected error:", sys.exc_info()[0])
            logging_error.error("Exception occurred")

    def _check_input():
        print("_check_input runing")
        arg = 'data_parse_batch_v1.3.py'
        home = str(Path(__file__).parents[0])
        try:
            print("file_path={}".format(os.path.join(home, arg)))
            f = open(os.path.join(home, arg), 'rb')
        except OSError as e:
            print('cannot open', arg)
            logging_error.error(e)
        else:
            file_open_message = "{} has {} lines.".format(
                arg, len(f.readlines()))
            print(file_open_message)
            logging_batch.info(file_open_message)
            f.close()

    print("shareholder_number_change runing")

    _do_ocr_result_check()
    _transform_data()
    _change_sinkyu_master()
    _change_kabu_master()
    _input_master_data_sinkyu()
    _input_master_data_kabu()
    _check_input()
    logging_batch.info(CharacterTransformation.i001)
    endtime = datetime.datetime.now()
    print("程序执行时间(微秒)：{}".format(endtime - starttime))
    return df


def transaction_reason_change(df):
    print("transaction_reason_change runing")


def main_processing():
    print("main_processing runing")
    df = db_connect()
    print(df)
    return df


def image_transmission(df):
    print("image_transmission runing")


def update_status(df):
    print("update_status runing")


def create_csv_file(df):
    print("create_csv_file runing")


if __name__ == '__main__':
    df = main_processing()
    shareholder_number_change(df)
    transaction_reason_change(df)
    create_csv_file(df)
    image_transmission(df)
    update_status(df)
