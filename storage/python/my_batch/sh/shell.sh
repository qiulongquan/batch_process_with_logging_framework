#!/usr/bin/bash
path=my_batch/bin/batch.py
# path=test.py
# echo $path
shell_log=my_batch/log/shell.log
file_name=batch

if [ -f  $shell_log ];then
	cat $shell_log
fi

PythonPid=`ps -ef | grep $path | grep -v grep | wc -l`

if [ $PythonPid -eq 0 ]; then
	echo "`date "+%Y-%m-%d %H:%M:%S"`:$file_name is not running. now start running." >> $shell_log
	python3 $path
else
	echo "`date "+%Y-%m-%d %H:%M:%S"`:$file_name is running. stop running new batch." >> $shell_log
fi


# 使用vscode查看一下使用LF 换行就可以正常执行程序了，不要使用CRLF他是回车换行
# CRLF 是carriagereturnline feed的缩写。中文意思是回车换行。
# LF是line feed的缩写，中文意思是换行。
