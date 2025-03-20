# . Create a Python package named shapes with a submodule circle.py 
# that contains a function area(radius) to calculate the area of a circle. 
# Then, import the function in another file and use it. 


from shapes.circle import area
radius=5
circle_area = area(radius)
print(f"The area of the circle with radius {radius} is: {circle_area}")

