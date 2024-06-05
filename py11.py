from sympy import symbols, Eq, solve

def circle_intersection(x1, y1, r1, x2, y2, r2, x3, y3, r3):
    # Variables for circle centers and radii
    x, y = symbols('x y')
    
    # Equations for the three circles
    eq1 = Eq((x - x1)*2 + (y - y1)2, r1*2)
    eq2 = Eq((x - x2)*2 + (y - y2)2, r2*2)
    eq3 = Eq((x - x3)*2 + (y - y3)2, r3*2)
    
    # Solving the system of equations
    intersection_points = solve((eq1, eq2, eq3), (x, y))
    
    return intersection_points

# Example usage
x1, y1, r1 = 0, 0, 1
x2, y2, r2 = 2, 0, 1
x3, y3, r3 = 1, 2, 1

result = circle_intersection(x1, y1, r1, x2, y2, r2, x3, y3, r3)
print("Intersection Points:", result)