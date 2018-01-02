import unittest
from hashmap import HashMap

# test hashmap class
class HashMapTests(unittest.TestCase):
    def setUp(self):
        self.hashmap = HashMap()

    def tearDown(self):
        self.hashmap = None

    # test if empty hashmap is empty
    def test_initialize_hashmap(self):
        self.assertTrue(self.hashmap.is_empty())
        self.assertEqual(len(self.hashmap), 0)

    # test adding key into hashmap and getter method
    def test_insert_into_hashmap(self):
        self.assertFalse(self.hashmap.has_key("randomValue"))
        self.hashmap["FirstKey"] = "FirstValue"
        self.assertTrue(self.hashmap.has_key("FirstKey"))
        self.assertEqual(len(self.hashmap), 1)

    # test updating key in hashmap
    def test_update_in_hashmap(self):
        self.hashmap["FirstKey"] = "FirstValue"
        self.hashmap["SecondKey"] = "SecondValue"
        self.assertEqual("FirstValue", self.hashmap["FirstKey"])

    # test deleting key in hashmap
    def test_delete_in_hashmap(self):
        self.hashmap["FirstKey"] = "FirstValue"
        self.hashmap.delete("FirstKey")
        self.assertFalse(self.hashmap.has_key("FirstKey"))
        self.assertIsNone(self.hashmap.get("FirstKey"))

    # test sections grow with an increase in # of key/values
    def test_hashmap_resize(self):
        self.assertEqual(6, self.hashmap.num_sections())

        i = 1
        while i <= 7:
            self.hashmap[i] = i
            i += 1

        self.assertEqual(12, self.hashmap.num_sections())

    # test for other hashmap to update old hashmap
    def test_hash_map_updates_with_other_hashmap(self):

        self.hashmap["FirstKey"] = "FirstValue"
        other_hashmap = HashMap()
        other_hashmap["FirstKey"] = "OtherFirstValue"
        other_hashmap["SeondKey"] = "SecondValue"
        self.hashmap.update(other_hashmap)
        self.assertEqual("OtherFirstValue", self.hashmap["FirstKey"])

if __name__ == '__main__':
    unittest.main()