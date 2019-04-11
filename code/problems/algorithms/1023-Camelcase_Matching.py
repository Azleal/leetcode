# -*- coding: utf-8 -*-


class Solution:
    def camelMatch(self, queries, pattern: str) :
        results = []
        for i in queries:
            results.append(self.solve(i, pattern))
        print(results)
        return results

    def solve(self,str, pattern) -> bool:
        strArray=list(str)
        matchedPattern=""
        matchedPatternCurrsor = 0;
        for index in range(len(strArray)):
            e = strArray[index]
            if e == pattern[matchedPatternCurrsor:matchedPatternCurrsor+1]:
                matchedPattern += e
                matchedPatternCurrsor += 1

                if matchedPattern == pattern:
                    return str[index+1:].lower() == str[index+1:]

            elif e.isupper():
                return False
        return False

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"
Solution().camelMatch(queries, pattern)


