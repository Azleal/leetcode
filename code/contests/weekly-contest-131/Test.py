# -*- coding: utf-8 -*-
#1 5 11
m=[float('inf')] * 20
m[0]=0

w = 15
costW = 0
for i in range(0,20):

    if i + 11 < 20:
        m[i + 11] = min(m[i + 11], m[i] + 1)
    if i + 5 < 20 :
        m[i + 5] = min(m[i + 5], m[i] + 1)
    if i + 1 < 20 :
        m[i + 1] = min(m[i + 1], m[i] + 1)

    if w == i:
        costW = m[i]
        # break
print(costW)


