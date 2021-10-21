# Bar Plot 

# creating the dataset
data = {'Services':3.34, 'Connect':2.67, 'Help':2.21,
        'Learn':1.27, 'Interact':1.13}
versions = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

plt.bar(versions, values, color ='#003f5c',
        width = 0.4)

plt.xlabel("Experiments")
plt.ylabel("Click-through Rate")
plt.title("Click-through rate - Homepage")
plt.show()