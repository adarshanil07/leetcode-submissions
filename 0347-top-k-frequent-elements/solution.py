class Solution(object):
    def topKFrequent(self, nums, k):
        num_dict = {}


        for number in nums:
            try:
                num_dict[number] += 1
            except KeyError:
                num_dict[number] = 1
         
        freqNums = []
        numFreqPairs = []

        if len(num_dict.keys()) == 0:
            return freqNums

        numFreqPairs = sorted(num_dict.items(), key=lambda pair: pair[1], reverse=True)

        for i in range(0, k):
            freqNums.append(self.getMax(numFreqPairs))

        return freqNums


    def getMax(self, numFreqPairs):

        numberToRemove, freq = numFreqPairs[0]
        numFreqPairs.pop(0)
        return numberToRemove
        
