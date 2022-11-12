from enum import Enum

# 0. 定义一组工厂支持形式
class ShepeTypeEnum(Enum):
    Circle = 1
    Square = 2

# 1. 定义一个工厂基类,包含各种模板方法，供派生类进行复写
class Shape:
    def draw(self):
        print("没有描述类型")

# 2. 定义工厂类型
class Circle(Shape):
    def draw(self):
        print("画圆")
class Square(Shape):
    def draw(self):
        print("画方")

# 3. 定义工厂方法,即从这里是入口，获取实例
def getShapeClass(shape_type: ShepeTypeEnum) -> Shape:
    if shape_type == ShepeTypeEnum.Circle:
        return Circle()
    elif shape_type == ShepeTypeEnum.Square:
        return Square()
    else:
        return Shape()

if __name__ == '__main__':
    obj = getShapeClass(ShepeTypeEnum.Circle)
    obj.draw()