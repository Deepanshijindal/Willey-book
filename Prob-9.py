import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("Economic Planning")

# Define parameters
years = range(0,6)  # Including initial year 0
industries = ['coal', 'steel', 'transport']
initial_stocks = {'coal': 150, 'steel': 80, 'transport': 100}
exogenous_demand = {'coal': 60, 'steel': 60, 'transport': 30}
manpower_capacity = 470
inputs_production = {
    'coal': {'coal': 0.1, 'steel': 0.5, 'transport': 0.4, 'manpower': 0.6},
    'steel': {'coal': 0.1, 'steel': 0.1, 'transport': 0.2, 'manpower': 0.3},
    'transport': {'coal': 0.2, 'steel': 0.1, 'transport': 0.2, 'manpower': 0.2}
}
inputs_capacity = {
    'coal': {'coal': 0.0, 'steel': 0.7, 'transport': 0.9, 'manpower': 0.4},
    'steel': {'coal': 0.1, 'steel': 0.1, 'transport': 0.1, 'manpower': 0.2},
    'transport': {'coal': 0.2, 'steel': 0.1, 'transport': 0.2, 'manpower': 0.1}
}

# Define decision variables
production = model.addVars(years, industries, name="production", lb=0)
stocks = model.addVars(years, industries, name="stocks", lb=0)
capacity_expansion = model.addVars(range(2,7), industries, name="capacity_expansion", lb=0)

# Initial stocks
for ind in industries:
    model.addConstr(stocks[0, ind] == initial_stocks[ind])

# Constraints for each year
for t in range(0,5):  # Constraints for years 0 to 4
    for ind in industries:
        # Total input constraint
        total_input = (
            sum(inputs_production[ind][j] * production[t+1, j] for j in industries)
            + sum(inputs_capacity[ind][j] * capacity_expansion[t+2, j] for j in industries)
            + stocks[t, ind]
            - stocks[t+1, ind]
            - exogenous_demand[ind]
        )
        model.addConstr(total_input == 0)

# Manpower constraint
for t in range(0,5):  # Constraints for years 0 to 4
    total_manpower = (
        0.6 * production[t+1, 'coal'] + 0.3 * production[t+1, 'steel'] + 0.2 * production[t+1, 'transport']
        + 0.4 * capacity_expansion[t+2, 'coal'] + 0.2 * capacity_expansion[t+2, 'steel'] + 0.1 * capacity_expansion[t+2, 'transport']
    )
    model.addConstr(total_manpower <= manpower_capacity)

# # Productive capacity constraint
# for ind in industries:
#     total_capacity = (
#         initial_stocks[ind]
#         + sum(capacity_expansion[l, ind] for l in range(1, 6))  # Sum for years 1 to 5
#     )
#     model.addConstr(production[4, ind] <= total_capacity)

# Productive capacity constraint
for t in range(0, 5):  # years 1 to 5
    for ind in industries:
        total_capacity = (
            initial_stocks[ind]  # initial capacity in year 0
            + sum(capacity_expansion[l, ind] for l in range(2, t+2))  # Sum for years 2 to t+2
        )
        model.addConstr(production[t, ind] <= total_capacity)


# Objective: Maximize total productive capacity at the end of 5 years
total_capacity_5years = sum(capacity_expansion[5, ind] for ind in industries)
model.setObjective(total_capacity_5years, GRB.MAXIMIZE)

# Optimize the model
model.optimize()

# # Print results
# if model.status == GRB.OPTIMAL:
#     print("Optimal solution found:")
#     for t in years:
#         print(f"Year {t}:")
#         for ind in industries:
#             print(f"  {ind.capitalize()} production: {production[t, ind].x:.2f}")
# else:
#     print("No optimal solution found.")
# Print results

if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    for t in range(0, 6):  # Print results for years 1 to 5
        print(f"Year {t}:")
        for ind in industries:
            print(f"  {ind.capitalize()} production: {production[t, ind].x:.2f}, Stock: {stocks[t, ind].x:.2f}")
else:
    print("No optimal solution found.")
