class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self._normalize()
        print(f"Constructor called: {self}")

    def __del__(self):
        print(f"Destructor called for {self}")

    
    def _normalize(self):
        if self.cm >= 100:
            self.m += self.cm // 100
            self.cm = self.cm % 100
        if self.m >= 1000:
            self.km += self.m // 1000
            self.m = self.m % 1000

    
    def __add__(self, other):
        new_km = self.km + other.km
        new_m = self.m + other.m
        new_cm = self.cm + other.cm
        result = Distance(new_km, new_m, new_cm)
        result._normalize()
        return result

    
    def __sub__(self, other):
        # Convert all to cm for easy subtraction
        total_cm_self = (self.km * 100000) + (self.m * 100) + self.cm
        total_cm_other = (other.km * 100000) + (other.m * 100) + other.cm
        total_cm_result = abs(total_cm_self - total_cm_other)  # absolute difference

        # Convert back to km, m, cm
        km = total_cm_result // 100000
        total_cm_result %= 100000
        m = total_cm_result // 100
        cm = total_cm_result % 100
        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"


# Example usage
if __name__ == "__main__":
    d1 = Distance(2, 750, 80)
    d2 = Distance(1, 500, 50)

    print("\nAddition of two distances:")
    d3 = d1 + d2
    print(f"{d1} + {d2} = {d3}")

    print("\nSubtraction of two distances:")
    d4 = d1 - d2
    print(f"{d1} - {d2} = {d4}")
