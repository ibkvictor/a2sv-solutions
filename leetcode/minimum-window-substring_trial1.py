from collections import defaultdict
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count_t = Counter(t)
        # len_t = len(t)
        # min_i = 0
        # min_j = -1

        # if len(t) > len(s):
        #     return ""

        # else:
        #     i = 0
        #     for j in range(len(s)):
        #         count = {k: 0 for k in count_t.keys()}

        #         if s[j] in count:
        #             len_t_found += 1
        #             count[s[j]] += 1

        #         while i < j and len_t_found > len_t:
        #             if s[i] in count:
        #                 len_t_found -= 1
        #                 count[s[j]] -= 1

        #             i += 1

        # return s[min_i: min_j + 1]




        # "F E A D O B E C O D  E  B  A  N  C"
        #  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

        # 0 5




        # while (t(counter) != s(counter) and permu == len(t)) i < j

        counter_t = 1
        counter = 
        seen_t = 

        i = 0
        count = Counter(s[0: len(t)])
        for j in range(len(t) - 1, len(s)):
            if s[i] in counter[t]:
                counter[s[i]] += 1

            while i < j and len_seen > and counter == counter_t:

                i += 1

        # a a a a a a a a a a a a b b b b b c d d
        # 0 1 2 3 4 5 6 7 8 9 10 11 

        # min_length = math.inf
        # max_sub_string = ""
        # for i in range(len(s)):
        #     count = defaultdict(int)
        #     for j in range(i, len(s)):
        #         if s[j] in t_set and count[s[j]] == t_set[s[j]]:
        #             count[s[j]] += 0

        #         else:
        #             count[s[j]] += 1
        #         # if i == 11 and j == 19:
        #         #     print(list(t_set.values()))

        #         if len(count.keys() & (t_set)) == len(t_set) and list(t_set.values()) == list(map(count.get, t_set.keys())): # hack this
        #             # print(i, j)
        #             # sub_string = s[i: j]
        #             if j - i + 1 < min_length:
        #                 min_length = j - i + 1
        #                 max_sub_string = s[i: j + 1]

        # return max_sub_string
