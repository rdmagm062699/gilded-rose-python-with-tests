from item import Item


class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            item.quality = update_quality(item)
            item.sell_in = update_sell_in(item)
        return items


def update_quality(item: Item) -> int:
    return item.quality - 1


def update_sell_in(item: Item) -> int:
    return item.sell_in - 1
