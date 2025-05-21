class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def set(self, key, value):
        index = self._hash(key)

        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def get(self, key):
        index = hash(key) % self.size

        for k, v in self.table[index]:
            if key == k:
                return v

df = HashTable(3)
df.set("casa", "carro")
df.set("agua", "fogo")
print(df.get("agua"))
print(df.get("casa"))
print(df.get("ca"))
