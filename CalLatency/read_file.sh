#!/bin/zsh

# 变量ip
ip="192.168.1.52"

# 远程服务器信息
remote_username="mxh"
remote_password="mxh"
remote_server="10.8.1.52"
remote_directory="/home/mxh"

# 本地保存目录
local_directory="."

# 遍历cli_num和coro_num的所有组合
cli_num=0
coro_num=0
for cli_num in $(seq 0 $cli_num); do
  for coro_num in $(seq 0 $coro_num); do
    # 设置要匹配的文件名
    filename="insert_lat${cli_num}${coro_num}.txt"
    echo $filename

    # 执行SCP命令，从远程服务器复制文件到本地并修改文件名
    sshpass -p "$remote_password" scp "$remote_username@$remote_server:$remote_directory/$filename" "$local_directory/insert_lat${cli_num}${coro_num}${ip}.txt"
  done
done