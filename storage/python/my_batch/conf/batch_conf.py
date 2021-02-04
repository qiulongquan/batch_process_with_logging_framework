import logging
import time


# 相当于配置文件，可以加入自己需要的参数
class BatchConf(object):

    # logging error config
    # logger disabled定義
    logger_disabled_error = False
    # loggingバックアップファイル数定義
    backupCount_error = 5
    # loggingファイル最大サイズ定義
    maxBytes_error = 1024 * 1024 * 2
    # loggingファイル名定義
    logging_file_name_error = time.strftime(
        '%Y%m%d_%H%M%S', time.localtime(time.time())) + '_error.log'
    # logging_path定義
    log_path_error = 'log'
    # logging name定義
    logging_name_error = 'logger_error'
    # logging 出力レベル定義
    level_error = logging.WARNING
    # logging フォーマット定義
    formatting_error = '%(asctime)s %(levelname)s filename:%(filename)s funcName:%(funcName)s message:%(message)s'

    # logging batch config
    # logger disabled定義
    logger_disabled_batch = False
    # loggingバックアップファイル数定義
    backupCount_batch = 3
    # loggingファイル最大サイズ定義
    maxBytes_batch = 1024 * 1024
    # loggingファイル名定義
    logging_file_name_batch = time.strftime(
        '%Y%m%d_%H%M%S', time.localtime(time.time())) + '_batch.log'
    # logging_path定義
    log_path_batch = 'log'
    # logging name定義
    logging_name_batch = 'logger_batch'
    # logging 出力レベル定義
    level_batch = logging.INFO
    # logging フォーマット定義
    # formatting_batch = '%(asctime)s - filename:%(filename)s - funcName:%(funcName)s - message:%(message)s - processID:%(process)s'
    formatting_batch = '%(asctime)s %(levelname)s %(message)s'


# 字符转换类，用来实现文字一覧機能
class CharacterTransformation(object):
    c001 = "文字一覧テスト"
    e001 = "異常発生、エラーログ出力"
    e002 = "数据读取发生错误"
    i001 = "XXXX処理実行完了"


class Process_name(object):
    p001 = "XXX处理"
