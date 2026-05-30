class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #nums.sort()
        n=len(nums)
        memo=[-1]*(target+1)
        memo[0]=1
        def dfs(total):
            if memo[total] != -1:
                return memo[total]

            res = 0
            for i in range(len(nums)):
                if total < nums[i]:
                    continue
                res += dfs(total - nums[i])
            memo[total]=res
            return res

        return dfs(target)