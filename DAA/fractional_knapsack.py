# Practical 3
# Write a program to solve a fractional Knapsack problem using greedy method

def fractional_knapsack_by_ratio(items, capacity):
	sorted_items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)    
	total_value = 0
	
	for value, weight in sorted_items:
		if capacity >= weight:
			total_value += value
			capacity -= weight
		else:
			total_value += capacity * (value / weight)
			break
	
	return total_value

def fractional_knapsack_by_weight(items, capacity):
	sorted_items = sorted(items, key=lambda x: x[1])    
	total_value = 0
	
	for value, weight in sorted_items:
		if capacity >= weight:
			total_value += value
			capacity -= weight
		else:
			total_value += capacity * (value / weight)
			break
	
	return total_value

def fractional_knapsack_by_value(items, capacity):
	sorted_items = sorted(items, key=lambda x: x[0], reverse=True)    
	total_value = 0
	
	for value, weight in sorted_items:
		if capacity >= weight:
			total_value += value
			capacity -= weight
		else:
			total_value += capacity * (value / weight)
			break
	
	return total_value

def main():
	items = [[60, 10], [100, 20], [120, 30]]  # Different values for different results
	capacity = 50
	
	max_value_ratio = fractional_knapsack_by_ratio(items, capacity)
	max_value_weight = fractional_knapsack_by_weight(items, capacity)
	max_value_value = fractional_knapsack_by_value(items, capacity)
	
	print(f"Maximum value by value/weight ratio: {max_value_ratio:.2f}")
	print(f"Maximum value by weight: {max_value_weight:.2f}")
	print(f"Maximum value by value: {max_value_value:.2f}")

if __name__ == "__main__":
	main()		

