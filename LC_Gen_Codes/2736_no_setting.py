class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        n = len(nums1)
        
        for query in queries:
            xi, yi = query
            max_sum = -1
            
            for j in range(n):
                if nums1[j] >= xi and nums2[j] >= yi:
                    max_sum = max(max_sum, nums1[j] + nums2[j])
            
            answer.append(max_sum)
        
        return answer