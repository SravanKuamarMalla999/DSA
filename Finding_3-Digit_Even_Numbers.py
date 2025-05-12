from collections import Counter

class Solution:
    def findEvenNumbers(self, digits):
        result = []
        digit_count = Counter(digits)

        for num in range(100, 1000):
            if num % 2 != 0:
                continue  # not even
            num_digits = [int(d) for d in str(num)]
            num_count = Counter(num_digits)

            if all(num_count[d] <= digit_count[d] for d in num_count):
                result.append(num)

        return sorted(result)
