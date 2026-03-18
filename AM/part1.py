# ============================================================
# PART A — Concept Application
# ============================================================
 
print("=" * 60)
print("PART A — Concept Application")
print("=" * 60)
 
# ----------------------------------------------------------
# A1 — Max / Min using loops only
# ----------------------------------------------------------
print("\n--- A1: Max and Min using Loops ---")
 
def find_max_min(lst):
    """Return (max, min) of a list using only loops."""
    max_val = lst[0]
    min_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
        if item < min_val:
            min_val = item
    return max_val, min_val
 
numbers = [42, 7, 19, 3, 88, 55, 23, 1]
maximum, minimum = find_max_min(numbers)
print(f"List   : {numbers}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
 
 
# ----------------------------------------------------------
# A1 — Frequency count using a dictionary
# ----------------------------------------------------------
print("\n--- A1: Frequency Count using Dictionary ---")
 
def count_frequency(lst):
    """Count frequency of each element using a dict and loops."""
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
 
sample = [1, 2, 3, 2, 1, 4, 3, 2, 5, 1]
print(f"List     : {sample}")
print(f"Frequency: {count_frequency(sample)}")
 
 
# ----------------------------------------------------------
# A2 — Reverse a number using while loop
# ----------------------------------------------------------
print("\n--- A2: Reverse a Number (while loop) ---")
 
def reverse_number(n):
    """Reverse the digits of an integer using a while loop."""
    reversed_num = 0
    n = abs(n)                   # handle negatives gracefully
    while n > 0:
        digit = n % 10           # extract last digit
        reversed_num = reversed_num * 10 + digit
        n //= 10                 # drop last digit
    return reversed_num
 
for num in [123, 4567, 100, 9]:
    print(f"  reverse({num}) → {reverse_number(num)}")
 
 
# ----------------------------------------------------------
# A2 — Palindrome check using while loop
# ----------------------------------------------------------
print("\n--- A2: Palindrome Check (while loop) ---")
 
def is_palindrome(n):
    """Return True if n is a palindrome number."""
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num
 
for num in [121, 123, 1331, 12321, 10]:
    print(f"  {num} → palindrome: {is_palindrome(num)}")
 
 
# ----------------------------------------------------------
# A3 — Convert list of tuples to dictionary (no built-ins)
# ----------------------------------------------------------
print("\n--- A3: List of Tuples → Dictionary ---")
 
def tuples_to_dict(tuple_list):
    """Convert [(key, value), ...] to a dict without dict()."""
    result = {}
    for pair in tuple_list:
        result[pair[0]] = pair[1]
    return result
 
pairs = [("name", "Alice"), ("age", 21), ("city", "Mumbai"), ("grade", "A")]
converted = tuples_to_dict(pairs)
print(f"Tuples : {pairs}")
print(f"Dict   : {converted}")
 
 
# ----------------------------------------------------------
# A3 — Find key with highest value using loops only
# ----------------------------------------------------------
print("\n--- A3: Key with Highest Value (loops only) ---")
 
def key_with_max_value(d):
    """Return the key whose value is the highest, using only loops."""
    max_key = None
    max_val = None
    for key in d:
        if max_val is None or d[key] > max_val:
            max_val = d[key]
            max_key = key
    return max_key, max_val
 
scores = {"Alice": 88, "Bob": 95, "Charlie": 72, "Diana": 91}
best_key, best_val = key_with_max_value(scores)
print(f"Dict   : {scores}")
print(f"Highest: '{best_key}' with value {best_val}")
 
 
# ----------------------------------------------------------
# A4 — *args: sum and average (no sum())
# ----------------------------------------------------------
print("\n--- A4: *args — Sum and Average ---")
 
def sum_and_average(*args):
    """Accept multiple numbers; return (total, average) without sum()."""
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1
    if count == 0:
        return 0, 0
    average = total / count
    return total, average
 
total, avg = sum_and_average(10, 20, 30, 40, 50)
print(f"Numbers : 10, 20, 30, 40, 50")
print(f"Sum     : {total}")
print(f"Average : {avg}")
 
total2, avg2 = sum_and_average(5, 15, 25)
print(f"\nNumbers : 5, 15, 25")
print(f"Sum     : {total2}")
print(f"Average : {avg2:.2f}")
 
 
# ----------------------------------------------------------
# A5 — **kwargs: student with highest marks
# ----------------------------------------------------------
print("\n--- A5: **kwargs — Student with Highest Marks ---")
 
def top_student(**kwargs):
    """
    Accept student_name=marks pairs via **kwargs.
    Return the name and score of the highest-scoring student.
    """
    best_name = None
    best_marks = None
    for student, marks in kwargs.items():
        if best_marks is None or marks > best_marks:
            best_marks = marks
            best_name = student
    return best_name, best_marks
 
name, marks = top_student(Alice=88, Bob=95, Charlie=72, Diana=91, Eve=95)
print(f"Students: Alice=88, Bob=95, Charlie=72, Diana=91, Eve=95")
print(f"Top student: {name} with {marks} marks")
 
