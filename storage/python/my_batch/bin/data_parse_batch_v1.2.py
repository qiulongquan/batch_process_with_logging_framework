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
sys.path.append(str(Path(__file__).parents[1]))
from conf.batch_conf import CharacterTransformation
from conf.batch_conf import Process_name
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
def get_logger(logger_disabled, logging_name, level, log_path, logging_file_name, maxBytes, backupCount, formatting):
    # 親ディレクトリをアプリケーションのホーム(${app_home})に設定
    app_home = str(Path(__file__).parents[1])
    # logging设定
    logger = logging.getLogger(logging_name)
    logger.setLevel(level=level)
    # error logging conf定義
    rHandler = RotatingFileHandler(os.path.join(
        app_home, log_path, logging_file_name), encoding="utf-8", maxBytes=maxBytes, backupCount=backupCount)
    rHandler.setLevel(level)
    formatter = logging.Formatter(formatting)
    rHandler.setFormatter(formatter)
    logger.addHandler(rHandler)
    logger.disabled = logger_disabled
    return logger


# ロギング対象（logging_batch）作成
logging_batch = get_logger(BatchConf.logger_disabled_batch, BatchConf.logging_name_batch, BatchConf.level_batch, BatchConf.log_path_batch,
                           BatchConf.logging_file_name_batch, BatchConf.maxBytes_batch, BatchConf.backupCount_batch, BatchConf.formatting_batch)

# ロギング対象（logging_error）作成
logging_error = get_logger(BatchConf.logger_disabled_error, BatchConf.logging_name_error, BatchConf.level_error, BatchConf.log_path_error,
                           BatchConf.logging_file_name_error, BatchConf.maxBytes_error, BatchConf.backupCount_error, BatchConf.formatting_error)

processed_record = 0
error_record = 0


def db_connect():
    print("db_connect runing")
    df = pd.DataFrame(
        np.array([np.arange(1, 5), np.arange(11, 15), np.arange(101, 105)]), columns=['帳票分類コード', '会社コード', '基準日', '株主番号'])
    return df


def shareholder_number_change(df):
    starttime = datetime.datetime.now()
    process_name = Process_name.p001
    total_process_record = len(df)
    process_status_result = " 処理名:{}\n 処理開始時間:{}\n 予定処理件数:{}".format(process_name,starttime,total_process_record)
    logging_batch.info(process_status_result)

    
    def _input_master_data_sinkyu():
        print("_input_master_data_sinkyu runing")
        for i in np.arange(1, 3):
            try:
                raise IOError
            except IOError as e:
                # 出力フォーマット定義
                logging_error.exception(CharacterTransformation.e002)
                global error_record
                error_record += 1

    def _input_master_data_kabu():
        print("_input_master_data_kabu runing")

    def _check_input():
        print("_check_input runing")
        
    def _change_sinkyu_master():
        print("_change_sinkyu_master runing")
        global processed_record
        processed_record = 3

    def _change_kabu_master():
        print("_change_kabu_master runing")

    def _create_batch_log_data():
        endtime = datetime.datetime.now()
        processed_time = endtime - starttime
        process_status_result = " 処理終了時間:{}\n 処理時間:{}\n 実際処理件数:{}\n エラー件数:{}\n ".format(endtime,processed_time,processed_record,error_record)
        return process_status_result
    
    # print("shareholder_number_change runing")
    _input_master_data_sinkyu()
    _input_master_data_kabu()
    _check_input()
    _change_sinkyu_master()
    _change_kabu_master()
    process_status_result = _create_batch_log_data()
    # print("processed time(microseconds)：{}".format(processed_time))
    logging_batch.info(process_status_result)
    # logging_batch.info(CharacterTransformation.i001)
    return df


def transaction_reason_change(df):
    print("transaction_reason_change runing")


def main_processing():
    print("main_processing runing")
    df = db_connect()
    print(df)
    # 他の処理。。。。
    return df


def image_transmission(df):
    print("image_transmission runing")
    # 他の処理。。。。


def update_status(df):
    print("update_status runing")
    # 他の処理。。。。


def create_csv_file(df):
    print("create_csv_file runing")
    # 他の処理。。。。


if __name__ == '__main__':
    df = main_processing()
    shareholder_number_change(df)
    transaction_reason_change(df)
    create_csv_file(df)
    image_transmission(df)
    update_status(df)
