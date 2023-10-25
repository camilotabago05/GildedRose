import unittest
from Gilded_Rose_Original import GildedRose, Item

class TestGildedRose(unittest.TestCase):

    def test_normal_item_quality_degradation(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_sell_in_degradation(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 9)

    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_quality_never_negative(self):
        items = [Item("Normal Item", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_sulfuras_quality_and_sell_in_never_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 10)

    def test_backstage_passes_quality_increases_correctly(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)

if __name__ == '__main__':
    unittest.main()

