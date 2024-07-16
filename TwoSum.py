from typing import List


class TwoSum:

    @staticmethod
    def Indexes(nums: List[int], target: int) -> List[int]:
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
print(ts.Indexes([11, 2, 7, 4], 9))
print(ts.Indexes([1, 2, 9, 10], 3))
