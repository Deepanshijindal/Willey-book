

##################################################################### solution ###################################################################
# import gurobipy as gp
# from gurobipy import GRB

# # Create a new model
# model = gp.Model("Manpower working Problem")

# # Define time periods
# periods = range(1, 5)
# workers = ['skilled', 'semi-skilled', 'unskilled']
# retrain = ['unskilled', 'semi-skilled']
# downgrade = ['skilled-SS', 'skilled-U', 'semi-skilled-U']

# # Define decision variables
# Strength = model.addVars(periods, workers, name="Strength", lb=0)
# Recruitment = model.addVars(periods, workers, name="Recruitment", lb=0)
# Retraining = model.addVars(periods, retrain, name="Retraining", lb=0)
# Downgrading = model.addVars(periods, downgrade, name="Downgrading", lb=0)
# Redundancy = model.addVars(periods, workers, name="Redundancy", lb=0)
# short_time_working = model.addVars(periods, workers, name="short_time_working", lb=0)
# Overmanning = model.addVars(periods, workers, name="Overmanning", lb=0)

# # Objective function
# model.setObjective(
#     gp.quicksum(
#         3000*Overmanning[t, 'skilled'] + 2000*Overmanning[t, 'semi-skilled'] + 1500*Overmanning[t, 'unskilled'] + 400* Retraining[t, 'unskilled'] + 500* Retraining[t, 'semi-skilled'] + 200* Redundancy[t, 'unskilled'] + 500* Redundancy[t, 'skilled'] + 500* Redundancy[t, 'semi-skilled'] + 500* short_time_working[t,'unskilled'] + 400* short_time_working[t,'skilled'] + 400* short_time_working[t,'semi-skilled']
#         for t in periods
#     ),
#     GRB.MINIMIZE
# )

# # model.setObjective(
# #     gp.quicksum(
# #         Redundancy[t, 'skilled'] + Redundancy[t, 'semi-skilled'] + Redundancy[t, 'unskilled']
# #         for t in periods
# #     ),
# #     GRB.MINIMIZE
# # )

# # Initial workforce
# SKILLED = [1000, 1500, 2000]
# SEMI_SKILLED = [1400, 2000, 2500]
# UNSKILLED = [1000, 500, 0]

# # Continuity constraints
# for t in range(2, 5):
#     model.addConstr((0.95 * Strength[t - 1, 'skilled'] + 0.9 * Recruitment[t, 'skilled'] + 0.95 * Retraining[t, 'semi-skilled'] - Downgrading[t, 'skilled-SS'] - Downgrading[t, 'skilled-U'] - Redundancy[t, 'skilled']) == Strength[t, 'skilled'], f"Link_1_{t}")
#     model.addConstr((0.95 * Strength[t - 1, 'semi-skilled'] + 0.8 * Recruitment[t, 'semi-skilled'] + 0.95 * Retraining[t, 'unskilled'] - Retraining[t, 'semi-skilled'] + 0.5 * Downgrading[t, 'skilled-SS'] - Downgrading[t, 'semi-skilled-U'] - Redundancy[t, 'semi-skilled']) == Strength[t, 'semi-skilled'], f"Link_{t}")
#     model.addConstr((0.9 * Strength[t - 1, 'unskilled'] + 0.75 * Recruitment[t, 'unskilled'] - Retraining[t, 'unskilled'] + 0.5 * Downgrading[t, 'skilled-U'] + 0.5 * Downgrading[t, 'semi-skilled-U'] - Redundancy[t, 'unskilled']) == Strength[t, 'unskilled'], f"Link_2_{t}")

#     # Retraining semi-skilled workers
#     model.addConstr((Retraining[t, 'semi-skilled'] - 0.25 * Strength[t, 'skilled']) <= 0)

#     # Overmanning
#     model.addConstr((Overmanning[t, 'skilled'] + Overmanning[t, 'semi-skilled'] + Overmanning[t, 'unskilled']) <= 150)

