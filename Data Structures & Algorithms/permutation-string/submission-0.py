class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sortedS1 = sorted(s1)
        s1Len = len(s1)
        for i in range(len(s2)):
            print(i)
            tmp = s2[i: i + s1Len]
            print(tmp)
            sortedTmp = sorted(tmp)
            if sortedTmp == sortedS1:
                return True

        return False

                    