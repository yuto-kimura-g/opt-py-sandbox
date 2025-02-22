import pulp
from pulp import *

# Create a new model
m = LpProblem()

# Create variables
x = LpVariable('x', lowBound=0, upBound=1, cat='Continuous')
y = LpVariable('y', lowBound=0, upBound=1, cat='Continuous')

# Add constraints
m += x + y <= 1
m += x - y >= 1

# Set the objective function
m += x + y

# Write the model to a file
# m.writeLP('model.lp')

# Solve the model
# m.solve() # ok
# m.solve(solver=PULP_CBC_CMD()) # ng ??
m.solve(solver=CPLEX()) # ok
# m.solve(solver=HiGHS()) # ok
# m.solve(solver=GUROBI()) # ok
