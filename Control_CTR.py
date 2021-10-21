# read data
interact_df = pd.read_csv('/Users/romain/Desktop/Data_Python_Portfolio/A:B_testing/UX AB/CrazyEgg/Homepage Version 1 - Interact, 5-29-2013/Element list Homepage Version 1 - Interact, 5-29-2013.csv')
interact_df.head()

# display total number of clicks fro the Control version
interact_df['No. clicks'].sum()

# display number of clicks for the tag name FIND
interact_df.loc[(interact_df['Name'] == 'FIND')] 
# display number of clicks for the tag name REQUEST
interact_df.loc[(interact_df['Name'] == 'REQUEST')] 
# display number of clicks for the tag name INTERACT
interact_df.loc[(interact_df['Name'] == 'INTERACT')] 
# display number of clicks for the tag name SEARCH
interact_df.loc[(interact_df['Name'] == 'Search')] 

# store number of clicks for each variations as variables
FIND = 842
REQUEST = 151
INTERACT = 42
SEARCH = 101
TOTAL_CLICK = 3714

# OTHERS = total number of clicks minus the sum of all the variation clicks
OTHERS = 3714 - (832+151+42+101)
OTHERS

# Calculate CTR for control using ctr 
ctr(INTERACT)
ctr(FIND)
ctr(REQUEST)
ctr(SEARCH)
ctr(OTHERS)


