class Palindrome:
    @staticmethod
    def isPalindrome(num: int) -> bool:

        """
        :param num: Int
        :return: Boolean
        """

        temp = num
        startNum = 0

        if num < 0:
            return False

        while temp > 0:
            endNum = temp % 10
            startNum = startNum * 10 + endNum
            temp = temp // 10

        return startNum == num


palindrome = Palindrome()
print(palindrome.isPalindrome(121))
