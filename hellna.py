from typing import Union

def process(value: str | int) -> None:
    print(f"Processing: {value}")

def describe(point):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y axis at {y}"
        case (x, 0):
            return f"On X axis at {x}"
        case (x, y):
            return f"At ({x}, {y})"

# Call the functions
process(42)
print(describe((0, 0)))
print(describe((3, 4)))