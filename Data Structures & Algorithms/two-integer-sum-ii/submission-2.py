class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex=0
        rightIndex=len(numbers)-1
        while True:
            total=numbers[leftIndex]+numbers[rightIndex]
            if total>target:
                rightIndex-=1
            elif total<target:
                leftIndex+=1
            else:
                return [leftIndex+1, rightIndex+1]
            

