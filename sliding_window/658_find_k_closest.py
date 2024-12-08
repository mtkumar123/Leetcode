class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # first do binary search to find number
        # closest to x
        # in case x is not find keep track of
        # element that is closest to x and it's index
        l = 0
        r = len(arr) - 1
        val, idx = arr[0], 0

        while l <= r:
            mid = (l + r) // 2
            currdiff = abs(arr[mid] - x)
            valdiff = abs(val - x)

            if currdiff < valdiff:
                val = arr[mid]
                idx = mid
            elif currdiff == valdiff and arr[mid] <= val:
                val = arr[mid]
                idx = mid

            if x > arr[mid]:
                l = mid + 1
            elif x < arr[mid]:
                r = mid - 1
            else:
                break

        # start from idx because this is the number
        # that is the closest to x
        l = r = idx
        while (r - l + 1) < k:
            if l == 0:
                r = r + 1
            elif r == len(arr) - 1:
                l = l - 1
            elif x - arr[l - 1] <= arr[r + 1] - x:
                l = l - 1
            elif x - arr[l - 1] > arr[r + 1] - x:
                r = r + 1
        return arr[l : r + 1]


if __name__ == "__main__":
    s = Solution()
    s.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9)
