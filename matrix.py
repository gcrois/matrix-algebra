#!/usr/bin/env python3
from copy import deepcopy


class Matrix:
    def __init__(self, array):
        self.row = len(array)
        self.col = len(array[0])
        self.arr = array
        self.hom = self.row == self.col
        for i in array:
            if len(i) != self.row:
                raise TypeError("Length of rows do not match.")
    def __repr__(self):
        o = ""
        for i in range(0,len(self.arr)):
            o += str(self.arr[i])
            if i != self.row-1:
                o += "\n"
        return o
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
                print(n[0][column])
                for k in n[1:]:
                    del k[column]
                    print(k)
                q += (m[0][column] * split(n[1:]) * sign)
                print("DONE")
            return q
        return split(self.arr)
    def trn(self):
        m = self.arr
        m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
        self.__init__(m)

x = Matrix([[4,6],[3,8]])
y = Matrix([[1,4,2.2,3],[0,1,4,4],[-1,0,1,0],[2,0,4,1]])
print(x)
x.trn()
print(x)
