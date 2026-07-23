class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex, rightIndex=0,len(numbers)-1
        while leftIndex<rightIndex:
            current=numbers[leftIndex]+numbers[rightIndex]
            if current==target:
                return [leftIndex+1, rightIndex+1]
            elif current<target:
                leftIndex+=1
            else:
                rightIndex-=1
        
        
