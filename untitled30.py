# Python program to find maximum contiguous subarray

# Function to find the maximum contiguous subarray
from sys import maxint
def maxSubArraySum(a,size):
	
	max_so = -maxint - 1
	max_end = 0
	
	for i in range(0, size):
		max_end = max_end + a[i]
		if (max_end>max_so):
			max_so= max_end

		if max_end< 0:
			max_end = 0
	return max_so

# Driver function to check the above function 
a = [13, -3, 4]
print "Maximum contiguous sum is", maxSubArraySum(a,len(a))

#This code is contributed by _Devesh Agrawal_
