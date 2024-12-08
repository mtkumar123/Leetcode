class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        winsum = 0
        result = 0
        lp = 0
        for index, rp in enumerate(arr):
            winsum += rp

            if index - lp + 1 == k:
                # Let's check the average
                avg = winsum / k
                if avg >= threshold:
                    result += 1

                # Now let's move lp
                winsum -= arr[lp]
                lp += 1

        return result
