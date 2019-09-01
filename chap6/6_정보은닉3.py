class Student:
    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def set_id(self, id):
        if id > 0:
            self.__id = id

    def get_id(self):
        return self.__id

    def __str__(self):
        return "{}학번 {}".format(self.__id, self.name)

student = Student("윤상건", 20191632)
student.__id = -20 # student인스턴스에 __id라는 새로운 변수 선언 및 초기화
print(student._Student__id) # Student클래스에서 __id로 선언된 변수 참조
print(student.__id) # student인스턴스에서 __id로 선언된 변수 참조
