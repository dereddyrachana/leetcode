class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

		# HashMap for the solution, to avoid duplicates
        solution = {}
		
		# i = 0 ..... n-1
        for i in range( len(nums) ):
			#j = i+1 ..... n-1
            for j in range( i+1, len( nums ) ):
                start = j+1
                end = len(nums) - 1
                while ( start < end ):
                    temp = nums[i] + nums[j] + nums[start] + nums[end]
                    
                    if ( temp == target ):
                        solution[ nums[i], nums[j], nums[start], nums[end] ] = True
                        start +=1
                        end -=1
                    elif temp < target:
                        start+=1
                    else:
                        end -=1
        
        return solution.keys()
                            
