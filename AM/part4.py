D1 — Prompt Given to AI
Prompt: "Explain Python dunder methods with examples for beginners and include a custom class implementation."

D2 — AI Output (Documented)
The AI provided the following explanation and class implementation (summarised below):

AI Explanation of Dunder Methods
Dunder methods (double-underscore methods) are special built-in methods in Python that allow customisation of object behaviour. They are automatically invoked by Python in response to specific syntax or built-in function calls.

AI-Provided Example Class
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f'{self.title} ({self.pages} pages)'

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __add__(self, other):
        # Combine two books into an anthology
        combined_pages = self.pages + other.pages
        return Book(f'{self.title} & {other.title}', combined_pages)

    def __len__(self):
        return self.pages

b1 = Book('Python Basics', 300)
b2 = Book('Advanced Python', 450)
print(b1)           # Python Basics (300 pages)
print(repr(b1))     # Book('Python Basics', 300)
combined = b1 + b2
print(combined)     # Python Basics & Advanced Python (750 pages)
print(len(b1))      # 300

D3 — Evaluation of AI Output

Criterion	Result	Notes
Are the examples correct?	Yes	All dunder method examples produce the expected output when tested in Python 3.
Is the class implementation working?	Yes	The Book class compiles and runs without errors. All four dunders behave correctly.
Are explanations beginner-friendly?	Yes	Concepts are explained in plain language with concrete analogies.
Any use of restricted built-ins?	No	The AI correctly avoided sum(), max(), etc. in the loop-only sections.
Suggested improvement	Minor	__eq__ and __lt__ could be added to make Book objects sortable — not shown by the AI.
