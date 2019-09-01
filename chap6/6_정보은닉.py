class Student:
    def __init__(self, name, id):
        self.name = name
        self.__id = id
        def __str__(self):
            return "{}학번 {}".format(self.__id, self.name)

student = Student("윤상건", 20191632)
student.id = 20220001
print(student)
