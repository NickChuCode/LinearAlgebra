class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    @classmethod
    def zero(cls, dim):
        """返回一个dim维的零向量"""
        return cls([0] * dim)

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __add__(self, other):
        """向量加法，返回结果向量"""
        assert len(self) == len(other), \
            "Error in adding , the length of vectors must be the same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        """向量减法，返回结果向量"""
        assert len(self) == len(other), \
            "Error in substracting , the length of vectors must be the same."
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        """返回数量乘法的结果向量：self * k"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回数量乘法的结果向量：k * self"""
        return self * k

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self