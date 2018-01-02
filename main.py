from hashmap import HashMap

# Utilizing hashmap class
hash_map = HashMap()

print("Initializing empty hashmap " + str(hash_map))

hash_map["FirstKey"] = 23
hash_map["SecondKey"] = 53
print("Adding two values to hashmap " + str(hash_map))

hash_map["FirstKey"] = 13
print("Updating first value in hashmap " + str(hash_map))

hash_map.delete("FirstKey")
print("Deleting value in hashmap " + str(hash_map))

hash_map_two = HashMap()
hash_map_two["FirstKey"] = 203
print("Initializing second hashmap " + str(hash_map_two))

hash_map.update(hash_map_two)
print("Updating first hashmap with second hashmap " + str(hash_map))

print("All keys in hashamp " + str(hash_map.keys()))
print("All values in hashmap " + str(hash_map.values()))

print("The amount of buckets in hashmap " + str(hash_map.num_sections()))

