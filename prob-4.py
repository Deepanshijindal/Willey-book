# import gurobipy as gp
# from gurobipy import GRB
# import pandas as pd

# # Create a new model
# model = gp.Model("Factory Planning Problem")

# # Define time periods
# periods = range(1, 7)
# products = range(1, 8)
# machines = ['Grinding', 'Vertical drilling', 'Horizontal drilling', 'Boring', 'Planing']

# # Contribution to profit
# Cont_to_profit = {
#     1: 10,
#     2: 6,
#     3: 8,
#     4: 4,
#     5: 11,
#     6: 9,
#     7: 3
# }

# # Time required for each product on each machine
# time = {
#     1: {"Grinding": 0.5, "Vertical drilling": 0.1, "Horizontal drilling": 0.2, "Boring": 0.05, "Planing": 0},
#     2: {"Grinding": 0.7, "Vertical drilling": 0.2, "Horizontal drilling": 0, "Boring": 0.03, "Planing": 0},
#     3: {"Grinding": 0, "Vertical drilling": 0, "Horizontal drilling": 0.8, "Boring": 0, "Planing": 0.01},
#     4: {"Grinding": 0, "Vertical drilling": 0.3, "Horizontal drilling": 0, "Boring": 0.07, "Planing": 0},
#     5: {"Grinding": 0.3, "Vertical drilling": 0, "Horizontal drilling": 0, "Boring": 0.1, "Planing": 0.05},
#     6: {"Grinding": 0.2, "Vertical drilling": 0.6, "Horizontal drilling": 0, "Boring": 0, "Planing": 0},
#     7: {"Grinding": 0.5, "Vertical drilling": 0, "Horizontal drilling": 0.6, "Boring": 0.08, "Planing": 0.05}
# }

# # Market limitations for each product in each month
# Limitations = {
#     1: {1: 500, 2: 1000, 3: 300, 4: 300, 5: 800, 6: 200, 7: 100},
#     2: {1: 600, 2: 500, 3: 200, 4: 0, 5: 400, 6: 300, 7: 150},
#     3: {1: 300, 2: 600, 3: 0, 4: 0, 5: 500, 6: 400, 7: 100},
#     4: {1: 200, 2: 300, 3: 400, 4: 500, 5: 200, 6: 0, 7: 100},
#     5: {1: 0, 2: 100, 3: 500, 4: 100, 5: 1000, 6: 300, 7: 0},
#     6: {1: 500, 2: 500, 3: 100, 4: 300, 5: 1100, 6: 500, 7: 60}
# }

# # Machine availability
# initial_available = {'Grinding': 4, 'Vertical drilling': 2, 'Horizontal drilling': 3, 'Boring': 1, 'Planing': 1}

# # # Downtime for maintenance
# # not_avai = {i: {j: 0 for j in machines} for i in periods}
# # not_avai[1]['Grinding'] = 1
# # not_avai[2]['Horizontal drilling'] = 2
# # not_avai[3]['Boring'] = 1
# # not_avai[4]['Vertical drilling'] = 1
# # not_avai[5]['Grinding'] = 1
# # not_avai[5]['Vertical drilling'] = 1
# # not_avai[6]['Planing'] = 1
# # not_avai[6]['Horizontal drilling'] = 1

# # Define decision variables
# manufactured = model.addVars(periods, products, name="manufactured", lb=0)
# stored = model.addVars(periods, products, name="stored", lb=0)
# sold = model.addVars(periods, products, name="sold", lb=0)
# maintenance = model.addVars(periods, machines, vtype=GRB.BINARY, name="maintenance")

# # Objective function
# model.setObjective(
#     gp.quicksum(
#         Cont_to_profit[p] * sold[t, p]
#         - 0.5 * stored[t, p]
#         for p in products
#         for t in periods
#     ),
#     GRB.MAXIMIZE
# )