# # Requirements
# for t in range(2, 5):
#     model.addConstr((Strength[t, 'skilled'] - Overmanning[t, 'skilled'] - 0.5 * short_time_working[t, 'skilled']) == SKILLED[t - 2])
#     model.addConstr((Strength[t, 'semi-skilled'] - Overmanning[t, 'semi-skilled'] - 0.5 * short_time_working[t, 'semi-skilled']) == SEMI_SKILLED[t - 2])
#     model.addConstr((Strength[t, 'unskilled'] - Overmanning[t, 'unskilled'] - 0.5 * short_time_working[t, 'unskilled']) == UNSKILLED[t - 2])

#     model.addConstr(Recruitment[t, 'skilled'] <= 500)
#     model.addConstr(Recruitment[t, 'semi-skilled'] <= 800)
#     model.addConstr(Recruitment[t, 'unskilled'] <= 500)
#     model.addConstr(Retraining[t, 'unskilled'] <= 200)
#     model.addConstr(short_time_working[t, 'skilled'] <= 50)
#     model.addConstr(short_time_working[t, 'semi-skilled'] <= 50)
#     model.addConstr(short_time_working[t, 'unskilled'] <= 50)
# model.addConstr(Strength[1, 'skilled']== 1000)
# model.addConstr(Strength[1, 'semi-skilled']== 1500)
# model.addConstr(Strength[1, 'unskilled']== 2000)

# # Optimize the model
# model.optimize()

# # Check if the optimization was successful
# if model.status == GRB.OPTIMAL:
#     # Extract the results
#     recruitment_table = "Recruitment\nUnskilled Semi-skilled Skilled\n"
#     retraining_table = "Retraining and downgrading\nUnskilled to semi-skilled Semi-skilled to skilled Semi-skilled to unskilled Skilled to unskilled Skilled to semi-skilled\n"
#     redundancy_table = "Redundancy\nUnskilled Semi-skilled Skilled\n"
#     short_time_table = "Short-time working\nUnskilled Semi-skilled Skilled\n"
#     overmanning_table = "Overmanning\nUnskilled Semi-skilled Skilled\n"
#     total_redundancy = 0

#     for t in range(2, 5):
#         recruitment_table += f"Year {t-1} {Recruitment[t, 'unskilled'].X:.0f} {Recruitment[t, 'semi-skilled'].X:.0f} {Recruitment[t, 'skilled'].X:.0f}\n"
#         retraining_table += f"Year {t-1} {Retraining[t, 'unskilled'].X:.0f} {Retraining[t, 'semi-skilled'].X:.0f} {Downgrading[t, 'semi-skilled-U'].X:.0f} {Downgrading[t, 'skilled-U'].X:.0f} {Downgrading[t, 'skilled-SS'].X:.0f}\n"
#         redundancy_table += f"Year {t-1} {Redundancy[t, 'unskilled'].X:.0f} {Redundancy[t, 'semi-skilled'].X:.0f} {Redundancy[t, 'skilled'].X:.0f}\n"
#         short_time_table += f"Year {t-1} {short_time_working[t, 'unskilled'].X:.0f} {short_time_working[t, 'semi-skilled'].X:.0f} {short_time_working[t, 'skilled'].X:.0f}\n"
#         overmanning_table += f"Year {t-1} {Overmanning[t, 'unskilled'].X:.0f} {Overmanning[t, 'semi-skilled'].X:.0f} {Overmanning[t, 'skilled'].X:.0f}\n"
#         total_redundancy += Redundancy[t, 'unskilled'].X + Redundancy[t, 'semi-skilled'].X + Redundancy[t, 'skilled'].X

#     # Print the tables
#     print("With the objective of minimizing redundancy, the optimal policies to pursue are given below:")
#     print(recruitment_table)
#     print(retraining_table)
#     print(redundancy_table)
#     print(short_time_table)
#     print(overmanning_table)
#     print(f"These policies result in a total redundancy of {total_redundancy:.0f} workers over the three years.")
# else:
#     print("No optimal solution found")

######################################################################################################################### solution-2##############


# import gurobipy as gp
# from gurobipy import GRB
# import pandas as pd
# import math

# # Create a new model
# model = gp.Model("Manpower working Problem")

# # Define time periods
# periods = range(1, 5)
# workers = ['skilled', 'semi-skilled', 'unskilled']
# retrain = ['unskilled', 'semi-skilled']
# downgrade = ['skilled-SS', 'skilled-U', 'semi-skilled-U']

