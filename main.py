from tp import transportationProblem

def main():

	demand = [325, 425, 475, 275]
	supply = [400, 500, 600]

	cost_matrix = [[8,6,12,9],[7,11,10,14],[13,8,8,7]]

	TP = transportationProblem(supply, demand, cost_matrix)

	# find the basic feasible solution using VAM (Vogel's Approximation Method)
	TP.vam()

	print(TP.getTotalCost()) 

main()