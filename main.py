from tp import transportationProblem

def tc(n): 
	
	if n==0: # Answer = 10950

		supply = [400, 500, 600]
		demand = [325, 425, 475, 275]
		cost_matrix = [[8,6,12,9],[7,11,10,14],[13,8,8,7]]

	elif n==1: # Answer = 779

		supply = [7,9,18]
		demand = [5,8,7,14]
		cost_matrix = [[19,30,50,10],[70,30,40,60],[40,8,70,20]]

	elif n==2: # Answer = 2850

		supply = [300, 400, 500]
		demand = [250,350,400,200]
		cost_matrix = [[3,1,7,4],[2,6,5,9],[8,3,3,2]]
	
	elif n==3: # Answer = 2420

		supply = [100,60,80,60,50]
		demand = [60,40,100,50,100]
		cost_matrix = [[4,9,10,5,13],[9,17,19,9,11],[12,3,9,7,5],[6,17,8,14,10],[7,4,5,15,12]]

	else: # Answer = 12075
	
		supply = [250,300,400]
		demand = [200, 225, 275, 250]
		cost_matrix = [[11,13,17,14],[16,18,14,10],[21,24,13,10]]

	return [supply, demand, cost_matrix]	

def main():

	# find the basic feasible solution using VAM (Vogel's Approximation Method)

	for i in range(5):
		supply, demand, cost_matrix = tc(i)
		TP = transportationProblem(supply, demand, cost_matrix)
		TP.vam()
		print(TP.getTotalCost()) 

main()