# # Define decision variables
# Strength = model.addVars(periods, workers, name="Strength", lb=0, vtype= GRB.INTEGER)
# Recruitment = model.addVars(periods, workers, name="Recruitment", lb=0, vtype= GRB.INTEGER)
# Retraining = model.addVars(periods, retrain, name="Retraining", lb=0, vtype= GRB.INTEGER)
# Downgrading = model.addVars(periods, downgrade, name="Downgrading", lb=0, vtype= GRB.INTEGER)
# Redundancy = model.addVars(periods, workers, name="Redundancy", lb=0, vtype= GRB.INTEGER)
# short_time_working = model.addVars(periods, workers, name="short_time_working", lb=0, vtype= GRB.INTEGER)
# Overmanning = model.addVars(periods, workers, name="Overmanning", lb=0, vtype= GRB.INTEGER)

# # Objective function
# model.setObjective(
#     gp.quicksum(
#         3000*Overmanning[t, 'skilled'] + 2000*Overmanning[t, 'semi-skilled'] + 1500*Overmanning[t, 'unskilled'] + 400* Retraining[t, 'unskilled'] + 500* Retraining[t, 'semi-skilled'] + 200* Redundancy[t, 'unskilled'] + 500* Redundancy[t, 'skilled'] + 500* Redundancy[t, 'semi-skilled'] + 500* short_time_working[t,'unskilled'] + 400* short_time_working[t,'skilled'] + 400* short_time_working[t,'semi-skilled']
#         for t in periods
#     ),
#     GRB.MINIMIZE
# )

# # Initial workforce
# SKILLED = [1000, 1500, 2000]
# SEMI_SKILLED = [1400, 2000, 2500]
# UNSKILLED = [1000, 500, 0]

# # Continuity constraints
# for t in range(2, 5):
#     model.addConstr((0.95 * Strength[t - 1, 'skilled'] + 0.9 * Recruitment[t, 'skilled'] + 0.95 * Retraining[t, 'semi-skilled'] - Downgrading[t, 'skilled-SS'] - Downgrading[t, 'skilled-U'] - Redundancy[t, 'skilled']) == Strength[t, 'skilled'], f"Link_1_{t}")
#     model.addConstr((0.95 * Strength[t - 1, 'semi-skilled'] + 0.8 * Recruitment[t, 'semi-skilled'] + 0.95 * Retraining[t, 'unskilled'] - Retraining[t, 'semi-skilled'] + 0.5 * Downgrading[t, 'skilled-SS'] - Downgrading[t, 'semi-skilled-U'] - Redundancy[t, 'semi-skilled']) == Strength[t, 'semi-skilled'], f"Link_{t}")
#     model.addConstr((0.9 * Strength[t - 1, 'unskilled'] + 0.75 * Recruitment[t, 'unskilled'] - Retraining[t, 'unskilled'] + 0.5 * Downgrading[t, 'skilled-U'] + 0.5 * Downgrading[t, 'semi-skilled-U'] - Redundancy[t, 'unskilled']) == Strength[t, 'unskilled'], f"Link_2_{t}")

#     # Retraining semi-skilled workers
#     model.addConstr((Retraining[t, 'semi-skilled'] - 0.25 * Strength[t, 'skilled']) <= 0)

#     # Overmanning
#     model.addConstr((Overmanning[t, 'skilled'] + Overmanning[t, 'semi-skilled'] + Overmanning[t, 'unskilled']) <= 150)

# # Requirements
# for t in range(2, 5):
#     model.addConstr((Strength[t, 'skilled'] - Overmanning[t, 'skilled'] - 0.5 * short_time_working[t, 'skilled']) == SKILLED[t - 2])
#     model.addConstr((Strength[t, 'semi-skilled'] - Overmanning[t, 'semi-skilled'] - 0.5 * short_time_working[t, 'semi-skilled']) == SEMI_SKILLED[t - 2])
#     model.addConstr((Strength[t, 'unskilled'] - Overmanning[t, 'unskilled'] - 0.5 * short_time_working[t, 'unskilled']) == UNSKILLED[t - 2])

