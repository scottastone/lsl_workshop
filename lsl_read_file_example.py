import liesl
import matplotlib.pyplot as plt

# Read the file and extract the data
file = liesl.XDFFile('mouse.xdf')
position = file['MousePosition'].time_series
# Split by X and Y
x, y = position.T

# Plot the data
plt.scatter(x, y, marker='.')
plt.show()