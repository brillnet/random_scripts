class Solution:    
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):

        listOfTriplets = []

        #  Converting original list to a dictionary.
        convertedListDictionary = {}

        #  Converting the list of nums into a dictionary
        #  example nums=[1,2,3]
        #  The below keys is the value in the list.
        #  the below values are a list with the first
        #  element being the index of the value in the
        #  list followed by the value in the list.

        #  convertedDictionary[1] = [0,1]
        #  convertedDictionary[2] = [1,2]
        #  convertedDictionary[3] = [2,3]


        for k in range(len(nums)):
            # convertedListDictionary[nums[k]] = k
            convertedListDictionary[nums[k]] = [k,nums[k]]

        for i in range(len(nums)):
            for j in range(len(nums)):

                #  Confirming i != j
                if i == j or j < i:
                    continue

                #  Getting the sum of two numbers in the list. This value
                #  will be used to look for the third value in the 
                #  convertedListDictionary.
                twoSum = nums[i] + nums[j]

                if twoSum < 0:
                    #  Check to see if the positive value is in
                    #  convertedListDictionary
                    absolute_sum = abs(twoSum)

                    # if absolute_sum in convertedListDictionary and (absolute_sum != nums[i] or absolute_sum != nums[j]):
                    if absolute_sum in convertedListDictionary:

                        #  Confirming that i != k, and j != k
                        if i != convertedListDictionary[absolute_sum][0] and j != convertedListDictionary[absolute_sum][0]:

                            tempListOfTriplets = sorted([nums[i],nums[j],convertedListDictionary[abs(twoSum)][1]])

                            #  Confirming there are duplicates in templist and confirming the tempListOfTriplets
                            #  isn't already in the final list of triplets.
                            if tempListOfTriplets not in listOfTriplets:
                                if tempListOfTriplets not in listOfTriplets:
                                    listOfTriplets.append(tempListOfTriplets)

                #  If two sum is positive we will look for the negative
                #  value of twoSum in the convertedListDictionary
                else:

                    #  Finding absolute negative sum
                    negative_absolute_sum = -abs(twoSum)

                    if negative_absolute_sum in convertedListDictionary:
                        #  Confriming that i != k, and j != k
                        if i != convertedListDictionary[negative_absolute_sum][0] and j != convertedListDictionary[negative_absolute_sum][0]:
                            tempListOfTriplets = sorted([nums[i],nums[j],convertedListDictionary[negative_absolute_sum][1]])

                            # if len(list(set(tempListOfTriplets))) == 3 and tempListOfTriplets not in listOfTriplets:
                            if tempListOfTriplets not in listOfTriplets:
                                if tempListOfTriplets not in listOfTriplets:
                                    listOfTriplets.append(tempListOfTriplets)

        return listOfTriplets
SolutionObj = Solution()
print(SolutionObj.threeSum([-1,0,1,2,-1,-4]))

# The distinct triplets are [-1,0,1] and [-1,-1,2].