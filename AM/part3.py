# ============================================================
# PART C — Interview Ready
# ============================================================
 
print("\n" + "=" * 60)
print("PART C — Interview Ready")
print("=" * 60)
 
# ----------------------------------------------------------
# C2 — Student Class
# ----------------------------------------------------------
print("\n--- C2: Student Class ---")
 
class Student:
    """
    Represents a student with a name and marks.
 
    Methods
    -------
    calculate_grade() → str
        Returns 'A', 'B', or 'C' based on marks.
    __str__()
        Returns a formatted string with student details.
    """
 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
 
    def calculate_grade(self):
        """
        Grade scale:
          A  → marks >= 80
          B  → marks >= 60
          C  → marks  < 60
        """
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"
 
    def __str__(self):
        return (
            f"Student : {self.name}\n"
            f"Marks   : {self.marks}\n"
            f"Grade   : {self.calculate_grade()}"
        )
 
 
# Test Student
students = [
    Student("Alice", 92),
    Student("Bob", 74),
    Student("Charlie", 55),
    Student("Diana", 80),
]
 
for s in students:
    print(f"\n{s}")
    print("-" * 20)
 
 
print("\n✅  All parts executed successfully.")
