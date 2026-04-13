class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        # build first window
        for i in range(len(s1)):
            count_s2[ord(s2[i]) - ord('a')] += 1

        if count_s2 == count_s1:
            return True

        # sliding window
        for r in range(len(s1), len(s2)):
            count_s2[ord(s2[r - len(s1)]) - ord('a')] -= 1
            count_s2[ord(s2[r]) - ord('a')] += 1

            if count_s2 == count_s1:
                return True
        return False
