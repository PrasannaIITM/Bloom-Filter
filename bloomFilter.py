import mmh3 # murmurhash: is faster for blooms
import math

class BloomFilter(object):

    def __init__(self, m, k):
        self.m = m # size of bloom filter
        self.k = k # number of hash functions
        self.n = 0 # total count of the elemnts inserted in the set
        self.bloomFilter = [0 for i in range(self.m)]
        
    def _setAllBitsToZero(self):
        self.n = 0
        for i in self.bloomFilter:
            self.bloomFilter[i] = 0
            
    def getBitArrayIndices(self, item):
        """
		hashes the key for k defined,
		returns a list of the indexes which have to be set
        """

        indexList = []
        for i in range(1, self.k + 1):
            indexList.append((hash(item) + i * mmh3.hash(item)) % self.m)
        return indexList
        
    def add(self, item):
        """
		Insert an item in the filter
        """
        
        for i in self.getBitArrayIndices(item):
            self.bloomFilter[i] = 1
        
        self.n += 1
    
    def contains(self, key):
        """
		returns whether item exists in the set or not
        """

        for i in self.getBitArrayIndices(key):
            if self.bloomFilter[i] != 1:
                return False
        return True
        
    def length(self):
        """
		returns the current size of the filter
        """

        return self.n
        
    def generateStats(self):
        """
		Calculates the statistics of a filter
		Probability of False Positives, predicted false positive rate, n, m, k.
        """

        n = float(self.n)
        m = float(self.m)
        k = float(self.k)
        probability_fp = math.pow((1.0 - math.exp(-(k*n)/m)), k)

        print("Number of elements entered in filter: ", n)
        print("Number of bits in filter: ", m)
        print("Number of hash functions used: ", k)

        print("Predicted Probability of false positives: ", probability_fp)
        print("Predicted false positive rate: ", probability_fp * 100.0, "%")
        
    def reset(self):
        """
		Resets the filter and clears old values and statistics
        """

        self._setAllBitsToZero()