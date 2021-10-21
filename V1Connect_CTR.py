# read data
connect_df = pd.read_csv('/Users/romain/Desktop/Data_Python_Portfolio/A:B_testing/UX AB/CrazyEgg/Homepage Version 2 - Connect, 5-29-2013/Element list Homepage Version 2 - Connect, 5-29-2013.csv')
connect_df.head()

# Compute total number of clicks for the variation 1
connect_df['No. clicks'].sum()

# FIND
connect_df.loc[(connect_df['Name'] == 'FIND')]
# REQUEST
connect_df.loc[(connect_df['Name'] == 'REQUEST')]
# CONNECT
connect_df.loc[(connect_df['Name'] == 'CONNECT')]
# SEARCH
connect_df.loc[(connect_df['Name'] == 'Search')]

# store number of clicks for each variations as variables
FIND = 502
REQUEST = 57
CONNECT = 53
SEARCH = 47
TOTAL_CLICK = 1587

# OTHERS
OTHERS = TOTAL_CLICK - (FIND+REQUEST+CONNECT+SEARCH)
OTHERS

# Calculate CTR 
ctr(FIND)
ctr(REQUEST)
ctr(CONNECT)
ctr(SEARCH)
ctr(OTHERS)
