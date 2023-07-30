
from slotted_struct import SlottedStruct


class Point2D(metaclass=SlottedStruct):
    dim = 2

class Point3D(metaclass=SlottedStruct):
    dim = 3

# Example usage:
p1 = Point2D(1, 2)
p2 = Point2D(1, 2)
p3 = Point2D(3, 4)

print(p1 == p2)  # Output: True
print(p1 == p3)  # Output: False

print(hash(p1))  # Output: Some hash value
print(hash(p2))  # Output: Same hash value as p1
print(hash(p3))  # Output: Different hash value

print(p1)        # Output: Point2D(1, 2)

