from copy import deepcopy


class GildedRose:
    @staticmethod
    def update_quality(items):
       items[0].sell_in -= 1
       items[0].quality -= 1
