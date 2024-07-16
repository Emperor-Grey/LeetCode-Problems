from typing import List


class Duplicate:

    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        """
        :param nums: List of Integers
        :return: boolean (True or False)

        """
        # for i in nums:
        #     counter = nums.count(i)
        #     return True if counter > 1 else False

        return len(nums) != len(set(nums))


duplicate = Duplicate()
print(duplicate.containsDuplicate([1, 2, 3, 1, 3, 6]))
print(duplicate.containsDuplicate([1, 3, 6, 8, 9]))
