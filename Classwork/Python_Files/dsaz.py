class Human():

    __name = None
    _lastname = None
    ___age = None

    def info(self):
        print(self.__name,self._lastname,self.___age)

    def set(self,name,lastname,age):
        self.__name=name
        self._lastname=lastname
        self.___age=age


class Teacher(Human):
    work_experience = None

    def __init__(self,name,lastname,age,work_experience):
        self.__name=name
        self._lastname=lastname
        self.___age=age
        self.___work_experience=work_experience

    def info(self):
        print('\n'"Name  :" + str(self.__name.title()) + '\n' + "Lastame  :" + str(self._lastname.title()) + '\n' + "Age  :" + str(self.___age) + '\n' + "Work Experience  :" + str(self.work_experience))

    def teacherToFile(self,filename):
        file=open(filename+'.txt','a')
        file.write("Name  :"+str(self.__name.title())+'\n'+"Lastame  :"+str(self._lastname.title())+'\n'+"Age  :"+str(self.___age)+'\n'+"Course  :"+str(self.work_experience))
        file.close()

    def set(self,name,lastname,age,work_experience):
        self.__name=name
        self._lastname=lastname
        self.___age=age
        self.work_experience=work_experience


class Student(Human):
    course = None
    def __init__(self,name,lastname,age,course):
        self.__name = name
        self._lastname = lastname
        self.___age = age
        self.course = course
    def info(self):
        print('\n'"Name  :"+str(self.__name.title())+'\n'+"Lastame  :"+str(self._lastname.title())+'\n'+"Age  :"+str(self.___age)+'\n'+"Course  :"+str(self.course))

    def studentToFile(self,filename):
        file=open(filename+'.txt','a')
        file.write("Name  :"+str(self.__name.title())+'\n'+"Lastame  :"+str(self._lastname.title())+'\n'+"Age  :"+str(self.___age)+'\n'+"Course  :"+str(self.course))
        file.close()

    def set(self,name,lastname,age,course):
        self.__name = name
        self._lastname = lastname
        self.___age = age
        self.course = course


class Institut():
    faculty ={}


    # TEACHERS :D      \\\\\\\\\\\\\\\

    teacher  = Teacher('a', 'a', 48, 1)
    teacher1 = Teacher('b', 'b', 40, 2)
    teacher2 = Teacher('c', 'c', 48, 3)
    teacher3 = Teacher('d', 'd', 40, 4)
    teacher4 = Teacher('e', 'e', 48, 5)
    teacher5 = Teacher('f', 'f', 48, 6)


    # STUDENTS :D      ///////////////

    student  = Student('a', 'a', 48, 1)
    student2 = Student('b', 'b', 40, 2)
    student3 = Student('c', 'c', 18, 3)
    student4 = Student('d', 'd', 18, 4)
    student5 = Student('e', 'e', 18, 5)
    student6 = Student('f', 'f', 18, 6)

    # STUDENTS AND TEACHER SEARCH
    def studentsInfo(self,studentname):
        self.__getattribute__(str(studentname)).info()

        print("Faculty : ",str(self.faculty).title())

    def teachersInfo(self,teachername):
        self.__getattribute__(str(teachername)).info()
    # FACULTATION
    def facultation(self,studentname,faculty):
        self.faculty=faculty
        self.__getattribute__(studentname).faculty=studentname







institut=Institut()

institut.teachersInfo(teachername='teacher5')
institut.studentsInfo(studentname='student4')
institut.facultation(studentname='student2',faculty='math')
institut.studentsInfo(studentname='student2')
institut.facultation(studentname='student',faculty='sience')
institut.studentsInfo(studentname='student4')










