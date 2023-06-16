from item import Item


class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            item.sell_in = update_sell_in(item)
            item.quality = update_quality(item)
        return items


def appreciating_item(item: Item) -> bool:
    return (
        item.name == "Aged Brie"
        or item.name == "Backstage passes to a TAFKAL80ETC concert"
    )


def calculate_appreciation(item: Item) -> int:
    if item.sell_in <= 5:
        return 3
    if item.sell_in <= 10:
        return 2
    return 1


def calculate_depreciation(item: Item) -> int:
    if item.sell_in < 0:
        return 2
    return 1


def update_quality(item: Item) -> int:
    if appreciating_item(item):
        return item.quality + calculate_appreciation(item)
    return item.quality - calculate_depreciation(item)


def update_sell_in(item: Item) -> int:
    return item.sell_in - 1
