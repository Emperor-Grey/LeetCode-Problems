class Anagram:

    @staticmethod
    def is_anagram(s: str, t: str) -> bool:

        """
        Should return True if all the letters are present from first string param in second in param
        :param t: string
        :param s: str
        :return: Boolean
        """

        if len(s) != len(t):
            return False

        sSet = {}
        tSet = {}

        for char in s:
            sSet[char] = sSet.get(char, 0) + 1

        for char in t:
            tSet[char] = tSet.get(char, 0) + 1

        # print(sSet)
        # print(tSet)
        return sSet == tSet


ag = Anagram()
print(ag.is_anagram('anagram', 'nagaram'))
print(ag.is_anagram('cat', 'rat'))
