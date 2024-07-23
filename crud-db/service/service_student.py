from models.student import Student


class StudentService():
    
    @staticmethod
    def create_student(name, last_name, age):
        student = Student.create(name=name, last_name=last_name, age=age)
        return student
    
    @staticmethod
    def get_all_students():
        return list(Student.select())
    
    @staticmethod
    def delete_student(student_id):
        student = Student.get_by_id(student_id)
        student.delete_instance()
        