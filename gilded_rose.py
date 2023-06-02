class GildedRose:
    @staticmethod
    def update_quality(items):
        update_quality(items)


def aged_brie(item):
    return item.name == "Aged Brie"


def backstage_passes(item):
    return item.name == "Backstage passes to a TAFKAL80ETC concert"


def sulfuras_hand_of_ragnaros(item):
    return item.name == "Sulfuras, Hand of Ragnaros"


def update_quality(items):
    for item in items:
        if not aged_brie(item) and not backstage_passes(item):
            # TODO: Improve this code.  Word.
            if item.quality > 0:
                if not sulfuras_hand_of_ragnaros(item):
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if aged_brie(item):
                    if item.sell_in < 6:
                        item.quality = item.quality + 1
                # Increases the Quality of the stinky cheese if it's 11 days to due date.
                if aged_brie(item):
                    if item.sell_in < 11:
                        item.quality = item.quality + 1
                if backstage_passes(item):
                    if item.sell_in < 11:
                        # See revision number 2394 on SVN.
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if not sulfuras_hand_of_ragnaros(item):
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if not aged_brie(item):
                if not backstage_passes(item):
                    if item.quality > 0:
                        if not sulfuras_hand_of_ragnaros(item):
                            item.quality = item.quality - 1
                else:
                    # TODO: Fix this.
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                if aged_brie(item) and item.sell_in <= 0:
                    item.quality = 0
                    # of for.
        if not sulfuras_hand_of_ragnaros(item):
            if item.quality > 50:
                item.quality = 50
    return items
