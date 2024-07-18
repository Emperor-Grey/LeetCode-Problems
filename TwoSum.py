from typing import List


class TwoSum:

    @staticmethod
    def indexes(nums: List[int], target: int) -> List[int]:
        """
        This is two sum problem. Should give two parameters target and a list of numbers
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        hashset: dict[int, int] = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            hashset[nums[i]] = i
            if complement in hashset:
                return [hashset[complement], complement]


ts = TwoSum()
print(ts.indexes([11, 2, 7, 4], 9))
print(ts.indexes([1, 2, 9, 10], 3))
