class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        for i in range(len(numbers)):
            csum = numbers[l]+numbers[r]
            if csum<target:
                l+=1
            elif csum>target:
                r-=1
            else:
                return [l+1,r+1]
        return []

        