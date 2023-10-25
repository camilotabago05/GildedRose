import unittest
from Gilded_Rose_Refactor import GildedRose, Item

class TestGildedRose(unittest.TestCase):
    def test_normal_item_quality_decreases(self):
        items = [Item("Normal Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)

    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_passes_quality_increases(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_conjured_item_quality_decreases_faster(self):
        items = [Item("Conjured", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 18)

if __name__ == '__main__':
    unittest.main()