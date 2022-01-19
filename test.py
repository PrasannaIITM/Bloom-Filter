from bloomFilter import BloomFilter
import uuid

def getRandomString():
    return str(uuid.uuid4())
    
def unitTest():
    print("\nTest BloomFilter implementation:\n")
    bf = BloomFilter(10, 3)
    bf.add('coding')
    bf.add('music')
    bf.add('cat')


    if bf.contains('coding'):
        print("Test: OK \tItem: 'coding' is present")
    else:
        print("Test: Failed \tItem: 'coding' is not present")

        
    if bf.contains('music'):
        print("Test: OK \tItem: 'music' is present")
    else:
        print("Test: Failed \tItem: 'music' is not present")
    
    if bf.contains('randomString'):
        print("Test: Failed \tRandom Item present")
    else:
        print("Test: OK \tRandom Item not present")
	
    bf.generateStats()
    print("\nUnit Test Completed\n")
    bf.reset()

def testBloomFilter(n, m, k):
    print("\nTest BloomFilter probability for large size:\n")
    existentItems = []
    
    bf = BloomFilter(m, k)
    
    for i in range(0, n):
        randomString = getRandomString()
        bf.add(randomString)
        if (i % 1000) == 0:
            existentItems.append(randomString)		
            
    #check membership of existing items
    for i in existentItems:
        if not bf.contains(i):
            print("Load test failed. Existent item not present")
    print("Load test OK. All existent items are present")

	#check membership of random items
    numFalsePositives = 0
    numRandom = 100000
    for i in range(0, numRandom):
        if bf.contains(getRandomString()):
            numFalsePositives += 1

    bf.generateStats()

    print("Number of false positives: " + str(numFalsePositives) + " out of " + str(numRandom) + " random items")
    print("Actual False positive rate: ", 100.0 * float(numFalsePositives)/float(numRandom), "%")
    
    bf.reset()
    print("\nTest Complete\n")


if __name__ == '__main__':
    unitTest()
    testBloomFilter(200000, 1000000, 3)