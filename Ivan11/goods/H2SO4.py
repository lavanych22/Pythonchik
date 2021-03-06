from goods.Good import *
from enums.GoodsType import *
from enums.GoodsColour import *


class H2SO4(Good):
    goods_type = GoodsType.CLEANERS
    goods_colour = GoodsColour.BLUE

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return "Good type: " + str(self.goods_type.name) + " Price: " + str(self.price) + " Amount: " + str(self.amount)
