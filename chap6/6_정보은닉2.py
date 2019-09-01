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


student = Student("윤상건", 0)
student.__id = 20191632
print(student)
student.set_id(20191632)
print(student)
