
# ######################################## grid format ########################
# import gurobipy as gp
# from gurobipy import GRB
# from tabulate import tabulate

# # Create a new model
# model = gp.Model("Factory Planning Problem")

# # Define time periods
# periods = range(1, 7)
# products = range(1,8)
# machines = ['Grinding',"Vertical drilling","Horizontal drilling","Boring","Planing"]

# Cont_to_profit = {
#     1: 10,
#     2: 6,
#     3: 8,
#     4: 4,
#     5: 11,
#     6: 9,
#     7: 3
# }


# time = {
#     1: {
#         "Grinding": 0.5,
#         "Vertical drilling": 0.1,
#         "Horizontal drilling": 0.2,
#         "Boring": 0.05,
#         "Planing": None
#     },
#     2: {
#         "Grinding": 0.7,
#         "Vertical drilling": 0.2,
#         "Horizontal drilling": None,
#         "Boring": 0.03,
#         "Planing": 0.01
#     },
#     3: {
#         "Grinding": None,
#         "Vertical drilling": None,
#         "Horizontal drilling": None,
#         "Boring": None,
#         "Planing": None
#     },
#     4: {
#         "Grinding": 0.3,
#         "Vertical drilling": 0.3,
#         "Horizontal drilling": None,
#         "Boring": 0.07,
#         "Planing": None
#     },
#     5: {
#         "Grinding": 0.2,
#         "Vertical drilling": None,
#         "Horizontal drilling": 0.8,
#         "Boring": 0.1,
#         "Planing": 0.05
#     },
#     6: {
#         "Grinding": 0.5,
#         "Vertical drilling": 0.6,
#         "Horizontal drilling": None,
#         "Boring": None,
#         "Planing": None
#     },
#     7: {
#         "Grinding": None,
#         "Vertical drilling": None,
#         "Horizontal drilling": 0.6,
#         "Boring": 0.08,
#         "Planing": 0.05
#     }
# }

# Limitations = {
#     1: {
#         1: 500,
#         2: 1000,
#         3: 300,
#         4: 300,
#         5: 800,
#         6: 200,
#         7: 100
#     },
#     2: {
#         1: 600,
#         2: 500,
#         3: 200,
#         4: 0,
#         5: 400,
#         6: 300,
#         7: 150
#     },
#     3: {
#         1: 300,
#         2: 600,
#         3: 0,
#         4: 0,
#         5: 500,
#         6: 400,
#         7: 100
#     },
#     4: {
#         1: 200,
#         2: 300,
#         3: 400,
#         4: 500,
#         5: 200,
#         6: 0,
#         7: 100
#     },
#     5: {
#         1: 0,
#         2: 100,
#         3: 500,
#         4: 100,
#         5: 1000,
#         6: 300,
#         7: 0
#     },
#     6: {
#         1: 500,
#         2: 500,
#         3: 100,
#         4: 300,
#         5: 1100,
#         6: 500,
#         7: 60
#     }
# }


# intial_available = {'Grinding':4,"Vertical drilling":2, "Horizontal drilling":3, "Boring":1, "Planing":1}
# # Initialize a 2D dictionary
# not_avai = {i: {j: 0 for j in range(1,6)} for i in range(1, 7)}

# # Set specific values as per the given requirements
# not_avai[1][1] = 1
# not_avai[2][3] = 2
# not_avai[3][4] = 2
# not_avai[4][2] = 1
# not_avai[5][1] = 1
# not_avai[5][2] = 1
# not_avai[6][5] = 1
# not_avai[6][3] = 1

# machine_index = range(1,7)

# # Define decision variables
# manufactured = model.addVars(periods, products, name="manufactured", lb=0)
# stored = model.addVars(periods, products, name="stored", lb=0)
# sold = model.addVars(periods, products, name="sold", lb=0)
# prod = model.addVars(periods,products, name="prod", lb=0)
# # available_machines =  model.addVars(periods,machines, name="prod", lb=0)
# # active = model.addVars(periods, machines, vtype=GRB.BINARY, name="active")

# # Objective function
# model.setObjective(
#     gp.quicksum(
#         Cont_to_profit[p] * prod[t] -
#         0.5 * gp.quicksum(stored[t, machines] for machine in machines)
#         for p in products
#         for t in periods
#     ),
#     GRB.MAXIMIZE
# )

# # per month 24 days of work with 16 hours each day, there are four grinders, two vertical drills, three horizontal drills, one borer and one planer

