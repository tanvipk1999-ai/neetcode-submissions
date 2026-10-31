class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l = 0
        min_len = float('inf')
        need = {}
        window = {}

        for c in t:
            need[c] = 1 + need.get(c, 0)

        have = 0
        required = len(need)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # Check whether this character's requirement is met
            if c in need and window[c] == need[c]:
                have += 1

            # Shrink while the window is valid
            while have == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]

                # Remove the leftmost character
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        return res