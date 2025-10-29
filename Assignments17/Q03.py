
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



class MedicalStudent(Student):
   
    def __init__(self, student_id, name, age, percentage, specialization, marks_of_internship):
       
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.marks_of_internship = marks_of_internship

   
    def accept(self):
        super().accept() 
        self.specialization = input("Enter Specialization: ")
        self.marks_of_internship = float(input("Enter Marks of Internship: "))

 
    def display(self):
        super().display()  
        print(f"Specialization: {self.specialization}")
        print(f"Marks of Internship: {self.marks_of_internship}")

   
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



if __name__ == "__main__":
    print("=== Creating Medical Student Object ===")
    m1 = MedicalStudent(301, "Shubham", 23, 88, "Cardiology", 92)

    print("\n=== Using display() method ===")
    m1.display()

    print("\n=== Using calculate_rank() method ===")
    print("Rank:", m1.calculate_rank())

    print("\n=== Using __str__() method ===")
    print(m1.__str__())  # Explicit call (mandatory for assignment)