# # Storage linking constraints
# for t in periods:
#     for m in machine_index:
#         model.addConstr(
#             gp.quicksum(
#                 time[p][machine] * prod[t][p]
#                 for p in products
#                 for machine in machines
#             ) <= 24 * 16 * (intial_available[machine] - not_avai[t][m])
#             for machine in machines
#         )        

# for p in products:
#     # Initial constraint for month 1
#     model.addConstr((manufactured[1, p] - sold[1, p] - stored[1, p]) == 0, f"VVEG_1_{p}")
    
#     for t in range(2,6):
#         # Blending constraints for months 2 to 5
#         model.addConstr((stored[t-1, p] + manufactured[t, p] - sold[t, p] - stored[t, p]) == 0, f"VVEG_{t}_{p}")
    
#     # Final constraint for month 6
#     model.addConstr((stored[5, p] + manufactured[6, p] - sold[6, p]) == 50, f"VVEG_6_{p}")

#     for t in periods:
#         model.addConstr(manufactured[t][p]<= Limitations[t][p]) 

# # Optimize the model
# model.optimize()

# # # Print the results in the requested format
# # if model.status == GRB.OPTIMAL:
# #     print("Optimal solution found:")
    
# #     headers = ["Month", "Buy", "Use", "Store"]
# #     table = []
    
# #     for t in periods:
# #         buy_str = ""
# #         use_str = ""
# #         store_str = ""
        
# #         for oil in machines:
# #             if bought[t, oil].x > 0:
# #                 buy_str += "{}: {:.1f} tons ".format(oil, bought[t, oil].x)
# #             if manufactured[t, oil].x > 0:
# #                 use_str += "{}: {:.1f} tons ".format(oil, manufactured[t, oil].x)
# #             if stored[t, oil].x > 0:
# #                 store_str += "{}: {:.1f} tons ".format(oil, stored[t, oil].x)

# #         table.append([t, buy_str, use_str, store_str])
    
# #     print(tabulate(table, headers, tablefmt="grid"))
# #     print(f"Total Profit: {model.objVal}")
# # else:
# #     print("No optimal solution found")

##################################################################### uncomment above to see your code ##########################
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

# Downtime for maintenance
not_avai = {i: {j: 0 for j in machines} for i in periods}
not_avai[1]['Grinding'] = 1
not_avai[2]['Horizontal drilling'] = 2
not_avai[3]['Boring'] = 1
not_avai[4]['Vertical drilling'] = 1
not_avai[5]['Grinding'] = 1
not_avai[5]['Vertical drilling'] = 1
not_avai[6]['Planing'] = 1
not_avai[6]['Horizontal drilling'] = 1

# Define decision variables
manufactured = model.addVars(periods, products, name="manufactured", lb=0)
stored = model.addVars(periods, products, name="stored", lb=0)
sold = model.addVars(periods, products, name="sold", lb=0)
# maintenance = model.addVars(periods, machines, vtype=GRB.BINARY, name="maintenance")

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
            ) <= 24 * 16 * (initial_available[machine] - not_avai[t][machine]),
            f"Capacity_{machine}_{t}"
        )

# Market limitations
for t in periods:
    for p in products:
        model.addConstr(manufactured[t, p] <= Limitations[t][p], f"Market_Limit_{t}_{p}")

# Optimize the model
model.optimize()

# Check if the optimization was successful
if model.status == GRB.OPTIMAL:
    # Extract the results
    table = ""

    for t in periods:
        month_str = f"\n{t}\n"
        manufacture_str = "Manufacture "
        sell_str = "Sell        "
        hold_str = "Hold        "

        for p in products:
            if manufactured[t, p].X > 0:
                manufacture_str += f"{manufactured[t, p].X:.1f} PROD {p} "
            if sold[t, p].X > 0:
                sell_str += f"{sold[t, p].X:.1f} PROD {p} "
            if stored[t, p].X > 0:
                hold_str += f"{stored[t, p].X:.1f} PROD {p} "
        
        if manufacture_str.strip() == "Manufacture":
            manufacture_str += "Nothing"
        if sell_str.strip() == "Sell":
            sell_str += "Nothing"
        if hold_str.strip() == "Hold":
            hold_str += "Nothing"

        table += f"{month_str}{manufacture_str}\n{sell_str}\n{hold_str}\n"

    print(table)
    print(f"Total Profit: {model.objVal}")
else:
    print("No optimal solution found")
