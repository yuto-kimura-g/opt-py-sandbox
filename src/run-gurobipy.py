import gurobipy

# Create a new model
m = gurobipy.Model()

# Create variables
x = m.addVar(lb=0, ub=1, name='x', vtype=gurobipy.GRB.CONTINUOUS)
y = m.addVar(lb=0, ub=1, name='y', vtype=gurobipy.GRB.CONTINUOUS)

# Add constraints
m.addConstr(x + y <= 1)
m.addConstr(x - y >= 1)

# Set the objective function
m.setObjective(x + y, sense=gurobipy.GRB.MAXIMIZE)

# Write the model to a file
# m.write('model.lp')

# Solve the model
m.optimize()
