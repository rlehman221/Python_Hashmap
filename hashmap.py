from linked_list import LinkedList


class HashMap:

    # initialize hash map with set number of sections
    def __init__(self, num_sections = 6):
        self.store = self.initialize_mapping(num_sections)
        self.count = 0

    # initialize a list of linked lists
    # using number of sections for sizing
    def initialize_mapping(self, num_sections):
        new_store = []

        if num_sections < 6:
            num_sections = 6

        while len(new_store) < num_sections:
            new_store.append(LinkedList())

        return new_store

    # obtain the value for the given key
    # bracket method
    # return "None" if no instance of key
    def __getitem__(self, key):
        value = self.get_value(key)

        if value != None:
            return value

        return None

    # obtain the value for the given key
    # return "None" if no instance of key
    def get(self, key, default_value=None):
        value = self.get_value(key)

        if value is not None:
            return value

        return default_value

    # obtain the value for the given key
    # helper method for "get"
    def get_value(self, key):
        section = self.section(key)
        return section.get(key)

    # return number of buckets in hashmap
    def num_sections(self):
        return len(self.store)

    # use built in hash function and total sections to create index
    # return index of key
    def section(self, key):
        section_index = hash(key) % self.num_sections()
        return self.store[section_index]

    # bracket method that updates or adds value for given values
    # updates section counter depending on conditional statements
    def __setitem__(self, key, value):
        section = self.section(key)

        if section.isIncluded(key):
            section.update(key, value)
        else:
            section.append(key, value)
            self.count += 1

        if self.count > self.num_sections():
            self.resize()

        return value

    # develop new list of sections that is larger or smaller than current list
    # transfers key/value pairs from current list to new list
    # changes section size depending on bucket size
    def resize(self, grow=True):

        if grow:
            new_section = self.num_sections() * 2
        else:
            new_section = self.num_sections() / 2

        if new_section < 6:
            return

        old_store = self.store
        self.store = self.initialize_mapping(new_section)
        self.count = 0

        for section in old_store:
            item = section.head.next

            while item != section.tail:
                self[item.key] = item.value
                item = item.next

        return self

    # delete the instance for the given key
    def delete(self, key):
        value = self.section(key).remove(key)

        if value != None:
            self.count -= 1
            if self.count < self.num_sections() / 3:
                self.resize(False)

        return value

    # returns true or false if hashmap has related key
    def has_key(self, key):
        section = self.section(key)
        return section.isIncluded(key)

    # add a new instance of hashmap to current hashmap
    def update(self, other_hash_map):
        for key, value in other_hash_map.elements():

            self[key] = value

        return self

    # return length of hashmap
    def __len__(self):
        return self.count

    # determine if the hashmap is empty
    def is_empty(self):
        return self.count == 0

    # return all key and value pairs as a list
    def elements(self):
        return self.get_fragmentSet("elements")

    # return all keys as a list
    def keys(self):
        return self.get_fragmentSet()

    # return all values as a list
    def values(self):
        return self.get_fragmentSet("values")

    # loop through each linked list in hash map
    # helper function to get elements
    def get_fragmentSet(self, subset="keys"):
        contents = []

        for section in self.store:
            if subset == "elements":
                contents += section.elements()
            elif subset == "values":
                contents += section.values()

            else:
                contents += section.keys()


        return contents

    # print out hash map
    def __str__(self):
        elements = []

        for pair in self.elements():
            element_pair = ": ".join(self.format_pair(pair))
            elements.append(element_pair)

        return "{" + ", ".join(elements) + "}"

    # use quotes to return string
    def element_string(self, string):
        return "'%s'" % string

    # use print statement formatting for each element
    def format_pair(self, pair):
        element_pair = ()

        for element in pair:
            if isinstance(element, str):
                element_pair += (self.element_string(element),)
            else:
                element_pair += (str(element),)

        return element_pair
