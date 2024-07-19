
##############################################################
from gurobipy import GRB

class DecisionVariables:
    def __init__(self, id, model, data):
        self.id = id
        self.model = model
        self.data = data

    def define_decision_variables(self,model,data):
        var = {}
        if self.id == 10:
            var['office_city'] = model.addVars(data['offices'], data['cities'], vtype=GRB.BINARY, name='office_city')
            var['gamma'] = model.addVars(data['offices'], data['cities'], data['offices'], data['cities'], vtype=GRB.BINARY, name='gamma')

        elif  self.id == 11.1 :
            var['Y_cap'] = model.addVars(data['X'], vtype = GRB.CONTINUOUS, name = 'Y_cap')
            var['a'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'a')
            var['b'] = model.addVar(vtype = GRB. CONTINUOUS, name = 'b')
            var['abs_dev'] = [model.addVar(vtype = GRB. CONTINUOUS, name = 'abs{i}') for i in range(19)]
            var['c'] = model.addVar(vtype = GRB. CONTINUOUS, name = 'c', lb = -GRB.INFINITY)


        elif self.id ==11.2 or self.id ==11.3:
            var['a'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'a', lb = -GRB.INFINITY)
            var['b'] = model.addVar(vtype = GRB. CONTINUOUS, name = 'b', lb = -GRB.INFINITY)    
            var['Y_cap'] = model.addVars(data['X'], vtype = GRB.CONTINUOUS, name = 'Y_cap')                          
            var['max_dev'] = model.addVar(vtype = GRB.CONTINUOUS, lb =0, name = 'max_dev')
            var['c'] = model.addVar(vtype = GRB. CONTINUOUS, name = 'c', lb = -GRB.INFINITY)

        elif self.id == 13:
            var['retailer_assign'] = model.addVars(data['retailers'], vtype = GRB.BINARY, name = 'retailer_assign')
            var['abs_delivery_points'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_delivery_point', lb=0, ub=0.05)
            var['abs_spirit'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_spirit', lb=0, ub = 0.05)
            var['abs_oil_R1'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_oil_R1',lb=0, ub = 0.05)    
            var['abs_oil_R2'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_oil_R2',lb=0, ub = 0.05) 
            var['abs_oil_R3'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_oil_R3',lb=0, ub = 0.05)    
            var['abs_group_A'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_group_A',lb=0, ub = 0.05)     
            var['abs_group_B'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_group_B',lb=0, ub = 0.05)  

        elif self.id == 13.2:
            var['retailer_assign'] = model.addVars(data['retailers'], vtype = GRB.BINARY, name = 'retailer_assign')
            var['abs_delivery_points'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_delivery_point', lb=0, ub=0.05)
            var['abs_spirit'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_spirit', lb=0, ub = 0.05)
            var['abs_oil_R1'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_oil_R1',lb=0, ub = 0.05)    
            var['abs_oil_R2'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_oil_R2',lb=0, ub = 0.05) 
            var['abs_oil_R3'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_oil_R3',lb=0, ub = 0.05)    
            var['abs_group_A'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_group_A',lb=0, ub = 0.05)     
            var['abs_group_B'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'abs_group_B',lb=0, ub = 0.05)  
            var['max_deviation'] = model.addVar(vtype = GRB.CONTINUOUS, name = 'max_deviation', lb=0, ub = 0.05)

        # elif self.id == 14:
        #     var['select_box'] = model.addVars(30, vtype=GRB.BINARY, name="select_box")
        elif self.id == 15:
            var[1] = model.addVars(data['periods'],vtype=GRB.INTEGER, lb=0, ub=12, name= 'active_type_1') # Number of type 1 generator active by period
            var[2] = model.addVars(data['periods'],vtype=GRB.INTEGER, lb=0, ub=10, name= 'active_type_2') # Number of type 2 generator active by period
            var[3] = model.addVars(data['periods'],vtype=GRB.INTEGER, lb=0, ub=5, name= 'active_type_3')  # Number of type 3 generator active by period
            var['output_period_type'] = model.addVars(data['periods'], data['types'], name='output_period_type') # Output from every type of generator by period

            var['start_1'] = model.addVars(data['periods'], vtype=GRB.INTEGER, lb=0, ub=12, name= 'start_type_1') 
            var['start_2'] = model.addVars(data['periods'], vtype=GRB.INTEGER, lb=0, ub=10, name= 'start_type_2')
            var['start_3'] = model.addVars(data['periods'], vtype=GRB.INTEGER, lb=0, ub=5, name= 'start_type_3')

        elif self.id == 19:
            # variable factory_depot will define quantity served from factory to depot 
            var['factory_depot'] = model.addVars(data['factories'], data['depots'], lb=0, name= 'factory_depot_quantities')
            # variable factory_customer will define quantity served from factory to customer
            var['factory_customer'] = model.addVars(data['factories'], data['customers'], lb=0, name= 'factory_customer_quantities')
            # variable depot_customer will define quantity served from depot to customer
            var['depot_customer'] = model.addVars(data['depots'], data['customers'], lb=0, name= 'depot_customer_quantities')
            # Apply upper bounds based on infeasible routes and set objective coefficients
            for f in data['factories']:
                for d in data['depots']:
                    if data['costs_fd'][f][d] is None:
                        var['factory_depot'][f, d].ub = 0

            for f in data['factories']:
                for c in data['customers']:
                    if data['costs_fc'][f][c] is None:
                        var['factory_customer'][f, c].ub = 0

            for d in data['depots']:
                for c in data['customers']:
                    if data['costs_dc'][d][c] is None:
                        var['depot_customer'][d, c].ub = 0
        return var 