
############################################################################################
from gurobipy import GRB

class Results:
    def __init__(self, model, decision_vars, data, id):
        self.model = model
        self.decision_vars = decision_vars
        self.data = data
        self.id = id

    def display_results(self, model, data, vars):
        if model.status == GRB.OPTIMAL:
            print("Optimal solution found!")
            if self.id == 10:
                self._display_results_question_10(model,data,vars)
            elif self.id == 11.1 or self.id == 11.2 or self.id == 11.3:
                self._display_results_question_11(model,data,vars)  
            elif self.id == 13 or self.id ==13.2:
                self._display_results_question_13(model,data,vars)   
            elif self.id == 15:
                self._display_results_question_15(model,data,vars)    
            elif self.id == 19:
                self._display_results_question_19(model,data,vars)    
   

            # Add more elif statements for other questions if needed
        else:
            print("No optimal solution found.")

    def _display_results_question_10(self,model,data,vars):
        for office in data['offices']:
            for city in data['cities']:
                if vars['office_city'][office, city].x > 0.5:
                    print(f"Office {office} should be located in {city}")
        
        total_benefits = sum(
            data['benefits'][city][office] * vars['office_city'][office, city].x
            for office in data['offices']
            for city in data['cities']
            if vars['office_city'][office, city].x > 0.5
        )
        print(f"Total Benefits: £{total_benefits}")
        
        total_communication_cost = sum(
            data['quantities_of_communication'][office1][office2] * 
            data['costs_per_unit_of_communication'][city1][city2] * 
            vars['gamma'][office1, city1, office2, city2].x
            for office1 in data['offices']
            for office2 in data['offices']
            for city1 in data['cities']
            for city2 in data['cities']
        )
        print(f"Total Communication Cost: £{total_communication_cost}")
        
        print(f"Optimal total cost: £{model.objVal}")

    def _display_results_question_11(self,model,data,vars):
        a_val = vars['a']
        b_val = vars['b']
        c_val =  vars['c']
        for x in data['X']:
            print(vars['Y_cap'][x])

        y_pred = (vars['Y_cap'][x] for x in data['X'])
        print(f"The Value  of a : {a_val}")
        print(f"The value of b is : {b_val}")
        print(f"The value of b is : {c_val}")
        # print(f"The values of predicted y : {y_pred}")
        print(f"Optimal total cost: {model.objVal}")    

    def _display_results_question_13(self,model,data,vars):
        assignments = {r: vars['retailer_assign'][r].x for r in data['retailers']}
        print(f"the value : {vars['abs_delivery_points']}")
        print("Optimal assignments:", assignments)
        print(f"Optimal total cost: {model.objVal}")    

    # Define other methods for other questions as needed

    def _display_results_question_15(self, model, data, vars):
        if model.status == GRB.OPTIMAL:
            print("Optimal solution found.")
            print(f"Optimal total cost: {model.objVal}")
            for period in data['periods']:
                print(f"Period {period + 1}:")
                for i in data['types']:
                    print(f"  Type {i + 1} active generators: {vars[i + 1][period].X}")
                    print(f"  Type {i + 1} output: {vars['output_period_type'][period, i].X}")
                    print(f"  Type {i + 1} started generators: {vars[f'start_{i + 1}'][period].X}")
        else:
            print("No optimal solution found.") 
    

    def _display_results_question_19(self, model, data, vars):
        if model.status == GRB.OPTIMAL:
            print("Optimal solution found.")
            print(f"Optimal total cost: {model.objVal}")

            # Display quantities shipped from factories to depots
            print("\nQuantities shipped from factories to depots:")
            for f in data['factories']:
                for d in data['depots']:
                    if data['costs_fd'][f][d] is not None and vars['factory_depot'][f, d].X > 0:
                        print(f"  {f} to {d}: {vars['factory_depot'][f, d].X} tons")

            # Display quantities shipped from factories to customers
            print("\nQuantities shipped from factories to customers:")
            for f in data['factories']:
                for c in data['customers']:
                    if data['costs_fc'][f][c] is not None and vars['factory_customer'][f, c].X > 0:
                        print(f"  {f} to {c}: {vars['factory_customer'][f, c].X} tons")

            # Display quantities shipped from depots to customers
            print("\nQuantities shipped from depots to customers:")
            for d in data['depots']:
                for c in data['customers']:
                    if data['costs_dc'][d][c] is not None and vars['depot_customer'][d, c].X > 0:
                        print(f"  {d} to {c}: {vars['depot_customer'][d, c].X} tons")

        else:
            print("No optimal solution found.")
