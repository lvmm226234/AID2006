"""
    迭代图形管理器
    要求:以最快的速度完成
"""
class GraphicController:
    def __init__(self):
        self.__list_graphics = []

    def add_graphic(self, graphic):
        self.__list_graphics.append(graphic)


controller = GraphicController()
GraphicController.add_graphic("圆形")
GraphicController.add_graphic("矩形")
GraphicController.add_graphic("三角")
for item in controller:
    print(item)
