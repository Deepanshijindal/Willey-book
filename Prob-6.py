import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("Refinery optimisation Problem")


napthas = ['Light_N','Med_N', 'Heavy_N']
crudes = ['crude_1', 'crude_2']
# oils = ['Light_oil','Heavy_oil']
fractions = ['Light_N','Med_N', 'Heavy_N','Light_oil','Heavy_oil','Residuum']
material = ['oil','gasoline']
ln_used_for = ['premium','regular','reforming_gasoline']
oil_used_in = ['jet_fuel','fuel_oil','cracking']
cracked_oil_use = ['fuel_oil','jet_fuel']
cracked_gasoline_use = ['regular','premium']
R_used_for = ['lube_oil','jet_fuel','fuel_oil']
petrols =['premium','regular']
reformed_list = ['regular','premium']
# Decision variables
Crude = model.addVars(crudes, name="Crude", lb=0)
fraction = model.addVars(fractions, name ='fraction', lb=0)
light_naptha = model.addVars(ln_used_for, name = 'light_naptha', lb=0)
medium_naptha = model.addVars(ln_used_for, name = 'medium_naptha', lb=0)
heavy_naptha = model.addVars(ln_used_for, name = 'heavy_naptha', lb=0)
# gasoline_from_naptha = model.addVars(napthas, name= 'gasoline_from_naptha', lb=0)
light_oil = model.addVars(oil_used_in, name = 'light_oil', lb = 0)
heavy_oil = model.addVars(oil_used_in, name ='heavy_oil', lb=0)
cracked_oil = model.addVars(cracked_oil_use, name= "cracked_oil", lb=0)
cracked_oil_ = model.addVar(name= 'cracked_oil_', lb=0)
cracked_gasoline_ = model.addVar(name= 'cracked_gasoline', lb=0)
cracked_gasoline = model.addVars(cracked_gasoline_use, name= "cracked_gasoline", lb=0)
Residuum = model.addVars(R_used_for, name= 'Residuum', lb=0)
lube_oil = model.addVar(name = 'lube_oil', lb=0)
fuel_oil = model.addVar(name= 'fuel_oil', lb=0)
petrol = model.addVars(petrols, name='petrol', lb=0)
Reforming_gas = model.addVar(name= 'Reforming_gas', lb=0)
Reforming_gasoline = model.addVars(reformed_list, name= 'Reforming_gasoline', lb=0)
jet_fuel = model.addVar(name = 'jet_fuel', lb=0)

# objective_function
model.setObjective(
    gp.quicksum([
        7*petrol['premium'] + 6*petrol['regular'] + 4*jet_fuel + 3.5*fuel_oil + 1.5*lube_oil]
    ),
    GRB.MAXIMIZE
)

model.addConstr(fraction['Med_N'] == sum(medium_naptha[cat] for cat in ln_used_for))
model.addConstr(fraction['Light_N'] == sum(light_naptha[cat] for cat in ln_used_for))
model.addConstr(fraction['Heavy_N']== sum(heavy_naptha[cat] for cat in ln_used_for))
model.addConstr(fraction['Light_oil']== sum(light_oil[cat] for cat in oil_used_in))
model.addConstr(fraction['Heavy_oil']== sum(heavy_oil[cat] for cat in oil_used_in))
model.addConstr(fraction['Residuum']== sum(Residuum[cat] for cat in R_used_for))


# constraints for fractions of crude2
fractions_crude2 =[0.15, 0.25, 0.18, 0.08, 0.19, 0.12]
#Constraints for fractions of crude1
fractions_crude_1 = [0.1,0.2,0.2,0.12,0.2,0.13]
for i, name in enumerate(fractions):
    model.addConstr(fraction[name]== fractions_crude_1[i]*Crude['crude_1']+ fractions_crude2[i]*Crude['crude_2'] )


# for i, name in enumerate(fractions):
#     model.addConstr(fraction[name] == fractions_crude2[i]*Crude['crude_2'])
model.addConstr(Reforming_gas == Reforming_gasoline['regular']+ Reforming_gasoline['premium'])
# 1 LN ---> 0.6 reforming_gasoline so refored gasoline obtained from LN = 0.6*barrels of light naptha
# Reforming constraints
fraction_used_for_gasoline = [0.6, 0.52, 0.45]
model.addConstr(0.6*light_naptha['reforming_gasoline'] + 0.52*medium_naptha['reforming_gasoline'] + 0.45*heavy_naptha['reforming_gasoline'] == Reforming_gas)


# Cracking constraints
oil_coeff = [0.68, 0.75]
gasoline_coeff = [0.28, 0.2]
model.addConstr(cracked_gasoline_ == sum(cracked_gasoline[cat] for cat in cracked_gasoline_use))
model.addConstr(cracked_oil_ == sum(cracked_oil[cat] for cat in cracked_oil_use))

model.addConstr(cracked_oil_ == oil_coeff[0]*light_oil['cracking'] + oil_coeff[1]*heavy_oil['cracking'] )
model.addConstr(cracked_gasoline_ == gasoline_coeff[0]*light_oil['cracking'] + gasoline_coeff[1]*heavy_oil['cracking'] )
 # Residuum used for constraint
model.addConstr(0.5*Residuum['lube_oil'] == lube_oil)

# # Ratio constraint for fuel oil
# model.addConstr(fuel_oil == 10*light_oil['fuel_oil'] + 4*cracked_oil['fuel_oil'] + 3*heavy_oil['fuel_oil'] + Residuum['fuel_oil'])

