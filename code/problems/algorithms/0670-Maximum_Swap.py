# -*- coding: utf-8 -*-
class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = str(num)
        numArr = [[int(numStr[i:i+1]), i] for i in range(len(numStr))]
        numArr1 = numArr.copy()

        numArr.sort(key=lambda v: (v[0], -1 * v[1]))
        numArr1.sort(key=lambda v: (v[0], v[1]))

        result = num
        for i in range(len(numStr)):
            e = numStr[i:i+1]
            if e == str(numArr[-1][0]):
                v=numArr.pop()
                numArr1.remove(v)
            else:
                a,b = min(i, numArr1[-1][1]), max(i, numArr1[-1][1])
                if a != b:
                    result = int(numStr[:a] + numStr[b:b+1] + numStr[a+1:b] + numStr[a:a+1] + numStr[b+1:])
                break
        # print(result)
        return  result


# param = 9973
param = 1993
r=Solution().maximumSwap(param)
print(r)
