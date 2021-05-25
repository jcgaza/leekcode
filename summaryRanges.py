def summaryRanges(self, nums: List[int]) -> List[str]:
    if len(nums) == 0:
        return []
    
    ans = []
    finalStr = ""
    i = 0
    
    while i < len(nums):
        if len(finalStr) == 0:
            if i+1 < len(nums) and nums[i+1] != nums[i]+1:
                ans.append(str(nums[i]))
                i += 1
                continue
            elif i+1 == len(nums):
                ans.append(str(nums[i]))
                break
            elif i+1 < len(nums) and nums[i+1] == nums[i]+1:
                finalStr = str(nums[i])
        else:
            if i+1 < len(nums) and nums[i+1] != nums[i]+1:
                ans.append(finalStr+"->"+str(nums[i]))
                finalStr = ""
            elif i+1 == len(nums):
                ans.append(finalStr+"->"+str(nums[i]))
        
        i += 1
    
    
    return ans