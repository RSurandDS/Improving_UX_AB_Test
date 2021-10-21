# read data
help_df = pd.read_csv('/Users/romain/Desktop/Data_Python_Portfolio/A:B_testing/UX AB/CrazyEgg/Homepage Version 4 - Help, 5-29-2013/Element list Homepage Version 4 - Help, 5-29-2013.csv')
help_df.head()

# Compute total number of clicks for the variation 1
TOTAL_CLICK = help_df['No. clicks'].sum()
TOTAL_CLICK

# FIND
help_df.loc[(help_df['Name'] == 'FIND')]
# REQUEST
help_df.loc[(help_df['Name'] == 'REQUEST')]
# HELP
help_df.loc[(help_df['Name'] == 'HELP')]
# Search
help_df.loc[(help_df['Name'] == 'Search') & (help_df['Tag name'] == 'button')]

# store number of clicks for each variations as variables
FIND = 631
REQUEST = 72
HELP = 38
SEARCH = 59
TOTAL_CLICK = 1717

# OTHERS
OTHERS = 1717 - (631+72+38+59)
OTHERS

# Calculate CTR 
ctr(FIND)
ctr(REQUEST)
ctr(HELP)
ctr(SEARCH)
ctr(OTHERS)

