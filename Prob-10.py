# import gurobipy as gp
# from gurobipy import GRB

# # Create a new model
# model = gp.Model("Decentralisation")

# cities = ['Bristol', 'Brighton', 'London']
# offices = ['A', 'B', 'C', 'D', 'E']
# m = len(cities)
# n = len(offices)
# # Benefits
# benefits = {
#     'Bristol': {'A': 10, 'B': 15, 'C': 10, 'D': 20, 'E': 5},
#     'Brighton': {'A': 10, 'B': 20, 'C': 15, 'D': 15, 'E': 15},
#     'London': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
# }

# # Quantities of communication
# quantities_of_communication = {
#     'A': {'A': 0.0, 'B': 0.0, 'C': 1.0, 'D': 1.5, 'E': 0.0},
#     'B': {'A': 0.0, 'B': 0.0, 'C': 1.4, 'D': 1.2, 'E': 0.0},
#     'C': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 2.0},
#     'D': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.7},
#     'E': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0}  # Assuming symmetric and default 0 for E to others
# }

# # Costs per unit of communication
# costs_per_unit_of_communication = {
#     'Bristol': {'Bristol': 5, 'Brighton': 14, 'London': 13},
#     'Brighton': {'Bristol': 0, 'Brighton': 5, 'London': 9},
#     'London': {'Bristol': 0, 'Brighton': 0, 'London': 10}
# }

# # Decision variables
# office_city = model.addVars(offices, cities, vtype=GRB.BINARY, name='office_city')

# gamma = {}
# for i in range(n):
#     for k in range(i+1, n):
#         for j in range(m):
#             for l in range(m):
#                 gamma[(offices[i], cities[j], offices[k], cities[l])] = model.addVar(vtype=GRB.BINARY, name=f"gamma_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")

# # Add constraints γijkl - δij ≤ 0
# for i in range(n):
#     for k in range(i+1, n):
#         for j in range(m):
#             for l in range(m):
#                 model.addConstr(gamma[(offices[i], cities[j], offices[k], cities[l])] - office_city[offices[i], cities[j]] <= 0, name=f"c1_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")
#                 model.addConstr(gamma[(offices[i], cities[j], offices[k], cities[l])] - office_city[offices[k], cities[l]] <= 0, name=f"c2_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")

# # Add constraints δij + δkl - γijkl ≤ 1
# for i in range(n):
#     for k in range(i+1, n):
#         for j in range(m):
#             for l in range(m):
#                 model.addConstr(office_city[offices[i], cities[j]] + office_city[offices[k], cities[l]] - gamma[(offices[i], cities[j], offices[k], cities[l])] <= 1, name=f"c3_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")

# # Constraints
# for city in cities:
#     model.addConstr(sum(office_city[office, city] for office in offices) <= 3, f"Maxoffices_{city}")

# for office in offices:
#     model.addConstr(sum(office_city[office, city] for city in cities) == 1, f"OneCity_{office}")

# # Objective function
# objective = -gp.quicksum(
#     benefits[city][office] * office_city[office, city]
#     for office in offices
#     for city in cities
# ) + gp.quicksum(
#     quantities_of_communication[offices[i]][offices[k]] * 
#     costs_per_unit_of_communication[cities[j]][cities[l]] * 
#     gamma[(offices[i], cities[j], offices[k], cities[l])]
#     for i in range(n) for k in range(i+1, n)
#     for j in range(m) for l in range(m)
# )

# model.setObjective(objective, GRB.MINIMIZE)

# # Optimize the model
# model.optimize()

# # Check if the optimization was successful
# if model.status == GRB.OPTIMAL:
#     print("Optimal solution found!")
#     for office in offices:
#         for city in cities:
#             if office_city[office, city].x > 0.5:
#                 print(f"Office {office} should be located in {city}")
#     print(f"Optimal cost: {model.objVal}")
# else:
#     print("No optimal solution found.")


# import gurobipy as gp
# from gurobipy import GRB

# # Create a new model
# model = gp.Model("Decentralisation")

# cities = ['Bristol', 'Brighton', 'London']
# offices = ['A', 'B', 'C', 'D', 'E']
# m = len(cities)
# n = len(offices)

