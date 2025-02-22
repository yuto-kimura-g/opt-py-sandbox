import mip
from mip import *

# Create a new model
# 1.16-pre (2025/2/22)現在、CBC, HIGHS, GUROBIはサポートされている
# CPLEXは ``we plan to support'' らしい
# ref: https://github.com/coin-or/python-mip/blob/eb3dd63cf2e6dd632ec645997c2dc49e01af3e2b/mip/constants.py#L26
# cplexを試すならdocplexかpulpでどうぞ。
# m = Model(solver_name=mip.CBC) # ok
# m = Model(solver_name=mip.HIGHS) # ok
# m = Model(solver_name=mip.CPLEX) # ng
m = Model(solver_name=mip.GUROBI) # ng
print(f"{m.solver_name=}")

# Create variables
x = m.add_var(name='x', var_type=mip.CONTINUOUS, lb=0, ub=1)
y = m.add_var(name='y', var_type=mip.CONTINUOUS, lb=0, ub=1)

# Add constraints
m.add_constr(x + y <= 1)
m.add_constr(x - y >= 1)

# Set the objective function
m.objective = maximize(x + y)

# Write the model to a file
# m.write('model.lp')

# Solve the model
m.optimize()