#     model.addConstr(Recruitment[t, 'skilled'] <= 500)
#     model.addConstr(Recruitment[t, 'semi-skilled'] <= 800)
#     model.addConstr(Recruitment[t, 'unskilled'] <= 500)
#     model.addConstr(Retraining[t, 'unskilled'] <= 200)
#     model.addConstr(short_time_working[t, 'skilled'] <= 50)
#     model.addConstr(short_time_working[t, 'semi-skilled'] <= 50)
#     model.addConstr(short_time_working[t, 'unskilled'] <= 50)
# model.addConstr(Strength[1, 'skilled']== 1000)
# model.addConstr(Strength[1, 'semi-skilled']== 1500)
# model.addConstr(Strength[1, 'unskilled']== 2000)

# # Optimize the model
# model.optimize()

# # Check if the optimization was successful
# if model.status == GRB.OPTIMAL:
#     # Extract the results
#     recruitment_data = {'Period': [], 'Unskilled': [], 'Semi-skilled': [], 'Skilled': []}
#     retraining_data = {'Period': [], 'Unskilled to Semi-skilled': [], 'Semi-skilled to Skilled': []}
#     downgrading_data = {'Period': [], 'Skilled to Semi-skilled': [], 'Skilled to Unskilled': [], 'Semi-skilled to Unskilled': []}
#     redundancy_data = {'Period': [], 'Unskilled': [], 'Semi-skilled': [], 'Skilled': []}
#     short_time_data = {'Period': [], 'Unskilled': [], 'Semi-skilled': [], 'Skilled': []}
#     overmanning_data = {'Period': [], 'Unskilled': [], 'Semi-skilled': [], 'Skilled': []}
#     total_redundancy = 0
#     total_cost = model.ObjVal

#     for t in range(2, 5):
#         recruitment_data['Period'].append(f"Year {t-1}")
#         recruitment_data['Unskilled'].append(Recruitment[t, 'unskilled'].X)
#         recruitment_data['Semi-skilled'].append(Recruitment[t, 'semi-skilled'].X)
#         recruitment_data['Skilled'].append(Recruitment[t, 'skilled'].X)
        
#         retraining_data['Period'].append(f"Year {t-1}")
#         retraining_data['Unskilled to Semi-skilled'].append(Retraining[t, 'unskilled'].X)
#         retraining_data['Semi-skilled to Skilled'].append(Retraining[t, 'semi-skilled'].X)
        
#         downgrading_data['Period'].append(f"Year {t-1}")
#         downgrading_data['Skilled to Semi-skilled'].append(Downgrading[t, 'skilled-SS'].X)
#         downgrading_data['Skilled to Unskilled'].append(Downgrading[t, 'skilled-U'].X)
#         downgrading_data['Semi-skilled to Unskilled'].append(Downgrading[t, 'semi-skilled-U'].X)
        
#         redundancy_data['Period'].append(f"Year {t-1}")
#         redundancy_data['Unskilled'].append(Redundancy[t, 'unskilled'].X)
#         redundancy_data['Semi-skilled'].append(Redundancy[t, 'semi-skilled'].X)
#         redundancy_data['Skilled'].append(Redundancy[t, 'skilled'].X)
        
#         short_time_data['Period'].append(f"Year {t-1}")
#         short_time_data['Unskilled'].append(short_time_working[t, 'unskilled'].X)
#         short_time_data['Semi-skilled'].append(short_time_working[t, 'semi-skilled'].X)
#         short_time_data['Skilled'].append(short_time_working[t, 'skilled'].X)
        
#         overmanning_data['Period'].append(f"Year {t-1}")
#         overmanning_data['Unskilled'].append(Overmanning[t, 'unskilled'].X)
#         overmanning_data['Semi-skilled'].append(Overmanning[t, 'semi-skilled'].X)
#         overmanning_data['Skilled'].append(Overmanning[t, 'skilled'].X)
        
#         total_redundancy += Redundancy[t, 'unskilled'].X + Redundancy[t, 'semi-skilled'].X + Redundancy[t, 'skilled'].X

#     # Create DataFrames
#     recruitment_df = pd.DataFrame(recruitment_data)
#     retraining_df = pd.DataFrame(retraining_data)
#     downgrading_df = pd.DataFrame(downgrading_data)
#     redundancy_df = pd.DataFrame(redundancy_data)
#     short_time_df = pd.DataFrame(short_time_data)
#     overmanning_df = pd.DataFrame(overmanning_data)

