# 특정 디렉터리의 모든 하위 디렉터리 찾기_개선
import os
import queue


def get_subdir(path):
    # 검색이 허가되지 않은 디렉터리 접근에 관한 예외처리
    try:
        dirfiles = os.listdir(path)
    except PermissionError:
        return []

    subdir_list = []
    for each in dirfiles:
        full_name = path + each
        if os.path.isdir(full_name):
            subdir_list.append(full_name + "/")
    return subdir_list


dir_queue = queue.Queue()
dir_queue.put("시작 경로/")   # 검색하고자 하는 디렉터리를 줄 앞에 세움

all_dirs = []
while not dir_queue.empty():   # 큐가 비어있는 상태인지 확인
    dir_name = dir_queue.get()
    all_dirs.append(dir_name)

    subdir_names = get_subdir(dir_name)
    for each in subdir_names:
        dir_queue.put(each)

print(all_dirs)