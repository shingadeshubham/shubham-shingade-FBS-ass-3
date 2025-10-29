
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



if __name__ == "__main__":
    
    s1 = Student(101, "Shubham", 21, 88.5)
    s1.display()
    print("Rank:", s1.calculate_rank())


    print("\nUsing __str__ method:")
    print(s1)
