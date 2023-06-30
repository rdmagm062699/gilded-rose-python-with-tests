
INCREASING_QUALITY_ITEMS = ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]


class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            item.sell_in -= 1
            item.quality = _set_quality(item)


def _set_quality(item):
    if _increasing_quality_item(item):
        if item.sell_in <= 10:
            return item.quality + 2
        else:
            return item.quality + 1

    return item.quality - 1


def _increasing_quality_item(item):
    return item.name in INCREASING_QUALITY_ITEMS
