from docplex.mp.model import Model

# Create a new model
m = Model()

# Create variables
x = m.continuous_var(name='x', lb=0, ub=1)
y = m.continuous_var(name='y', lb=0, ub=1)

# Add constraints
m.add_constraint(x + y <= 1)
m.add_constraint(x - y >= 1)

# Set the objective function
m.maximize(x + y)

# Write the model to a file
# m.export_as_lp('model.lp')
# m.export_as_mps('model.mps')

# Solve the model
m.solve()
