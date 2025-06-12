# SEM FLYWEIGHT
# from memory_profiler import profile
#
# class Circle:
#     def __init__(self, color, radius):
#         self.color = color
#         self.radius = radius
#
#     def draw(self):
#         print(f"Drawing a {self.color} circle with radius {self.radius}")
#
# @profile
# def create_shapes():
#     shapes = []
#     colors = ['red', 'blue', 'green', 'yellow', 'black']
#     for i in range(100000):
#         color = colors[i % len(colors)]
#         radius = (i % 10) + 1
#         shapes.append(Circle(color, radius))
#     return shapes
#
# if __name__ == "__main__":
#     shapes = create_shapes()
#     for shape in shapes[:10]:
#         shape.draw()

# COM FLYWEIGHT
from memory_profiler import profile

class Color:
    def __init__(self, name):
        self.color = name

class ColorFactory:
    _colors = {}

    @staticmethod
    def get_color(color_name):
        if color_name not in ColorFactory._colors:
            ColorFactory._colors[color_name] = Color(color_name)
        return ColorFactory._colors[color_name]

class Circle:
    def __init__(self, color_name, radius):
        self.color = ColorFactory.get_color(color_name)
        self.radius = radius

    def draw(self):
        print(f"Drawing a {self.color.color} circle with radius {self.radius}")

@profile
def create_shapes():
    shapes = []
    colors = ['red', 'blue', 'green', 'yellow', 'black']
    for i in range(100000):
        color = colors[i % len(colors)]
        radius = (i % 10) + 1
        shapes.append(Circle(color, radius))
    return shapes

if __name__ == "__main__":
    shapes = create_shapes()
    for shape in shapes[:10]:
        shape.draw()
