from enum import Enum

# 0. 定义一组工厂支持形式
class ShepeTypeEnum(Enum):
    Circle = 1
    Square = 2
class ColorEnum(Enum):
    Red = 1
    yellow = 2

# 1. 定义一个工厂基类,包含各种模板方法，供派生类进行复写
class Shape:
    def draw(self):
        print("没有描述类型")
class Color:
    def fill(self):
        print("没有描述颜色")

# 2. 定义工厂类型
class Circle(Shape):
    def draw(self):
        print("画圆")
class Square(Shape):
    def draw(self):
        print("画方")
class RedColor(Color):
    def fill(self):
        print("填充红色")
class YellowColor(Color):
    def fill(self):
        print("填充黄色")
# 3. 定义抽象实例
class pinter:
    def __init__(self):
        self.shape: Shape = None
        self.color: Color = None
    def run(self):
        if self.shape is not None and self.color is not None:
            self.shape.draw()
            self.color.fill()
        else:
            print('未设置完全')

# 3. 定义实例获取方法
def getShapeClass(shape_type: ShepeTypeEnum, color_type: ColorEnum) -> pinter:
    ret = pinter()
    if shape_type == ShepeTypeEnum.Circle:
        ret.shape = Circle()
    elif shape_type == ShepeTypeEnum.Square:
        ret.shape = Square()
    else:
        ret.shape = Shape()
    if color_type == ColorEnum.Red:
        ret.color = RedColor()
    elif color_type == ColorEnum.yellow:
        ret.color = YellowColor()
    else:
        ret.color = Color()
    return ret

if __name__ == '__main__':
    obj = getShapeClass(ShepeTypeEnum.Circle, ColorEnum.Red)
    obj.run()