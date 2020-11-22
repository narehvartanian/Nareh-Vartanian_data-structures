class Entry():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap():
    def __init__(self):
        self._capacity = 26
        self._hashtable = [None] * self._capacity * 10
        self._size = 0

    def _hash(self, element):
        # return hash(element) % self._capacity
        return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        # print(index)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
            else:
                self._hashtable[i] = Entry(key, value)
                self._size += 1
                return None
        # TODO resize and add the key,value pair

    def get(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    return self._hashtable[i].value
            else:
                return None

    def hasKey(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    print(f'You have {key} in you address book')
                    return True
            else:
                print(f'You don\'t have {key} in you address book')
                return False

    def remove(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    print(f'Successfully removed {self._hashtable[i].value} from address book')
                    self._hashtable[i] = None
                    break
            else:
                print ("Address entry was not found")
                return None

    def size(self):
        return self._size

    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while (e != None):
                print(e.data)
                e = e.next

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i
                break

        return self._hashtable[tmpInd].value


addressBook = HashMap()
addressBook.put("Armen", {"fullName": "Armen Hakobyan",
                          "phoneNumber": "094444444"})
addressBook.put("Artak", {"fullName": "Artak Zakaryan",
                          "phoneNumber": "094444441"})
addressBook.put("Ani", {"fullName": "Ani Aslanyan",
                        "phoneNumber": "094444442"})
addressBook.put("Karen", {"fullName": "Karen Kocharyan",
                          "phoneNumber": "094444445"})
addressBook.put("Zaven", {"fullName": "Zaven Hakobyan",
                          "phoneNumber": "094444447"})
addressBook.put("Gohar", {"fullName": "Gohar Vardanyan",
                          "phoneNumber": "094444454"})

print("----------------------------")
print("Initializing Address Book...")
print("----------------------------")
for elem in addressBook:
    print(elem.get("fullName"))

print()
print("----------------------------")
print("Testing remove function")
print("----------------------------")
addressBook.remove("Ani")
addressBook.remove("Zaven")
print()
print("----------------------------")
print("Address Book after element removal")
print("----------------------------")
for elem in addressBook:
    print(elem.get("fullName"))

print()
print("----------------------------")
print("Key Checking")
print("----------------------------")
addressBook.hasKey("Karen")
addressBook.hasKey("Lola")
