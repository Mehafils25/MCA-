class Rectangle:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def area(self):
		return self.length * self.breadth
	def perimeter(self):
		return 2 * (self.length + self.breadth)
	def compare_area(self,a,b):
		if self.area() > a.area() & self.area() > b.area():
			return "The first rectangle has a larger area."
		elif a.area() > self.area() & a.area() > b.area():
			return "The second rectangle has a larger area."
		elif b.area() > self.area() & b.area() > a.area():
			return "The third rectangle has a larger area."
		else:
			return "all rectangles have the same area."
rectangle1=Rectangle(5, 6)
rectangle2=Rectangle(6, 6)
rectangle3=Rectangle(7, 6)
print("rectangle 1 area:",rectangle1.area())
print("rectangle 1 perimeter:",rectangle1.perimeter())
print("rectangle 2 area:",rectangle2.area())
print("rectangle 2 perimeter:",rectangle2.perimeter())
print("rectangle 3 area:",rectangle3.area())
print("rectangle 3 perimeter:",rectangle3.perimeter())
comparison_result = rectangle1.compare_area(rectangle2,rectangle3)
print("\nComparison Result: ", comparison_result)