# # Storage linking constraints
# for p in products:
#     model.addConstr((manufactured[1, p] - sold[1, p] - stored[1, p]) == 0, f"Link_1_{p}")
#     for t in range(2, 7):
#         model.addConstr((stored[t-1, p] + manufactured[t, p] - sold[t, p] - stored[t, p]) == 0, f"Link_{t}_{p}")
#     model.addConstr(stored[6, p] == 50, f"Final_Stock_{p}")

# # Production capacity constraints
# for t in periods:
#     for machine in machines:
#         model.addConstr(
#             gp.quicksum(
#                 (time[p][machine] if time[p][machine] is not None else 0) * manufactured[t, p]
#                 for p in products
#             ) <= 24 * 16 * (initial_available[machine] - not_avai[t][machine]),
#             f"Capacity_{machine}_{t}"
#         )

# # Market limitations
# for t in periods:
#     for p in products:
#         model.addConstr(sold[t, p] <= Limitations[t][p], f"Market_Limit_{t}_{p}")

# # Optimize the model
# model.optimize()

# # Check if the optimization was successful
# if model.status == GRB.OPTIMAL:
#     # Extract the results
#     table = ""

#     for t in periods:
#         month_str = f"\n{t}\n"
#         manufacture_str = "Manufacture "
#         sell_str = "Sell        "
#         hold_str = "Hold        "

#         for p in products:
#             if manufactured[t, p].X > 0:
#                 manufacture_str += f"{manufactured[t, p].X:.1f} PROD {p} "
#             if sold[t, p].X > 0:
#                 sell_str += f"{sold[t, p].X:.1f} PROD {p} "
#             if stored[t, p].X > 0:
#                 hold_str += f"{stored[t, p].X:.1f} PROD {p} "
        
#         if manufacture_str.strip() == "Manufacture":
#             manufacture_str += "Nothing"
#         if sell_str.strip() == "Sell":
#             sell_str += "Nothing"
#         if hold_str.strip() == "Hold":
#             hold_str += "Nothing"

#         table += f"{month_str}{manufacture_str}\n{sell_str}\n{hold_str}\n"

#     print(table)
#     print(f"Total Profit: {model.objVal}")
# else:
#     print("No optimal solution found")


import gurobipy as gp
from gurobipy import GRB
import pandas as pd

# Create a new model
model = gp.Model("Factory Planning Problem")

# Define time periods
periods = range(1, 7)
products = range(1, 8)
machines = ['Grinding', 'Vertical drilling', 'Horizontal drilling', 'Boring', 'Planing']

# Contribution to profit
Cont_to_profit = {
    1: 10,
    2: 6,
    3: 8,
    4: 4,
    5: 11,
    6: 9,
    7: 3
}

# Time required for each product on each machine
time = {
    1: {"Grinding": 0.5, "Vertical drilling": 0.1, "Horizontal drilling": 0.2, "Boring": 0.05, "Planing": 0},
    2: {"Grinding": 0.7, "Vertical drilling": 0.2, "Horizontal drilling": 0, "Boring": 0.03, "Planing": 0},
    3: {"Grinding": 0, "Vertical drilling": 0, "Horizontal drilling": 0.8, "Boring": 0, "Planing": 0.01},
    4: {"Grinding": 0, "Vertical drilling": 0.3, "Horizontal drilling": 0, "Boring": 0.07, "Planing": 0},
    5: {"Grinding": 0.3, "Vertical drilling": 0, "Horizontal drilling": 0, "Boring": 0.1, "Planing": 0.05},
    6: {"Grinding": 0.2, "Vertical drilling": 0.6, "Horizontal drilling": 0, "Boring": 0, "Planing": 0},
    7: {"Grinding": 0.5, "Vertical drilling": 0, "Horizontal drilling": 0.6, "Boring": 0.08, "Planing": 0.05}
}

