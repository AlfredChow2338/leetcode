# hash map
class Solution:
    def countLargestGroup(self, n: int) -> int:
        a = {}
        res, max_children_num = 0, 0
        def get_digit_sum(num):
            s = 0
            for d in str(num):
                s += int(d)
            return s
        for i in range(1, n+1):
            curr_sum = get_digit_sum(i)
            a[curr_sum] = a.get(curr_sum, 0) + 1
            if a[curr_sum] == max_children_num:
                res += 1
            if a[curr_sum] > max_children_num:
                max_children_num = a[curr_sum]
                res = 0
        return res

# arithmetic
class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_count = [0] * 37 # 1 <= n <= 10000 biggest 9999 = 36
        res, max_children_num = 0, 0
        for i in range(1, n+1):
            curr_sum = 0
            temp = i
            while temp > 0:
                curr_sum += temp % 10
                temp //= 10
            sum_count[curr_sum] += 1
            if sum_count[curr_sum] == max_children_num:
                res += 1
            if sum_count[curr_sum] > max_children_num:
                max_children_num = sum_count[curr_sum]
                res = 1
        return res