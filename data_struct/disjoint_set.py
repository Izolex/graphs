class DisjointSet:
    forest = []
    rank = []

    def append(self, value):
        self.forest.append(value)
        self.rank.append(0)

    def find(self, i):
        if self.forest[i] == i:
            return i
        return self.find(self.forest[i])

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)

        if self.rank[x_set] < self.rank[y_set]:
            self.forest[x_set] = y_set
        elif self.rank[x_set] > self.rank[y_set]:
            self.forest[y_set] = x_set
        else:
            self.forest[y_set] = x_set
            self.rank[x_set] += 1
