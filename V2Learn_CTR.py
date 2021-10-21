# read data
learn_df = pd.read_csv('/Users/romain/Desktop/Data_Python_Portfolio/A:B_testing/UX AB/CrazyEgg/Homepage Version 3 - Learn, 5-29-2013/Element list Homepage Version 3 - Learn, 5-29-2013.csv')
learn_df.head()

# Compute total number of clicks for the variation 1
TOTAL_CLICK = learn_df['No. clicks'].sum()
TOTAL_CLICK

# FIND
learn_df.loc[(learn_df['Name'] == 'FIND')]
# REQUEST
learn_df.loc[(learn_df['Name'] == 'REQUEST')]
# LEARN
learn_df.loc[(learn_df['Name'] == 'LEARN')]
# Search
learn_df.loc[(learn_df['Name'] == 'Search') & (learn_df['Tag name'] == 'button')]

# store number of clicks for each variations as variables
FIND = 587
REQUEST = 63
LEARN = 21
SEARCH = 50

# OTHERS
OTHERS = 1652 - (587+63+21+50)
OTHERS

# Calculate CTR 
ctr(FIND)
ctr(REQUEST)
ctr(LEARN)
ctr(SEARCH)
ctr(OTHERS)