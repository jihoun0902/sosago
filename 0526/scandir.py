import os

def scan_directory(path):
    with os.scandir(path) as entries:
        for entry in entries:
            print(entry.path)
            if entry.is_dir():
                scan_directory(entry.path)

base_path = input("탐색할 폴더 경로를 입력하세요: ")
scan_directory(base_path)