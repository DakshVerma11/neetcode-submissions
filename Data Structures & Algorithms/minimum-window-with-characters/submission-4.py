class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        scount = defaultdict(int)

        required = len(tcount)
        formed = 0

        l = 0
        ans = float("inf"), None, None

        for r in range(len(s)):
            c = s[r]
            scount[c] += 1

            if c in tcount and scount[c] == tcount[c]:
                formed += 1

            while l <= r and formed == required:

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                scount[s[l]] -= 1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    formed -= 1

                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]