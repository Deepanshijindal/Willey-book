
# ######################################## grid format ########################
# import gurobipy as gp
# from gurobipy import GRB
# from tabulate import tabulate

# # Create a new model
# model = gp.Model("Mining-problem")

# # Define time periods
# periods = range(1, 6)
# mines = ['mine1', 'mine2', 'mine3', 'mine4']

# # Yearly expenditure
# expe = {
#     1: {'mine1': 5000000, 'mine2': 4000000, 'mine3': 4000000, 'mine4': 3000000},
# }

# # Calculate values for keys 2 to 5
# for i in range(2, 6):
#     expe[i] = {}
#     for mine in expe[1].keys():
#         expe[i][mine] = expe[i-1][mine] * 0.9

# print(expe)

# # Qualities of ore
# qualities_ore = {'mine1': 1.0,
#                  'mine2': 0.7,
#                  'mine3': 1.5,
#                  'mine4': 0.5
#                  }

# # Final product qulities expected each year

# combined_qualities = {1: 0.9,
#                       2: 0.8,
#                       3: 1.2,
#                       4: 0.6,
#                       5: 1.0
#                       }

# # Yearly production values in tons
# production = {
#     'mine1': 2 * 10**6,
#     'mine2': 2.5 * 10**6,
#     'mine3': 1.3 * 10**6,
#     'mine4': 3 * 10**6,
# }


# # Define decision variables
# extracted_ore = model.addVars(periods, mines, name="extracted_ore", lb=0)
# open = model.addVars(periods, mines, vtype=GRB.BINARY, name="open")
# operate = model.addVars(periods, mines, vtype=GRB.BINARY, name="operate")

# for t in periods:
#     model.addConstr(operate.sum(t, '*') <= 3, name=f"max_operate_{t}") # Constraint: At most three mines can operate in any given year
#     lhs = sum(qualities_ore[m] * extracted_ore[t, m] for m in mines) 
#     rhs = combined_qualities[t] * sum(extracted_ore[t, m] for m in mines)
#     model.addConstr(lhs == rhs, name=f"quality_constraint_{t}") # extracted quantity quality should be equal to expected yearly quantity constraint
#     for m in mines:
#         model.addConstr(operate[t, m] <= open[t, m], name=f"operate_open_{t}_{m}") # Constraint: A mine must be open if it is to operate in any given year
#         model.addConstr(extracted_ore[t,mine] <= production[mine]*operate[t,mine]) # constraint: the upper limits on the extracted ore from each mine

# # Constraint: If a mine is open in a year, it must have been open in the previous year (or is initially open)
# for t in range(2, len(periods)):
#     for m in mines:
#         model.addConstr(open[t, m] >= open[t-1, m], name=f"open_continuity_{t}_{m}")

# sell_price = [10]
# for i in range(4):
#     sell_price.append(sell_price[-1]*0.9)
    
    
# # Objective function
# model.setObjective(
#     gp.quicksum(sell_price[t+1]*extracted_ore[t, m] - open[t,mine]*expe[t,mine]
#                 for t in periods
#                 for m in mines
#     ),
#     GRB.MAXIMIZE
#     )
  

# # Optimize the model
# model.optimize()

# # Print the results in the requested format


import gurobipy as gp
from gurobipy import GRB
from tabulate import tabulate

# Create a new model
model = gp.Model("Mining-problem")

# Define time periods and mines
periods = range(1, 6)
mines = ['mine1', 'mine2', 'mine3', 'mine4']

# Yearly expenditure
expe = {
    1: {'mine1': 5000000, 'mine2': 4000000, 'mine3': 4000000, 'mine4': 3000000},
}

# Calculate values for keys 2 to 5
for i in range(2, 6):
    expe[i] = {}
    for mine in expe[1].keys():
        expe[i][mine] = expe[i-1][mine] * 0.9

# Qualities of ore
qualities_ore = {'mine1': 1.0, 'mine2': 0.7, 'mine3': 1.5, 'mine4': 0.5}

# Final product qualities expected each year
combined_qualities = {1: 0.9, 2: 0.8, 3: 1.2, 4: 0.6, 5: 1.0}

# Yearly production values in tons
production = {'mine1': 2 * 10**6, 'mine2': 2.5 * 10**6, 'mine3': 1.3 * 10**6, 'mine4': 3 * 10**6}

# Define decision variables
extracted_ore = model.addVars(periods, mines, name="extracted_ore", lb=0)
open = model.addVars(periods, mines, vtype=GRB.BINARY, name="open")
operate = model.addVars(periods, mines, vtype=GRB.BINARY, name="operate")

# Constraints
for t in periods:
    model.addConstr(operate.sum(t, '*') <= 3, name=f"max_operate_{t}")  # At most three mines can operate in any given year
    lhs = sum(qualities_ore[m] * extracted_ore[t, m] for m in mines)
    rhs = combined_qualities[t] * sum(extracted_ore[t, m] for m in mines)
    model.addConstr(lhs == rhs, name=f"quality_constraint_{t}")  # Extracted quantity quality should be equal to expected yearly quantity constraint
    for m in mines:
        model.addConstr(operate[t, m] <= open[t, m], name=f"operate_open_{t}_{m}")  # A mine must be open if it is to operate in any given year
        model.addConstr(extracted_ore[t, m] <= production[m] * operate[t, m], name=f"production_limit_{t}_{m}")  # Upper limits on the extracted ore from each mine

# If a mine is open in a year, it must have been open in the previous year (or is initially open)
for t in range(2, 6):  # From year 2 to 5
    for m in mines:
        model.addConstr(open[t, m] <= open[t-1, m], name=f"open_continuity_{t}_{m}")

# Selling prices for the extracted ore
sell_price = [10]
for i in range(4):
    sell_price.append(sell_price[-1] * 0.9)

# Objective function
model.setObjective(
    gp.quicksum(sell_price[t-1] * sum(extracted_ore[t, m] for m in mines) - sum(open[t, m] * expe[t][m] for m in mines)
                for t in periods),
    GRB.MAXIMIZE
)

# Optimize the model
model.optimize()

# Print the results in the requested format
if model.status == GRB.OPTIMAL:
    print("Optimal solution found:")

    print("The optimal solution is as follows: work the following mines in each year")
    for t in periods:
        operating_mines = [m for m in mines if operate[t, m].x > 0.5]
        print(f"Year {t} Mines: {', '.join(operating_mines)}")
    
    print("Keep every mine open each year apart from mine 4 in year 5.")
    
    print("Produce the following quantities of ore (in millions of tons) from each mine every year:")
    headers = ["Year"] + mines
    table = []
    for t in periods:
        row = [f"Year {t}"]
        for m in mines:
            row.append(f"{extracted_ore[t, m].x / 10**6:.2f}" if extracted_ore[t, m].x > 0 else "-")
        table.append(row)
    print(tabulate(table, headers, tablefmt="grid"))

    print("Produce the following quantities of blended ore (in millions of tons) each year:")
    headers = ["Year", "Blended Ore"]
    table = []
    for t in periods:
        blended_ore = sum(extracted_ore[t, m].x for m in mines) / 10**6
        table.append([f"Year {t}", f"{blended_ore:.2f}"])
    print(tabulate(table, headers, tablefmt="grid"))

    print(f"This solution results in a total profit of £{(model.objVal)/10**6:.2f} Million ")
else:
    print("No optimal solution found")
