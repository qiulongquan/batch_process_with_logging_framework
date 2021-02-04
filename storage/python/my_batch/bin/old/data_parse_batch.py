#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author：QIU
Created date：2020-01-16
Updated date：2020-01-16
Objective：用于测试batch的开发代码雏形
"""

from conf.batch_conf import BatchConf
import logging
import os
import time
import sys
# import pprint
# import click
import datetime
import numpy as np
import pandas as pd
from pathlib import Path

# 親ディレクトリをアプリケーションのホーム(${app_home})に設定
app_home = str(Path(__file__).parents[1])
# ${app_home}をライブラリロードパスに追加
sys.path.append(app_home)
# 自身の名前から拡張子を除いてプログラム名(${prog_name})にする os.path.splitext就是获取自身的文件名和扩展名
prog_name = os.path.splitext(os.path.basename(__file__))[0]

error_df = pd.DataFrame(columns=['error_time', 'バッチ名', '明細ID', 'エラーメッセージ'])
error_df = error_df.set_index('error_time')


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

    def _transform_data():
        print("_transform_data runing")

    def _change_sinkyu_master():
        print("_change_sinkyu_master runing")

    def _change_kabu_master():
        print("_change_kabu_master runing")

    def _input_master_data_sinkyu():
        print("_input_master_data_sinkyu runing")
        for i in np.array([0, 1, 0, 2]):
            try:
                print(1.0 / int(i))
            except ZeroDivisionError as e:
                # 有异常发生
                print('catch ZeroDivisionError:', e)
                _collection_error_data('株主番号変更バッチ', 1, e)
            finally:
                pass

    def _input_master_data_kabu():
        print("_input_master_data_kabu runing")

    def _check_input():
        print("_check_input runing")

    def _collection_error_data(batch_name, meisai_id, error_message):
        global error_df
        print("_collection_error_data runing")
        dict = {
            'error_time':
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            'バッチ名':
            batch_name,
            '明細ID':
            meisai_id,
            'エラーメッセージ':
            error_message
        }
        error_new = pd.DataFrame([dict]).set_index('error_time')
        error_df = pd.concat([error_df, error_new])
        # print(error_df)

    def _create_batch_log_data():
        print("_create_batch_log_data runing")

    print("shareholder_number_change runing")

    _do_ocr_result_check()
    _transform_data()
    _change_sinkyu_master()
    _change_kabu_master()
    _input_master_data_sinkyu()
    _input_master_data_kabu()
    _check_input()
    _create_batch_log_data()
    print(error_df)
    output_error_log()
    endtime = datetime.datetime.now()
    print("程序执行时间(微秒)：{}".format((endtime - starttime).microseconds))
    return df


def transaction_reason_change(df):
    print("transaction_reason_change runing")


def main_processing():
    print("main_processing runing")
    df = db_connect()
    print(df)
    return df


def output_batch_log():
    print("output_batch_log runing")


def output_error_log():
    print("output_error_log running")


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
