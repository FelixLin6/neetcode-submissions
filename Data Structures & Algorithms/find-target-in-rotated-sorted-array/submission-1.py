class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[l] < nums[mid]:
                l = mid
            else:
                r = mid

        p = l + 1
        print(p)

        def bsearch(seg: List[int]) -> int:
            lo, hi = 0, len(seg) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                print(lo, hi, mid)
                if seg[mid] == target:
                    return mid
                elif seg[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        print(nums[:p], nums[p:])
        resL, resR = bsearch(nums[:p]), bsearch(nums[p:])
        if resL > -1:
            return resL
        elif resR > -1: 
            return resR + p
        
        return -1
