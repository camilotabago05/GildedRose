class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Sulfuras, Hand of Ragnaros":
                self.update_sell_in(item)
                self.update_quality_for_item(item)

    def update_sell_in(self, item):
        item.sell_in -= 1

    def update_quality_for_item(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes(item)
        elif item.name == "Conjured":
            self.update_conjured(item)
        else:
            self.update_normal_item(item)

    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11:
                self.increase_quality(item, 1)
            if item.sell_in < 6:
                self.increase_quality(item, 1)
        if item.sell_in < 0:
            item.quality = 0

    def update_conjured(self, item):
        self.decrease_quality(item, 2)

    def update_normal_item(self, item):
        self.decrease_quality(item, 1)

    def decrease_quality(self, item, amount):
        if item.quality > 0:
            item.quality -= amount

    def increase_quality(self, item, amount):
        if item.quality + amount <= 50:
            item.quality += amount

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)