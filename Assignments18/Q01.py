class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"Constructor called: {self}")

    def __del__(self):
        print(f"Destructor called for {self}")

    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


if __name__ == "__main__":
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, 2)

    print("\nAddition of two complex numbers:")
    c3 = c1 + c2
    print(f"{c1} + {c2} = {c3}")

    print("\nSubtraction of two complex numbers:")
    c4 = c1 - c2
    print(f"{c1} - {c2} = {c4}")