# # Benefits
# benefits = {
#     'Bristol': {'A': 10, 'B': 15, 'C': 10, 'D': 20, 'E': 5},
#     'Brighton': {'A': 10, 'B': 20, 'C': 15, 'D': 15, 'E': 15},
#     'London': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
# }

# # Quantities of communication
# quantities_of_communication = {
#     'A': {'A': 0.0, 'B': 0.0, 'C': 1.0, 'D': 1.5, 'E': 0.0},
#     'B': {'A': 0.0, 'B': 0.0, 'C': 1.4, 'D': 1.2, 'E': 0.0},
#     'C': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 2.0},
#     'D': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.7},
#     'E': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0}
# }

# # Costs per unit of communication
# costs_per_unit_of_communication = {
#     'Bristol': {'Bristol': 5, 'Brighton': 14, 'London': 13},
#     'Brighton': {'Bristol': 0, 'Brighton': 5, 'London': 9},
#     'London': {'Bristol': 0, 'Brighton': 0, 'London': 10}
# }

# # Decision variables
# office_city = model.addVars(offices, cities, vtype=GRB.BINARY, name='office_city')
# gamma = model.addVars(offices, cities, offices, cities, vtype = GRB.BINARY, name = 'gamma')

# # gamma = {}
# # for i in range(n):
# #     for k in range(i+1, n):
# #         for j in range(m):
# #             for l in range(m):
# #                 gamma[(offices[i], cities[j], offices[k], cities[l])] = model.addVar(vtype=GRB.BINARY, name=f"gamma_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")

# # # Add constraints γijkl - δij ≤ 0
# # for i in range(n):
# #     for k in range(i+1, n):
# #         for j in range(m):
# #             for l in range(m):
# #                 model.addConstr(gamma[(offices[i], cities[j], offices[k], cities[l])] - office_city[offices[i], cities[j]] <= 0, name=f"c1_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")
# #                 model.addConstr(gamma[(offices[i], cities[j], offices[k], cities[l])] - office_city[offices[k], cities[l]] <= 0, name=f"c2_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")

# # # Add constraints δij + δkl - γijkl ≤ 1
# # for i in range(n):
# #     for k in range(i+1, n):
# #         for j in range(m):
# #             for l in range(m):
# #                 model.addConstr(office_city[offices[i], cities[j]] + office_city[offices[k], cities[l]] - gamma[(offices[i], cities[j], offices[k], cities[l])] <= 1, name=f"c3_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")


# model.addConstr(gamma[])
# # Constraints: Each department must be located in exactly one city
# for office in offices:
#     model.addConstr(sum(office_city[office, city] for city in cities) == 1, f"OneCity_{office}")

# # Constraints: No city may be the location for more than three departments
# for city in cities:
#     model.addConstr(sum(office_city[office, city] for office in offices) <= 3, f"Maxoffices_{city}")

# # Objective function: Minimize -sum(Bij * deltaij) + sum(Cik * Djl * gammaijkl)
# objective = -gp.quicksum(
#     benefits[city][office] * office_city[office, city]
#     for office in offices
#     for city in cities
# ) + gp.quicksum(
#     quantities_of_communication[offices[i]][offices[k]] * 
#     costs_per_unit_of_communication[cities[j]][cities[l]] * 
#     gamma[(offices[i], cities[j], offices[k], cities[l])]
#     for i in range(n) for k in range(i+1, n)
#     for j in range(m) for l in range(m)
# )

# model.setObjective(objective, GRB.MINIMIZE)

# # Optimize the model
# model.optimize()

# # Check if the optimization was successful
# if model.status == GRB.OPTIMAL:
#     print("Optimal solution found!")
#     for office in offices:
#         for city in cities:
#             if office_city[office, city].x > 0.5:
#                 print(f"Office {office} should be located in {city}")
#     print(f"Optimal cost: {model.objVal}")
# else:
#     print("No optimal solution found.")


import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("Decentralisation")

cities = ['Bristol', 'Brighton', 'London']
offices = ['A', 'B', 'C', 'D', 'E']
m = len(cities)
n = len(offices)

