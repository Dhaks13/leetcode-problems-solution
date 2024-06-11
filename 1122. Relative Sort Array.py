class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr, temp = [], []
        c = {}
        for i in arr1:
            if(i not in c):
                c[i] = 1
            else:
                c[i] += 1
        for i in arr2:
            while(c[i]>0):
                arr.append(i)
                c[i] -= 1
        for i in c:
            while(c[i]>0):
                temp.append(i)
                c[i] -= 1
        arr.extend(sorted(temp))
        return arr            
