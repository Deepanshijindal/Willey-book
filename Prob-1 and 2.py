
######################################## grid format ########################
import gurobipy as gp
from gurobipy import GRB
from tabulate import tabulate

# Create a new model
model = gp.Model("multi_period_blending_problem")

# Define time periods
periods = range(1, 7)
oils = ['VEG1', 'VEG2', 'OIL1', 'OIL2', 'OIL3']

# Monthly costs for each oil type
costs = {
    1: {'VEG1': 110, 'VEG2': 120, 'OIL1': 130, 'OIL2': 110, 'OIL3': 115},
    2: {'VEG1': 130, 'VEG2': 130, 'OIL1': 110, 'OIL2': 90, 'OIL3': 115},
    3: {'VEG1': 110, 'VEG2': 140, 'OIL1': 130, 'OIL2': 100, 'OIL3': 95},
    4: {'VEG1': 120, 'VEG2': 110, 'OIL1': 120, 'OIL2': 120, 'OIL3': 125},
    5: {'VEG1': 100, 'VEG2': 120, 'OIL1': 150, 'OIL2': 110, 'OIL3': 105},
    6: {'VEG1': 90, 'VEG2': 100, 'OIL1': 140, 'OIL2': 80, 'OIL3': 135}
}

# Define decision variables
bought = model.addVars(periods, oils, name="bought", lb=0)
used = model.addVars(periods, oils, name="used", lb=0)
stored = model.addVars(periods, oils, name="stored", lb=0)
prod = model.addVars(periods, name="prod", lb=0)
blend = model.addVars(periods, oils, vtype=GRB.BINARY, name="blend")

# Objective function
model.setObjective(
    gp.quicksum(
        150 * prod[t] -
        gp.quicksum(costs[t][oil] * bought[t, oil] for oil in oils) -
        5 * gp.quicksum(stored[t, oil] for oil in oils)
        for t in periods
    ),
    GRB.MAXIMIZE
)

# Storage linking constraints
for t in periods:
    for oil in oils:
        if t == 1:
            model.addConstr(bought[t, oil] - used[t, oil] - stored[t, oil] == -500, f"StorageLink_{oil}_{t}")
        elif t == 6:
            model.addConstr(stored[t-1, oil] + bought[t, oil] - used[t, oil]- stored[t, oil] == 500, f"StorageLink_{oil}_{t}")
        else:
            model.addConstr(stored[t-1, oil] + bought[t, oil] - used[t, oil] - stored[t, oil] == 0, f"StorageLink_{oil}_{t}")

# Blending constraints for each month
for t in periods:
    model.addConstr(used[t, 'VEG1'] + used[t, 'VEG2'] <= 200, f"VVEG_{t}")
    model.addConstr(used[t, 'OIL1'] + used[t, 'OIL2'] + used[t, 'OIL3'] <= 250, f"NVEG_{t}")
    model.addConstr(
        8.8 * used[t, 'VEG1'] + 6.1 * used[t, 'VEG2'] + 2 * used[t, 'OIL1'] + 4.2 * used[t, 'OIL2'] + 5 * used[t, 'OIL3'] - 6 * prod[t] <= 0, f"UHRD_{t}")
    model.addConstr(
        8.8 * used[t, 'VEG1'] + 6.1 * used[t, 'VEG2'] + 2 * used[t, 'OIL1'] + 4.2 * used[t, 'OIL2'] + 5 * used[t, 'OIL3'] - 3 * prod[t] >= 0, f"LHRD_{t}")
    model.addConstr(
        gp.quicksum(used[t, oil] for oil in oils) - prod[t] == 0, f"CONT_{t}")
    
    model.addConstr(used[t, 'VEG1'] - 200*blend[t, 'VEG1'] <= 0, f"Maxusage_{t}_VEG1")
    model.addConstr(used[t, 'VEG2'] - 200*blend[t, 'VEG2'] <= 0, f"Maxusage_{t}_VEG2")
    model.addConstr(used[t, 'OIL1'] - 250*blend[t, 'OIL1'] <= 0, f"Maxusage_{t}_OIL1")
    model.addConstr(used[t, 'OIL2'] - 250*blend[t, 'OIL2'] <= 0, f"Maxusage_{t}_OIL2")
    model.addConstr(used[t, 'OIL3'] - 250*blend[t, 'OIL3'] <= 0, f"Maxusage_{t}_OIL3")
    # Constraint: Maximum 3 oils in blend
    model.addConstr(gp.quicksum(blend[t, oil] for oil in oils) <= 3, f"MaxOilInBlend_{t}")
    
    model.addConstr(2*blend[t, 'OIL3'] >= blend[t, 'VEG1'] + blend[t, 'VEG2'] , f"VEG_OIL3_{t}")
    # Constraint: Minimum 20 tons if oil is used
    for oil in oils:
        model.addConstr(used[t, oil] >= 20 * blend[t, oil], f"MinUsage_{t}_{oil}")
        

# Optimize the model
model.optimize()

# Print the results in the requested format
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    
    headers = ["Month", "Buy", "Use", "Store"]
    table = []
    
    for t in periods:
        buy_str = ""
        use_str = ""
        store_str = ""
        
        for oil in oils:
            if bought[t, oil].x > 0:
                buy_str += "{}: {:.1f} tons ".format(oil, bought[t, oil].x)
            if used[t, oil].x > 0:
                use_str += "{}: {:.1f} tons ".format(oil, used[t, oil].x)
            if stored[t, oil].x > 0:
                store_str += "{}: {:.1f} tons ".format(oil, stored[t, oil].x)

        table.append([t, buy_str, use_str, store_str])
    
    print(tabulate(table, headers, tablefmt="grid"))
    print(f"Total Profit: {model.objVal}")
else:
    print("No optimal solution found")