# Benefits
benefits = {
    'Bristol': {'A': 10000, 'B': 15000, 'C': 10000, 'D': 20000, 'E': 5000},
    'Brighton': {'A': 10000, 'B': 20000, 'C': 15000, 'D': 15000, 'E': 15000},
    'London': {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
}

# Quantities of communication
quantities_of_communication = {
    'A': {'A': 0.0, 'B': 0.0, 'C': 1000.0, 'D': 1500.0, 'E': 0.0},
    'B': {'A': 0.0, 'B': 0.0, 'C': 1400.0, 'D': 1200.0, 'E': 0.0},
    'C': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 2000.0},
    'D': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 700.0},
    'E': {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0}  # Assuming symmetric and default 0 for E to others
}

# Costs per unit of communication
costs_per_unit_of_communication = {
    'Bristol': {'Bristol': 5, 'Brighton': 14, 'London': 13},
    'Brighton': {'Bristol': 14, 'Brighton': 5, 'London': 9},
    'London': {'Bristol': 13, 'Brighton': 9, 'London': 10}
}

# Decision variables
office_city = model.addVars(offices, cities, vtype=GRB.BINARY, name='office_city')

# Initialize gamma variable
gamma = model.addVars(offices, cities, offices, cities, vtype=GRB.BINARY, name='gamma')

# Add constraints γijkl - δij ≤ 0 and γijkl - δkl ≤ 0
for i in range(n):
    for k in range(n):
        # if i < k:
        for j in range(m):
            for l in range(m):
                model.addConstr(gamma[offices[i], cities[j], offices[k], cities[l]] - office_city[offices[i], cities[j]] <= 0, name=f"c1_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")
                model.addConstr(gamma[offices[i], cities[j], offices[k], cities[l]] - office_city[offices[k], cities[l]] <= 0, name=f"c2_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")
                model.addConstr(office_city[offices[i], cities[j]] + office_city[offices[k], cities[l]] - gamma[offices[i], cities[j], offices[k], cities[l]] <= 1, name=f"c3_{offices[i]}_{cities[j]}_{offices[k]}_{cities[l]}")

# Constraints: Each department must be located in exactly one city
for office in offices:
    model.addConstr(sum(office_city[office, city] for city in cities) == 1, f"OneCity_{office}")

# Constraints: No city may be the location for more than three departments
for city in cities:
    model.addConstr(sum(office_city[office, city] for office in offices) <= 3, f"Maxoffices_{city}")

# Objective function: Minimize -sum(Bij * deltaij) + sum(Cik * Djl * gammaijkl)
objective =  -gp.quicksum(
    benefits[city][office] * office_city[office, city]
    for office in offices
    for city in cities
) + gp.quicksum(
    quantities_of_communication[offices[i]][offices[k]] * 
    costs_per_unit_of_communication[cities[j]][cities[l]] * 
    gamma[offices[i], cities[j], offices[k], cities[l]]
    for i in range(n) for k in range(n)  if k>i
    for j in range(m) for l in range(m) 
)

model.setObjective(objective, GRB.MINIMIZE)

# Optimize the model
model.optimize()

if model.status == GRB.OPTIMAL:
    print("Optimal solution found!")
    
    # Print optimal office locations
    for office in offices:
        for city in cities:
            if office_city[office, city].x > 0.5:
                print(f"Office {office} should be located in {city}")
    
    # Calculate and print total benefits
    total_benefits = sum(
        benefits[city][office] * office_city[office, city].x
        for office in offices
        for city in cities
        if office_city[office, city].x > 0.5
    )
    print(f"Total Benefits: £{total_benefits}")
    
    # Calculate and print total communication costs
    total_communication_cost = sum(
        quantities_of_communication[office1][office2] * 
        costs_per_unit_of_communication[city1][city2] * 
        gamma[(office1, city1, office2, city2)].x
        for office1 in offices
        for office2 in offices
        for city1 in cities
        for city2 in cities
        # if gamma[(office1, city1, office2, city2)].x > 0.5
    )
    print(f"Total Communication Cost: £{total_communication_cost}")
    
    # Print total cost (objective value)
    print(f"Optimal total cost: £{model.objVal}")
    
else:
    print("No optimal solution found.")