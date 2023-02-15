# A Dynamic Programming based Python3 program to
# find minimum of coins to make a given change V
import sys

# m is size of coins array (number of
# different coins)
def minCoins(coins, m, V):
	
	# table[i] will be storing the minimum
	# number of coins required for i value.
	# So table[V] will have result
	table = [0 for i in range(V + 1)]

	# Base case (If given value V is 0)
	table[0] = 0

	# Initialize all table values as Infinite
	for i in range(1, V + 1):
		table[i] = sys.maxsize

	# Compute minimum coins required
	# for all values from 1 to V
	for i in range(1, V + 1):
		
		# Go through all coins smaller than i
		for j in range(m):
			if (coins[j] <= i):
				sub_res = table[i - coins[j]]
				if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
					table[i] = sub_res + 1
	
	if table[V] == sys.maxsize:
		return -1
	
	return table[V]

# Driver Code
british_pound_coins = [1,2,5,10,15,20]
us_dollar_coins = [1,5,10,25]
norwegian_krone_coins = [1,5,10,20]
b = len(british_pound_coins)
u = len(us_dollar_coins)
n = len(norwegian_krone_coins)
change = int(input("How much change required? "))
print("Minimum British coins required is ",minCoins(british_pound_coins,b,change))
print("Minimum US coins required is ",minCoins(us_dollar_coins,u,change))
print("Minimum Norwegian coins required is ",minCoins(norwegian_krone_coins,n,change))
