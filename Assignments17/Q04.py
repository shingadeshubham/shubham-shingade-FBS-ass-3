
class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.student_id = input("Enter Student ID: ")
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Percentage: {self.percentage}")

    def calculate_rank(self):
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 80:
            return "A"
        elif self.percentage >= 70:
            return "B"
        elif self.percentage >= 60:
            return "C"
        else:
            return "D"

    def __str__(self):
        return (f"Student[ID={self.student_id}, Name={self.name}, "
                f"Age={self.age}, Percentage={self.percentage}, "
                f"Rank={self.calculate_rank()}]")



class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks

    def calculate_rank(self):
        total = (self.percentage * 0.8) + (self.internal_marks * 0.2)
        if total >= 90:
            return "A+"
        elif total >= 80:
            return "A"
        elif total >= 70:
            return "B"
        elif total >= 60:
            return "C"
        else:
            return "D"

    def __str__(self):
        return (f"EnggStudent[ID={self.student_id}, Name={self.name}, "
                f"Age={self.age}, Branch={self.branch}, "
                f"Internal Marks={self.internal_marks}, "
                f"Percentage={self.percentage}, Rank={self.calculate_rank()}]")



class MedicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, marks_of_internship):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship

    def calculate_rank(self):
        total = (self.percentage * 0.7) + (self.marks_of_internship * 0.3)
        if total >= 90:
            return "A+"
        elif total >= 80:
            return "A"
        elif total >= 70:
            return "B"
        elif total >= 60:
            return "C"
        else:
            return "D"

    def __str__(self):
        return (f"MedicalStudent[ID={self.student_id}, Name={self.name}, "
                f"Age={self.age}, Percentage={self.percentage}, "
                f"Specialization={self.specialization}, "
                f"Marks of Internship={self.marks_of_internship}, "
                f"Rank={self.calculate_rank()}]")



class College:
   
    def __init__(self, num_students):
        self.num_students = num_students
        self.students = []  


    def add_student(self, student):
        if len(self.students) < self.num_students:
            self.students.append(student)
            print(f"✅ Student '{student.name}' added successfully.")
        else:
            print("❌ Cannot add more students. College capacity full!")

 
    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

   
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"🗑️ Student '{student.name}' removed successfully.")
                return
        print("❌ Student not found!")

   
    def __str__(self):
        result = f"College has {len(self.students)}/{self.num_students} students:\n"
        for student in self.students:
            result += str(student) + "\n"
        return result



if __name__ == "__main__":
    print("=== College Management System ===")

   
    college = College(3)

  
    e1 = EnggStudent(201, "Shubham", 22, 85, "Computer Science", 88)
    m1 = MedicalStudent(301, "Tushar", 23, 90, "Neurology", 95)

   
    college.add_student(e1)
    college.add_student(m1)

    print("\n=== College Data ===")
    print(college)

  
    s = college.get_student(201)
    if s:
        print("🔎 Found Student:", s)

    
    college.remove_student(301)

    print("\n=== After Removal ===")
    print(college)