#     # Print DataFrames
#     print("Recruitment:")
#     print(recruitment_df)
#     print("\nRetraining:")
#     print(retraining_df)
#     print("\nDowngrading:")
#     print(downgrading_df)
#     print("\nRedundancy:")
#     print(redundancy_df)
#     print("\nShort Time Working:")
#     print(short_time_df)
#     print("\nOvermanning:")
#     print(overmanning_df)
#     print(f"\nTotal Redundant Employees: {math.ceil(total_redundancy)}")
#     print(f"Total Cost: {total_cost}")
# else:
#     print("No optimal solution found.")

# ###################################################################### part-2############################
import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("Manpower working Problem")

# Define time periods
periods = range(1, 5)
workers = ['skilled', 'semi-skilled', 'unskilled']
retrain = ['unskilled', 'semi-skilled']
downgrade = ['skilled-SS', 'skilled-U', 'semi-skilled-U']

# Define decision variables
Strength = model.addVars(periods, workers, name="Strength", lb=0)
Recruitment = model.addVars(periods, workers, name="Recruitment", lb=0)
Retraining = model.addVars(periods, retrain, name="Retraining", lb=0)
Downgrading = model.addVars(periods, downgrade, name="Downgrading", lb=0)
Redundancy = model.addVars(periods, workers, name="Redundancy", lb=0)
short_time_working = model.addVars(periods, workers, name="short_time_working", lb=0)
Overmanning = model.addVars(periods, workers, name="Overmanning", lb=0)

# Objective function
model.setObjective(
    gp.quicksum(
        3000 * Overmanning[t, 'skilled'] + 2000 * Overmanning[t, 'semi-skilled'] + 1500 * Overmanning[t, 'unskilled'] +
        400 * Retraining[t, 'unskilled'] + 500 * Retraining[t, 'semi-skilled'] +
        200 * Redundancy[t, 'unskilled'] + 500 * Redundancy[t, 'skilled'] + 500 * Redundancy[t, 'semi-skilled'] +
        500 * short_time_working[t, 'unskilled'] + 400 * short_time_working[t, 'skilled'] + 400 * short_time_working[t, 'semi-skilled']
        for t in periods
    ),
    GRB.MINIMIZE
)

# model.setObjective(
#     gp.quicksum(
#         Redundancy[t, 'skilled'] + Redundancy[t, 'semi-skilled'] + Redundancy[t, 'unskilled']
#         for t in periods
#     ),
#     GRB.MINIMIZE
# )


# Initial workforce
SKILLED = [1000, 1500, 2000]
SEMI_SKILLED = [1400, 2000, 2500]
UNSKILLED = [1000, 500, 0]

# Continuity constraints
for t in range(2, 5):
    model.addConstr((0.95 * Strength[t - 1, 'skilled'] + 0.9 * Recruitment[t, 'skilled'] + 0.95 * Retraining[t, 'semi-skilled'] - Downgrading[t, 'skilled-SS'] - Downgrading[t, 'skilled-U'] - Redundancy[t, 'skilled']) == Strength[t, 'skilled'], f"Link_1_{t}")
    model.addConstr((0.95 * Strength[t - 1, 'semi-skilled'] + 0.8 * Recruitment[t, 'semi-skilled'] + 0.95 * Retraining[t, 'unskilled'] - Retraining[t, 'semi-skilled'] + 0.5 * Downgrading[t, 'skilled-SS'] - Downgrading[t, 'semi-skilled-U'] - Redundancy[t, 'semi-skilled']) == Strength[t, 'semi-skilled'], f"Link_{t}")
    model.addConstr((0.9 * Strength[t - 1, 'unskilled'] + 0.75 * Recruitment[t, 'unskilled'] - Retraining[t, 'unskilled'] + 0.5 * Downgrading[t, 'skilled-U'] + 0.5 * Downgrading[t, 'semi-skilled-U'] - Redundancy[t, 'unskilled']) == Strength[t, 'unskilled'], f"Link_2_{t}")

    # Retraining semi-skilled workers
    model.addConstr((Retraining[t, 'semi-skilled'] - 0.25 * Strength[t, 'skilled']) <= 0)

    # Overmanning
    model.addConstr((Overmanning[t, 'skilled'] + Overmanning[t, 'semi-skilled'] + Overmanning[t, 'unskilled']) <= 150)

