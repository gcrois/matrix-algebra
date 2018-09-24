#!/usr/bin/env python3
from copy import deepcopy


class Matrix:
    def __init__(self, array):
        self.row = len(array)
        self.col = len(array[0])
        self.arr = array
        self.hom = self.row == self.col
        m = self.arr
        self.trn = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        for i in array:
            if len(i) != self.col:
                raise TypeError("Length of rows do not match.")

    def __repr__(self):
        o = ""
        for i in range(0,len(self.arr)):
            o += str(self.arr[i])
            if i != self.row-1:
                o += "\n"
        return o

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.row != other.col:
                raise TypeError("Dimension mismatch")
            m = []
            for q in range(self.row):
                n = []
                for r in range(self.row):
                    t = 0
                    for c in range(self.col):
                        t += self.arr[q][c] * other.arr[c][r]
                    n += [t]
                m += [n]
            return Matrix(m)
        if isinstance(other, str):
            raise TypeError("Cannot multiply string")
        else:
            m = deepcopy(self.arr)
            for r in range(self.row):
                for c in range(self.col):
                    m[r][c] = m[r][c] * other
            return m


    def det(self):
        if not self.hom:
            raise TypeError("Must be a square matrix")
        def cross(m):
            return (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
        def split(m):
            q = 0
            if len(m) == 2:
                return cross(m)
            for column in range(0,len(m)):
                sign = (((column + 1) % 2) * 2) - 1 #makes every other term negative
                n = deepcopy(m)
                for k in n[1:]:
                    del k[column]
                q += (m[0][column] * split(n[1:]) * sign)
            return q
        return split(self.arr)

    def inv(self):
        if not self.hom:
            raise TypeError("Must be a square matrix")

        def cross(m):
            return (m[0][0]*m[1][1])-(m[0][1]*m[1][0])

        def minor(m):
            o = []
            q = deepcopy(m)
            for row in range(len(m)):
                k = []
                for column in range(len(m)):
                    n = deepcopy(m)
                    del n[row]
                    for i in range(len(n)):
                        del n[i][column]
                    k += [det(n)]
                o += [k]
            return o

        def cofactors(x):
            o = []
            for i in range(x):
                q = []
                k = i % 2
                for j in range(x):
                    q += [(((k + 1) % 2) * 2) - 1]
                    k += 1
                o += [q]
            return o

        def sign(m):
            s = cofactors(len(m[0]))
            for r in range(len(m)):
                for c in range(len(m)):
                    m[r][c] = m[r][c] * s[r][c]
            return m

        def adj(m):
            o = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
            return o

        def det(m):
            return Matrix(m).det()

        def mul(m, d):
            for r in range(len(m)):
                for c in range(len(m)):
                    m[r][c] = m[r][c] * d
            return m

        if len(self.arr[0]) == 2:
            m = deepcopy(self.arr)
            m[0][0], m[1][1] = m[1][1], m[0][0]
            return mul(sign(m),1/det(self.arr))

        return Matrix(mul(adj(sign(minor(self.arr))),1/det(self.arr)))






x = Matrix([[0,-1,2],[4,11,2]])
y = Matrix([[3,-1],[1,2],[6,1]])

#print(y.inv())
print(x * 3)
