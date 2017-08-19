
def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict = {}
        for i in range(len(list1)):
            dict[list1[i]] = i

        min_sum = 1000000
        sum = 0
        possibleAnswers = []
        for j in range(len(list2)):
            if dict.__contains__(list2[j]):
                sum = j + dict[list2[j]]
                if sum < min_sum:
                    min_sum = sum
                    possibleAnswers = []
                    possibleAnswers.append(list2[j])
                elif sum == min_sum:
                    possibleAnswers.append(list2[j])

        return possibleAnswers;

a = ["Shogun","Tapioca Express","Burger King","KFC"]
b = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

print(findRestaurant(a, b))
