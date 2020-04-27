'''
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

    每组都有 X 张牌。
    组内所有的牌上都写着相同的整数。

仅当你可选的 X >= 2 时返回 true。

'''
from collections import Counter #得出列表中相同数字的个数，返回一个字典
from math import gcd   #gad（a,b）求两个数的最大公约数

class Solution:
    def hasGroupsSizeX(self, deck):
        a = Counter(deck)
        print(a)
        b = list(a.values())
        c = min(b)
        for i in b:
            c = gcd(c,i)
            if c>1:
                continue
            else:
                return False
        return True

s = Solution()
deck = [1,1,2,2,3,3,3,3]
ss = s.hasGroupsSizeX(deck)
print(ss)



