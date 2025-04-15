import matplotlib.pyplot as plt

# Create empty lists
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

# Generate data
for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.5 ** i)  # You can try 2 ** i as well

# Plot the data
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

# Label the axes
plt.xlabel('Sample Points')
plt.ylabel('Function Value')

# Add a title
plt.title('Different Orders of Growth')

# Add a legend
plt.legend(['Linear', 'Quadratic', 'Cubic', 'Exponential'])

# Show the plot
plt.show()
