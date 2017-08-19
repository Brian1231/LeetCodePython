class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for i in range(1, n + 1):
            res = ""
            if i % 3 == 0:
                res += "Fizz"
            if i % 5 == 0:
                res += "Buzz"

            if res == "":
                # print("here")
                list.append(str(i))
            else:
                list.append(res)

        return list