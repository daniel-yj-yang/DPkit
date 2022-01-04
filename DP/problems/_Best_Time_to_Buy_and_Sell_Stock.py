# -*- coding: utf-8 -*-

# Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
# License: BSD-3-Clause


from functools import lru_cache
import inspect


class Best_Time_to_Buy_and_Sell_Stock():

    def explanation(self):
        print(f"\nThe question provides an prices array of the price of a given stock on the i-th day, and asks you to return the maximum profit that can be achieved from buying and selling on a different day in the future.")
        print(f"\nSome possible recurrence relations:\n")
        print(f"(1) min_price_past_and_now(i) = min(prices[i], min_price_past_and_now(i-1)), and max_profit_past_and_now = max(max_profit_past_and_now, prices[i] - min_price_past_and_now(i)), while counting from prices[0] forward;\n")
        print(f"(2) max_price_now_n_future(i) = max(prices[i], max_price_now_n_future(i+1)), and max_profit_now_n_fugure = max(max_profit_now_n_fugure, max_price_now_n_future(i) - prices[i]), while counting from prices[-1] backward;\n")
        print(f"(3) max_profit(i) = max(price_diff[i], price_diff[i] + max_profit(i-1)), for i in range(1, len(prices)), where price_diff[i] = prices[i] - prices[i-1]; this is basically to find the max. subarray sum with the array being np.diff(prices);\n")
        print(f"(4) max_profit(i) = max(0,             price_diff[i] + max_profit(i-1)), while all else the same as in (3); this is because if price_diff[i] < 0, it is better off not having that transaction at all to ensure that max_profit(i) >= 0;\n")
        print(inspect.getsource(self.top_down) + '\n')
        print(inspect.getsource(self.bottom_up))

    def top_down(self, prices=[7, 1, 5, 3, 6, 4, 2, 10, 2, 3, 9, 1]):
        """
        Recursion + Memoization;
        Time Complexity O(n), Space Complexity O(n) for the recursion call stack
        this is implementing #4 recurrence relation above
        """
        @lru_cache(maxsize=None)
        def max_profit(i):
            nonlocal global_max
            if i == 0:
                return 0
            res = max(0, prices[i] - prices[i-1] + max_profit(i-1))
            global_max = max(global_max, res)
            return res
        global_max = 0
        max_profit(len(prices)-1)
        return global_max

    def bottom_up(self, prices=[7, 1, 5, 3, 6, 4, 2, 10, 2, 3, 9, 1]):
        """
        Tabulation - full tabulation has Space Complexity O(n); keeping only needed items has Space Complexity O(1)
        Time Complexity O(n), Space Complexity O(1)
        this is implementing #4 recurrence relation above
        """
        global_max = max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(0, prices[i] - prices[i-1] + max_profit)
            global_max = max(global_max, max_profit)
        return global_max
