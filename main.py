
#########################################################
import gurobipy as gp
from Input_data import InputData
from Decision_variables import DecisionVariables
from Constraints import Constraints
from Objective_function import ObjectiveFunction
from Results import Results


def main(id):
    # Initialize InputData with the specific question ID
    data = InputData(id)
    # print(data)
    # Create a Gurobi model
    model = gp.Model("Office Relocation")

    # Initialize DecisionVariables with the model and input data
    decision_vars = DecisionVariables(id, model, data)
    vars = decision_vars.define_decision_variables(model,data.input_fun())

    # Initialize Constraints with the model, input data, decision variables, and ID
    constraints = Constraints(id)
    constraints.add_constraints(model,data.input_fun(),vars)

    # Initialize ObjectiveFunction with the model, input data, decision variables, and ID
    objective_function = ObjectiveFunction(model, data, decision_vars, id)
    objective_function.set_objective(model,data.input_fun(),vars)

    # Optimize the model
    model.optimize()
    model.write("abc.lp")

    # Display results using Results with the model, decision variables, input data, and ID
    results = Results(model, decision_vars, data, id)
    results.display_results(model,data.input_fun(), vars)

if __name__ == "__main__":
    question_id = 19 # Set the appropriate question ID here
    main(question_id)