# Market limitations for each product in each month
Limitations = {
    1: {1: 500, 2: 1000, 3: 300, 4: 300, 5: 800, 6: 200, 7: 100},
    2: {1: 600, 2: 500, 3: 200, 4: 0, 5: 400, 6: 300, 7: 150},
    3: {1: 300, 2: 600, 3: 0, 4: 0, 5: 500, 6: 400, 7: 100},
    4: {1: 200, 2: 300, 3: 400, 4: 500, 5: 200, 6: 0, 7: 100},
    5: {1: 0, 2: 100, 3: 500, 4: 100, 5: 1000, 6: 300, 7: 0},
    6: {1: 500, 2: 500, 3: 100, 4: 300, 5: 1100, 6: 500, 7: 60}
}

# Machine availability
initial_available = {'Grinding': 4, 'Vertical drilling': 2, 'Horizontal drilling': 3, 'Boring': 1, 'Planing': 1}

# Define decision variables
manufactured = model.addVars(periods, products, name="manufactured", lb=0)
stored = model.addVars(periods, products, name="stored", lb=0)
sold = model.addVars(periods, products, name="sold", lb=0)

# Maintenance decision variables
maintenance = model.addVars(periods, machines, vtype=GRB.BINARY, name="maintenance")

# Objective function
model.setObjective(
    gp.quicksum(
        Cont_to_profit[p] * sold[t, p]
        - 0.5 * stored[t, p]
        for p in products
        for t in periods
    ),
    GRB.MAXIMIZE
)

# Storage linking constraints
for p in products:
    model.addConstr((manufactured[1, p] - sold[1, p] - stored[1, p]) == 0, f"Link_1_{p}")
    for t in range(2, 7):
        model.addConstr((stored[t-1, p] + manufactured[t, p] - sold[t, p] - stored[t, p]) == 0, f"Link_{t}_{p}")
    model.addConstr(stored[6, p] == 50, f"Final_Stock_{p}")

# Production capacity constraints
for t in periods:
    for machine in machines:
        model.addConstr(
            gp.quicksum(
                (time[p][machine] if time[p][machine] is not None else 0) * manufactured[t, p]
                for p in products
            ) <= 24 * 16 * (initial_available[machine] - maintenance[t, machine]),
            f"Capacity_{machine}_{t}"
        )

# Market limitations
for t in periods:
    for p in products:
        model.addConstr(manufactured[t, p] <= Limitations[t][p], f"Market_Limit_{t}_{p}")

# Maintenance scheduling constraints

for machine in machines[1:]:
    model.addConstr(gp.quicksum(maintenance[t,machine] for t in periods) == initial_available[machine] , f"Maintenance_{machine}")

# Grinding machine special constraint
model.addConstr(gp.quicksum(maintenance[t, 'Grinding'] for t in periods) == 2, "Grinding_Maintenance")

# Optimize the model
model.optimize()

# Check if the optimization was successful
if model.status == GRB.OPTIMAL:
    # Extract the results
    table = ""

    for t in periods:
        month_str = f"\nMonth {t}\n"
        manufacture_str = "Manufacture "
        sell_str = "Sell        "
        hold_str = "Hold        "
        maintenance_str = "Maintenance "

        for p in products:
            if manufactured[t, p].X > 0:
                manufacture_str += f"{manufactured[t, p].X:.1f} PROD {p} "
            if sold[t, p].X > 0:
                sell_str += f"{sold[t, p].X:.1f} PROD {p} "
            if stored[t, p].X > 0:
                hold_str += f"{stored[t, p].X:.1f} PROD {p} "
        
        for machine in machines:
            if maintenance[t, machine].X > 0.5:  # Binary variable, so should be either 0 or 1
                maintenance_str += f"{machine} "

        if manufacture_str.strip() == "Manufacture":
            manufacture_str += "Nothing"
        if sell_str.strip() == "Sell":
            sell_str += "Nothing"
        if hold_str.strip() == "Hold":
            hold_str += "Nothing"
        if maintenance_str.strip() == "Maintenance":
            maintenance_str += "No Maintenance"

        table += f"{month_str}{manufacture_str}\n{sell_str}\n{hold_str}\n{maintenance_str}\n"

    print(table)
    print(f"Total Profit: {model.objVal}")
else:
    print("No optimal solution found")
