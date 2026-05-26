import os

def get_file_set(directory):
    """(파일명, 크기, 내용)을 하나의 튜플로 묶어 집합(set)으로 반환"""
    file_info = set()
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                size = entry.stat().st_size
                with open(entry.path, 'rb') as f:
                    content = f.read()
                file_info.add((entry.name, size, content))
    return file_info

def compare_directories():
    dir1, dir2 = input("첫 번째 폴더: "), input("두 번째 폴더: ")

    set1 = get_file_set(dir1)
    set2 = get_file_set(dir2)

    if set1 == set2:
        print("결과: 모든 파일이 완벽히 일치합니다.")
    else:
        print("결과: 파일 수, 이름, 크기 또는 내용 중 다른 점이 있습니다.")

if __name__ == "__main__":
    compare_directories()