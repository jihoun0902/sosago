import os

def find_txt_files(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith('.txt'):
                    print(f"찾은 파일: {entry.path}")
                
                elif entry.is_dir():
                    find_txt_files(entry.path)
    except PermissionError:
        pass

base_path = input("텍스트 파일을 찾을 폴더 경로를 입력하세요: ")
find_txt_files(base_path)