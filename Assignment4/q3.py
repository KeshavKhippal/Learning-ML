class Student:
    def __init__(self, name, rollno, marks):
        self.set_name(name)
        self.set_rollno(rollno)
        self.set_marks(marks)

    def set_name(self, name):
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = name

    def set_rollno(self, rollno):
        if rollno < 1 or rollno > 100:
            raise ValueError("Roll number must be between 1 and 100")
        self.__rollno = rollno

    def set_marks(self, marks):
        if marks < 0:
            raise ValueError("Marks cannot be negative")
        self.__marks = marks

    def get_name(self):
        return self.__name

    def get_rollno(self):
        return self.__rollno

    def get_marks(self):
        return self.__marks