model.addConstr(Crude['crude_1']<= 20000)
model.addConstr(Crude['crude_2']<= 30000)
model.addConstr(Crude['crude_1']+ Crude['crude_2']<= 45000)
model.addConstr(light_naptha['reforming_gasoline'] + medium_naptha['reforming_gasoline'] + heavy_naptha['reforming_gasoline'] <= 10000)
model.addConstr(heavy_oil['cracking']+ light_oil['cracking'] <= 8000)
model.addConstr(lube_oil<=1000)
model.addConstr( lube_oil>= 500)
model.addConstr(petrol['premium']>= 0.4*petrol['regular'])

# for exp if we want to make a wine which is made of 4 juice then if we want to make 1 litre of wine then we will trake juices with respect to that 1 litre final value and use ratio method.
# constraints for mixture
model.addConstr(light_oil['fuel_oil'] == (10/18) *fuel_oil)
model.addConstr(cracked_oil['fuel_oil']== (4/18)* fuel_oil)
model.addConstr(heavy_oil['fuel_oil']== (3/18)* fuel_oil)
model.addConstr(Residuum['fuel_oil']== (1/18)* fuel_oil)

# petrols
for nam in petrols:
    model.addConstr(petrol[nam]== light_naptha[nam] + medium_naptha[nam] + heavy_naptha[nam] + Reforming_gasoline[nam] + cracked_gasoline[nam])
model.addConstr(petrol['regular']*84 <= 90*light_naptha['regular'] + 80*medium_naptha['regular'] + 70*heavy_naptha['regular'] + 115*Reforming_gasoline['regular'] + 105*cracked_gasoline['regular'])   
model.addConstr(petrol['premium']*94 <= 90*light_naptha['premium'] + 80*medium_naptha['premium'] + 70*heavy_naptha['premium'] + 115*Reforming_gasoline['premium'] + 105*cracked_gasoline['premium'])    
model.addConstr(jet_fuel == light_oil['jet_fuel'] + heavy_oil['jet_fuel'] + cracked_oil['jet_fuel'] + Residuum['jet_fuel'])
model.addConstr(1*light_oil['jet_fuel'] + 0.6*heavy_oil['jet_fuel'] + 1.5*cracked_oil['jet_fuel'] + 0.05*Residuum['jet_fuel'] <= 1*jet_fuel)


# Optimize the model
model.optimize()

# Check if the optimization was successful
if model.status == GRB.OPTIMAL:
    print(f"The optimal solution results in a profit of £{model.objVal:.2f}.")
    print("The optimal values of the variables defined in Part III are given below:")

    # print(f"CRA {Crude['crude_1'].X:.0f} MNPMF {medium_naptha['premium'].X:.0f}")
    # print(f"CRB {Crude['crude_2'].X:.0f} MNRMF {medium_naptha['regular'].X:.0f}")
    # print(f"LN {light_naptha['reforming_gasoline'].X:.0f} HNPMF {heavy_naptha['premium'].X:.0f}")
    # print(f"MN {medium_naptha['reforming_gasoline'].X:.0f} HNRMF {heavy_naptha['regular'].X:.0f}")
    # print(f"HN {heavy_naptha['reforming_gasoline'].X:.0f} JF {jet_fuel.X:.0f}")
    # print(f"LO {light_oil['jet_fuel'].X:.0f} FO {fuel_oil.X:.0f}")
    # print(f"HO {heavy_oil['jet_fuel'].X:.0f} LUB {lube_oil.X:.0f}")
    # print(f"RES {Residuum['jet_fuel'].X:.0f} PR {petrol['premium'].X:.0f}")
    # print(f"LNPMF {light_naptha['premium'].X:.0f} RR {petrol['regular'].X:.0f}")
    # print(f"LNRMF {light_naptha['regular'].X:.0f} ")
    # print(f"LOJF {light_oil['jet_fuel'].X:.0f} ")
    # print(f"LOFO {light_oil['fuel_oil'].X:.0f} ")
    # print(f"LOCR {light_oil['cracking'].X:.0f} ")
    # print(f"HOJF {heavy_oil['jet_fuel'].X:.0f} ")
    # print(f"HOFO {heavy_oil['fuel_oil'].X:.0f} ")
    # print(f"HOCR {heavy_oil['cracking'].X:.0f} ")
    # print(f"RESJF {Residuum['jet_fuel'].X:.0f} ")
    # print(f"RESFO {Residuum['fuel_oil'].X:.0f} ")
    # print(f"RESLB {Residuum['lube_oil'].X:.0f} ")
    # print(f"COFO {cracked_oil['fuel_oil'].X:.0f} ")
    # print(f"COJF {cracked_oil['jet_fuel'].X:.0f} ")
    # print(f"COCR {cracked_oil_.X:.0f} ")
    # print(f"CGPMF {cracked_gasoline['premium'].X:.0f} ")
    # print(f"CGRMF {cracked_gasoline['regular'].X:.0f} ")
    # print(f"CG {cracked_gasoline_.X:.0f} ")
    # print(f"REG {Reforming_gasoline['regular'].X:.0f} ")
    # print(f"REPMF {Reforming_gasoline['premium'].X:.0f} ")
    # print(f"REFG {Reforming_gas.X:.0f} ")
else:
    print("No optimal solution found.")

