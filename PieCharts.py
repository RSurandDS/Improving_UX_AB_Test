# Interact - CONTROL

# The slices will be ordered and plotted counter-clockwise.
labels = ['Find (22.4%)', r'Request (4.1%)', 
r'Interact (1.1%)', r'Search (2.7%)', r'Others (69.7%)']
sizes = [22.4,4.1,1.1,2.7,69.7]
colors = ['#003f5c','#58508d','#bc5090','#ff6361','#ffa600']
explode = (0,0,0.5,0,0)

plt.figure(figsize=(7,7), dpi=72)
plt.pie(sizes,colors=colors,startangle = 90, shadow=False, explode = explode, autopct='%1.0f%%', pctdistance=1.1)
plt.legend(labels,loc='upper right')

plt.title('Click-Through-Rates - Homepage, Interact')
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()
plt.show()


# ------------------------------

# Version 1 - CONNECT

# The slices will be ordered and plotted counter-clockwise.
labels = ['Find (31.6%)', r'Request (3.6%)', 
r'Connect (3.3%)', r'Search (3.0%)', r'Others (58.5%)']
sizes = [31.6,3.6,3.3,3.0,58.5]
colors = ['#003f5c','#58508d','#bc5090','#ff6361','#ffa600']
explode = (0,0,0.5,0,0)

plt.figure(figsize=(7,7), dpi=72)
plt.pie(sizes,colors=colors,startangle = 90, shadow=False, explode = explode, autopct='%1.0f%%', pctdistance=1.1)
plt.legend(labels,loc='upper right')

plt.title('Click-Through-Rates - Homepage, Connect')
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()
plt.show()



# ------------------------------

# Version 2 - LEARN

# The slices will be ordered and plotted counter-clockwise.
labels = ['Find (35.5%)', r'Request (3.8%)', 
r'Learn (1.3%)', r'Search (3.0%)', r'Others (56.4%)']
sizes = [35.5,3.8,1.3,3.0,56.4]
colors = ['#003f5c','#58508d','#bc5090','#ff6361','#ffa600']
explode = (0,0,0.5,0,0)

plt.figure(figsize=(7,7), dpi=72)
plt.pie(sizes,colors=colors,startangle = 90, shadow=False, explode = explode, autopct='%1.0f%%', pctdistance=1.1)
plt.legend(labels,loc='upper right')
plt.title('Click-Through-Rates - Homepage, Learn')
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()
plt.show()



# ------------------------------

# Version 3 - HELP


# The slices will be ordered and plotted counter-clockwise.
labels = ['Find (36.8%)', r'Request (4.2%)', 
r'Help (2.2%)', r'Search (3.4%)', r'Others (53.5%)']
sizes = [36.8,4.2,2.2,3.4,53.4]
colors = ['#003f5c','#58508d','#bc5090','#ff6361','#ffa600']
explode = (0,0,0.5,0,0)

plt.figure(figsize=(7,7), dpi=72)
plt.pie(sizes,colors=colors,startangle = 90, shadow=False, explode = explode, autopct='%1.0f%%', pctdistance=1.1)
plt.legend(labels,loc='upper right')

plt.title('Click-Through-Rates - Homepage, Help')
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()

plt.show()



# ------------------------------

# Version 4 - SERVICES


# The slices will be ordered and plotted counter-clockwise.
labels = ['Find (29.5%)', r'Request (4.2%)', 
r'Services (3.3%)', r'Search (6.3%)', r'Others (56.7%)']
sizes = [29.5,4.2,3.3,6.3,56.7]
colors = ['#003f5c','#58508d','#bc5090','#ff6361','#ffa600']
explode = (0,0,0.5,0,0)

plt.figure(figsize=(7,7), dpi=72)
plt.pie(sizes,colors=colors,startangle = 90, shadow=False, explode = explode, autopct='%1.0f%%', pctdistance=1.1)
plt.legend(labels,loc='upper right')

plt.title('Click-Through-Rates - Homepage, Services')
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.tight_layout()
plt.show()



