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


def legendary_item(item: Item) -> bool:
    return item.name == "Sulfuras, Hand of Ragnaros"


def conjured_item(item: Item) -> bool:
    return item.name == "Conjured Mana Cake"


def calculate_appreciation(item: Item) -> int:
    if item.sell_in <= 0:
        # After sell by date passes, quality drops to 0.
        return -1 * item.quality
    if item.sell_in <= 5:
        return 3
    if item.sell_in <= 10:
        return 2
    return 1


def calculate_depreciation(item: Item) -> int:
    if item.sell_in < 0:
        return 2
    return 1


def clamp(amount: int, limit: int) -> int:
    return min(amount, limit)


def update_quality(item: Item) -> int:
    if conjured_item(item):
        return item.quality - (calculate_depreciation(item) * 2)
    if legendary_item(item):
        return item.quality
    if appreciating_item(item):
        return clamp(item.quality + calculate_appreciation(item), 50)
    return item.quality - calculate_depreciation(item)


def update_sell_in(item: Item) -> int:
    if legendary_item(item):
        return item.sell_in
    return item.sell_in - 1
