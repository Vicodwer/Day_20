# ============================================================
# PART B — Stretch Problem: Vector Class
# ============================================================
 
print("\n" + "=" * 60)
print("PART B — Vector Class with Dunder Methods")
print("=" * 60)
 
class Vector:
    """
    A mathematical vector backed by a tuple of numbers.
 
    Supports:
      __add__  → element-wise addition
      __sub__  → element-wise subtraction
      __mul__  → scalar multiplication  (Vector * scalar)
      __repr__ → readable string output
    """
 
    def __init__(self, components):
        """
        Parameters
        ----------
        components : tuple
            Numeric values representing each dimension of the vector.
        """
        if not isinstance(components, tuple):
            raise TypeError("components must be a tuple")
        self.components = components
 
    def __repr__(self):
        return f"Vector{self.components}"
 
    def __add__(self, other):
        """Element-wise addition; both vectors must have the same length."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of dimensions")
        result = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(result)
 
    def __sub__(self, other):
        """Element-wise subtraction; both vectors must have the same length."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of dimensions")
        result = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(result)
 
    def __mul__(self, scalar):
        """Scalar multiplication: Vector * number."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        result = tuple(a * scalar for a in self.components)
        return Vector(result)
 
    # Support right-side multiplication: number * Vector
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
 
 
# --- Test Vector ---
v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))
v3 = Vector((0, -1, 2))
 
print(f"\nv1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")
 
print(f"\nv1 + v2           = {v1 + v2}")
print(f"v1 - v2           = {v1 - v2}")
print(f"v2 - v3           = {v2 - v3}")
print(f"v1 * 3            = {v1 * 3}")
print(f"2 * v2            = {2 * v2}")
print(f"v1 + v2 + v3      = {v1 + v2 + v3}")
print(f"(v1 + v2) * 0.5   = {(v1 + v2) * 0.5}")
