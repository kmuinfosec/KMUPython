# 학생 클래스를 선언합니다.
class Studnet:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def self_introduce(self):
        print("안녕하세요.")
        print("{} {}입니다.".format(self.id, self.name))
        print("만나서 반갑습니다.")


# 학생 객체를 만듭니다.
student = Studnet("김영재", 20153160)

# 메서드를 호출합니다.
student.self_introduce()
