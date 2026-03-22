class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, 0
        countW = 0

        # build first window
        while r < l + k:
            if blocks[r] == 'W':
                countW += 1
            r += 1

        res = countW

        # sliding
        while r < len(blocks):
            if blocks[l] == 'W':
                countW -= 1
            if blocks[r] == 'W':
                countW += 1

            res = min(res, countW)
            l += 1
            r += 1

        return res
