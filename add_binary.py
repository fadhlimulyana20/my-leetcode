class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLen = max(len(a), len(b))
        
        a = a.zfill(maxLen)
        b = b.zfill(maxLen)
        
        carry = 0
        newBin = []
        for i in range(maxLen -1, -1, -1):
            num_a = int(a[i])
            num_b = int(b[i])
            new_num = num_a + num_b + carry
            print(num_a, num_b, new_num)
            if new_num > 1:
                carry = 1 
                bin = new_num%2
                newBin.insert(0, bin)
            else:
                carry = 0
                newBin.insert(0, new_num)
        if carry == 1:
            newBin.insert(0, 1)
        newBinStr =  ''.join(str(x) for x in newBin)
        return newBinStr
        
if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11', '1'))