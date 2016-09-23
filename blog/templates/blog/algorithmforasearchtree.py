function searchtree(problem, strategy) returns a solution or a failure
	initialise the search using the initial state of the problem
	do loop
		if there are no candidates for expansion,then return failure
		choose the leafnode for expansion according to strategy

		if the node contains the goal state then return the corresponding solution
		else expand the node and add the resulting nodes to the search there

	end