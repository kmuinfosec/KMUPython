# 학생 클래스를 선언합니다.
class Studnet:
    def __init__(self, name, id):
        print("생성자가 실행되었습니다.")
        self.name = name
        self.id = id

    def __del__(self):
        print("소멸자가 실행되었습니다.")
        

# 학생 객체를 만듭니다.
student = Studnet("김영재", 20153160)

print(student.name)
print(student.id)
