
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

   
    def accept(self):
        super().accept()  
        self.branch = input("Enter Branch: ")
        self.internal_marks = float(input("Enter Internal Marks: "))

    
    def display(self):
        super().display()  
        print(f"Branch: {self.branch}")
        print(f"Internal Marks: {self.internal_marks}")

    
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
                f"Age={self.age}, Percentage={self.percentage}, "
                f"Branch={self.branch}, Internal Marks={self.internal_marks}, "
                f"Rank={self.calculate_rank()}]")



if __name__ == "__main__":
    e1 = EnggStudent(201, "Shubham", 22, 85, "Computer Science", 88)
    e1.display()
    print("Rank:", e1.calculate_rank())

    print("\nUsing __str__ method:")
    print(e1)
