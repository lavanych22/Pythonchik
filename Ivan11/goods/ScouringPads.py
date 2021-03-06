from goods.Good import *
from enums.GoodsType import *
from enums.GoodsColour import *


class ScouringPads(Good):
    goods_type = GoodsType.SCOURING_PADS
    goods_colour = GoodsColour.BLACK

    def __init__(self, name, price, amount, smell, volume):
        self.name = name
        self.price = price
        self.amount = amount
        self.smell = smell
        self.volume = volume

    def __str__(self):
        return "Good type: " + str(self.goods_type.name) + " Price: " + str(self.price) + " Smell: " + self.smell\
               + " Volume: " + str(self.volume)
