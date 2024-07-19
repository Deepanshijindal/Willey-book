
####################################################################
import gurobipy as gp
class ObjectiveFunction:
    def __init__(self, model, data, decision_vars, id):
        model = model
        self.data = data
        self.decision_vars = decision_vars
        self.id = id

    def set_objective(self, model, data, vars):
        if self.id == 10:
            self._set_objective_question_10(model,data,vars)
        if self.id == 11.1 :
            self._set_objective_question_11_1(model,vars)
        if self.id == 11.2 or self.id ==11.3:
            self._set_objective_question_11_2(model,vars)  
        if self.id ==13:
            self._set_objective_question_13(model,vars)
        if self.id == 13.2:
            self._set_objective_question_13_2(model,vars)   
        if self.id == 15:
            self._set_objective_question_15(model, data, vars)   
        if self.id == 19:
            self._set_objective_question_19(model, data, vars)      



        # Add more elif statements for other questions if needed

    def _set_objective_question_10(self,model,data,vars):
        objective = -gp.quicksum(
            data['benefits'][city][office] * vars['office_city'][office, city]
            for city in data['cities'] for office in data['offices']
        ) + gp.quicksum(
            data['quantities_of_communication'][office1][office2] *
            data['costs_per_unit_of_communication'][city1][city2] *
            vars['gamma'][office1, city1, office2, city2]
            for office1 in data['offices'] for office2 in data['offices']
            for city1 in data['cities'] for city2 in data['cities']
        )
        model.setObjective(objective, gp.GRB.MINIMIZE)

    # def _set_objective_question_11(self):
    #     objective = gp.quicksum((y- vars['Y_cap'])
    #                             for y in data['Y'])   

    #     model.setObjective(objective, gp.GRB.MINIMIZE) 
    
    def _set_objective_question_11_2(self,model,vars):
        objective = vars['max_dev']
        model.setObjective(objective, gp.GRB.MINIMIZE)

    def _set_objective_question_11_1(self, model, vars):
        objective = gp.quicksum(vars['abs_dev'][x] for x in range(19))
        model.setObjective(objective, gp.GRB.MINIMIZE)

    def _set_objective_question_13(self, model, vars):
        objective = (vars['abs_delivery_points'] + vars['abs_spirit'] + vars['abs_oil_R1'] + vars['abs_oil_R2'] + vars['abs_oil_R3'] + vars['abs_group_A'] + vars['abs_group_B'])
        model.setObjective(objective, gp.GRB.MINIMIZE)

    def _set_objective_question_13_2(self, model, vars):
        objective = (vars['max_deviation'])
        model.setObjective(objective, gp.GRB.MINIMIZE)        

    def _set_objective_question_13_2(self, model, vars):
        objective = (vars['max_deviation'])
        model.setObjective(objective, gp.GRB.MINIMIZE) 

    def _set_objective_question_15(self, model, data, vars):
            # Objective function: Minimize total cost
        # objective = gp.quicksum(
        #     data['property'][i]['Cost per hour per megawatt above minimum'] * (vars['output_period_type'][period, i] - data['property'][i]['Minimum level'] * vars[k][period] * data['durations'][j]) +
        #     data['property'][i]['Cost per hour at minimum'] * data['durations'][j] * vars[k][period] +
        #     data['property'][i]['Cost'] * vars['start_{k}'][period]
        #     for i in data['types']
        #     for j in data['durations']
        #     for period in data['periods']
        #     for k in range(1,4)
        # )     
        objective = gp.quicksum(
        data['property'][i]['Cost per hour per megawatt above minimum'] * (vars['output_period_type'][period, i] - data['property'][i]['Minimum level'] * vars[i+1][period] * data['durations'][period])+
        data['property'][i]['Cost per hour at minimum'] * data['durations'][period] * vars[i+1][period] +
        data['property'][i]['Cost'] * vars[f'start_{i+1}'][period]
        for i in data['types']
        for period in data['periods']
        )
    
        model.setObjective(objective, gp.GRB.MINIMIZE)     

    def _set_objective_question_19(self,model,data,vars):
        total_cost = 0.0
        # Cost from factories to depots
        for f in data['factories']:
            for d in data['depots']:
                if data['costs_fd'][f][d] is not None:
                    total_cost += data['costs_fd'][f][d] * vars['factory_depot'][f, d]

        # Cost from factories to customers
        for f in data['factories']:
            for c in data['customers']:
                if data['costs_fc'][f][c] is not None:
                    total_cost += data['costs_fc'][f][c] * vars['factory_customer'][f, c]

        # Cost from depots to customers
        for d in data['depots']:
            for c in data['customers']:
                if data['costs_dc'][d][c] is not None:
                    total_cost += data['costs_dc'][d][c] * vars['depot_customer'][d, c]

        # Set objective to minimize total distribution cost
        model.setObjective(total_cost, gp.GRB.MINIMIZE)