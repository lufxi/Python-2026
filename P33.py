square_area = lambda a: a**2
rectangle_area = lambda l, b: l * b
triangle_area = lambda ba, h: 0.5 * ba * h

a =  int(input("Enter the length : "))
print("Area of the square : ",square_area(a))

l = int(input("Enter a length : "))
b = int(input("Enter a breadth : "))
print("Area of the rectangle : ",rectangle_area(l, b))

ba = int(input("Enter a base : "))
h = int(input("Enter a height : "))
print("Area of the triangle : ",triangle_area(ba, h))
