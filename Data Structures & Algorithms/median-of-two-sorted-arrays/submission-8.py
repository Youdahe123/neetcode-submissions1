class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A,B = B,A

        l = 0
        r = len(A) - 1

        while True:
            mid = ( l + r) // 2
            j = half - mid - 2

            ALeft = A[mid] if mid >= 0 else float('-inf')
            ARight = A[mid + 1] if mid + 1 < len(A) else float('inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            BRight = B[j + 1] if  j + 1 < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 1:
                    return min(ARight,BRight)
                left = max(ALeft,BLeft)
                right = min(ARight,BRight)

                return (left + right) / 2
            elif ALeft > BRight:
                r = mid - 1
            else:
                l = mid + 1     