# Requirements
for t in range(2, 5):
    model.addConstr((Strength[t, 'skilled'] - Overmanning[t, 'skilled'] - 0.5 * short_time_working[t, 'skilled']) == SKILLED[t - 2])
    model.addConstr((Strength[t, 'semi-skilled'] - Overmanning[t, 'semi-skilled'] - 0.5 * short_time_working[t, 'semi-skilled']) == SEMI_SKILLED[t - 2])
    model.addConstr((Strength[t, 'unskilled'] - Overmanning[t, 'unskilled'] - 0.5 * short_time_working[t, 'unskilled']) == UNSKILLED[t - 2])

    model.addConstr(Recruitment[t, 'skilled'] <= 500)
    model.addConstr(Recruitment[t, 'semi-skilled'] <= 800)
    model.addConstr(Recruitment[t, 'unskilled'] <= 500)
    model.addConstr(Retraining[t, 'unskilled'] <= 200)
    model.addConstr(short_time_working[t, 'skilled'] <= 50)
    model.addConstr(short_time_working[t, 'semi-skilled'] <= 50)
    model.addConstr(short_time_working[t, 'unskilled'] <= 50)
    
model.addConstr(Strength[1, 'skilled'] == 1000)
model.addConstr(Strength[1, 'semi-skilled'] == 1500)
model.addConstr(Strength[1, 'unskilled'] == 2000)

# Optimize the model
model.optimize()

# Check if the optimization was successful
if model.status == GRB.OPTIMAL:
    # Extract the results
    recruitment_table = "Recruitment\nUnskilled Semi-skilled Skilled\n"
    retraining_table = "Retraining and downgrading\nUnskilled to semi-skilled Semi-skilled to skilled Semi-skilled to unskilled Skilled to unskilled Skilled to semi-skilled\n"
    redundancy_table = "Redundancy\nUnskilled Semi-skilled Skilled\n"
    short_time_table = "Short-time working\nUnskilled Semi-skilled Skilled\n"
    overmanning_table = "Overmanning\nUnskilled Semi-skilled Skilled\n"
    total_redundancy = 0

    for t in range(2, 5):
        recruitment_table += f"Year {t-1} {Recruitment[t, 'unskilled'].X:.0f} {Recruitment[t, 'semi-skilled'].X:.0f} {Recruitment[t, 'skilled'].X:.0f}\n"
        retraining_table += f"Year {t-1} {Retraining[t, 'unskilled'].X:.0f} {Retraining[t, 'semi-skilled'].X:.0f} {Downgrading[t, 'semi-skilled-U'].X:.0f} {Downgrading[t, 'skilled-U'].X:.0f} {Downgrading[t, 'skilled-SS'].X:.0f}\n"
        redundancy_table += f"Year {t-1} {Redundancy[t, 'unskilled'].X:.0f} {Redundancy[t, 'semi-skilled'].X:.0f} {Redundancy[t, 'skilled'].X:.0f}\n"
        short_time_table += f"Year {t-1} {short_time_working[t, 'unskilled'].X:.0f} {short_time_working[t, 'semi-skilled'].X:.0f} {short_time_working[t, 'skilled'].X:.0f}\n"
        overmanning_table += f"Year {t-1} {Overmanning[t, 'unskilled'].X:.0f} {Overmanning[t, 'semi-skilled'].X:.0f} {Overmanning[t, 'skilled'].X:.0f}\n"
        total_redundancy += Redundancy[t, 'unskilled'].X + Redundancy[t, 'semi-skilled'].X + Redundancy[t, 'skilled'].X

    # Print the tables
    print("With the objective of minimizing redundancy, the optimal policies to pursue are given below:")
    print(recruitment_table)
    print(retraining_table)
    print(redundancy_table)
    print(short_time_table)
    print(overmanning_table)
    print(f"These policies result in a total redundancy of {total_redundancy:.0f} workers over the three years.")
    print(f"The minimized cost is: {model.objVal:.2f}")
else:
    print("No optimal solution found")
