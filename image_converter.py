import sys
import os
import glob
import subprocess

def convert_directory(dirPath, src, dest):
    # ファイルとディレクトリに仕分け
    listDir = os.listdir(dirPath)
    files = glob.glob(os.path.join(dirPath, "*." + src))
    directories = [directory for directory in listDir if os.path.isdir(os.path.join(dirPath, directory))]
    
    for file in files:
        newName = file.replace("." + src, "." + dest)
        command = ["sips", "-s", "format", dest, file, "-o", newName]
        subprocess.call(command, shell=False)
        os.remove(file)
    
    # サブフォルダも再帰的に変換
    for directory in directories:
        convert_directory(os.path.join(dirPath, directory), src, dest)

# コマンドライン引数読み取り
args = sys.argv
if len(args) != 4:
    print("Error: コマンドライン引数を入力してください！")
    exit()
dirPath = args[1]
src = args[2]
dest = args[3]

# ディレクトリかどうか判断
if not os.path.isdir(dirPath):
    print("Error: コマンドライン引数にはディレクトリのパスを指定してください！")
    exit()

# 変換開始
convert_directory(dirPath, src, dest)
