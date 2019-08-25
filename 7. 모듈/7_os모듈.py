# os모듈 활용_디렉터리와 파일 분리해서 저장
import os

path = "C:/"
dirfiles = os.listdir(path)
dir_names = []
file_names = []

for each in dirfiles:
    full_name = path + each

    # full_name이 디렉터리인지 판단
    if os.path.isdir(full_name):
        dir_names.append(full_name + "/")
    else:
        file_names.append(full_name)

print("dir names: ")
print(dir_names)
print("file names: ")
print(file_names)