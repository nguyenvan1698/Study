#Given a string, find the length of the longest substring in it with no more
#than K distinct characters.
import math


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # define maxLength
        maxLength = 0;
        lenght = len(s)

        # define pointer
        cur_end = 0
        cur_start = 0

        # define hashtable
        charHash = {}

        while cur_end < lenght:
            # update hashtable
            if s[cur_end] in charHash:
                charHash[s[cur_end]] += 1
            else:
                print()
                charHash.update({s[cur_end]: 1})

            # contract windown table
            while (len(charHash) > k):
                charHash[s[cur_start]] -= 1
                if charHash[s[cur_start]] == 0:
                    del charHash[s[cur_start]]
                cur_start +=1

                # update max value
            maxLength = max(maxLength, (cur_end - cur_start + 1))

            # move cur_end to next
            cur_end +=1

        return maxLength


test = Solution()

result = test.longestSubstring('araaci',3)
print('result is:')
print(result)





