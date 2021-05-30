class solution:
    def hammit(sefl, x, y):
        return bin(x^y).count('1') #hàm bin() lấy về chuổi nhị phân #count đếm 1 xuât hiện bao nhiêu lần trong bin
o = solution()
print(o.hammit(4,2))