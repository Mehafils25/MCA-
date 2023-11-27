class Rectangle:
	def __init__(self, lenght, breadth):
		self.lenght = lenght
		self.breadth = breadth 
	def area(self):
		return self.lenght * self.breadth
	def perimeter(self):
		return 2 * (self.lenght + self.breadth)
	def compare_area(self,other_rectangle):
		if self.area () > other_rectangle.area():
			return "The first rectangle has a larger area."
		elif self.area() < other_rectangle.area():
			return "The second rectangle has a larger area."
		else:
			return "Both rectangle have the same area ."
rectangle1 = Rectangle (5,10)
rectangle2 = Rectangle(8,6)
print("Rectangle 1 Area:", rectangle1.area())
print("Rectangle 1 Perimeter:", rectangle1.perimeter())
print("Rectangle 2 Area:", rectangle2.area())
print("Rectangle 2 Perimeter", rectangle2.perimeter())
comparison_result = rectangle1.compare_area(rectangle2)
print("Compsrison Result:", comparison_result)
