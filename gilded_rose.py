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


def calculate_sell_in(item):
    if sulfuras_hand_of_ragnaros(item):
        return item.sell_in
    return item.sell_in - 1


def calculate_quality(item):
    quality = item.quality
    sell_in = item.sell_in
    if not aged_brie(item) and not backstage_passes(item):
        # TODO: Improve this code.  Word.
        if quality > 0:
            if not sulfuras_hand_of_ragnaros(item):
                quality = quality - 1
    else:
        if quality < 50:
            quality = quality + 1
            if aged_brie(item):
                if sell_in < 6:
                    quality = quality + 1
            # Increases the Quality of the stinky cheese if it's 11 days to due date.
            if aged_brie(item):
                if sell_in < 11:
                    quality = quality + 1
            if backstage_passes(item):
                if sell_in < 11:
                    # See revision number 2394 on SVN.
                    if quality < 50:
                        quality = quality + 1
                # Increases the Quality of Backstage Passes if the Quality is 6 or less.
                if sell_in < 6:
                    if quality < 50:
                        quality = quality + 1
    sell_in = calculate_sell_in(item)
    if sell_in < 0:
        if not aged_brie(item):
            if not backstage_passes(item):
                if quality > 0:
                    if not sulfuras_hand_of_ragnaros(item):
                        quality = quality - 1
            else:
                # TODO: Fix this.
                quality = quality - quality
        else:
            if quality < 50:
                quality = quality + 1
            if aged_brie(item) and sell_in <= 0:
                quality = 0
                # of for.
    if not sulfuras_hand_of_ragnaros(item):
        if quality > 50:
            quality = 50

    return quality


def update_quality(items):
    for item in items:
        item.quality = calculate_quality(item)
        item.sell_in = calculate_sell_in(item)
    return items
