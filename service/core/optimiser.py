from ortools.algorithms import pywrapknapsack_solver
# from sample_data import values, weights, capacities


def optimiser(values, weights, capacities ):
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    packed_values = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            print(f"{i=}")
            packed_values.append(i)
            packed_weights.append(weights[0][i])
            print(f"{weights[0][i]}")
            total_weight += weights[0][i]
    # print('Total weight:', total_weight)
    # print('Packed items:', packed_values)
    # print('Packed_weights:', packed_weights)

    return computed_value, total_weight, packed_values, packed_weights


