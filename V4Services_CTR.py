# read data 
services_df = pd.read_csv('/Users/romain/Desktop/Data_Python_Portfolio/A:B_testing/UX AB/CrazyEgg/Homepage Version 5 - Services, 5-29-2013/Element list Homepage Version 5 - Services, 5-29-2013.csv')
services_df.head()

# Compute total number of clicks for the variation 1
TOTAL_CLICK = services_df['No. clicks'].sum()
TOTAL_CLICK

# FIND
services_df.loc[(services_df['Name'] == 'FIND')]
# REQUEST
services_df.loc[(services_df['Name'] == 'REQUEST')]
# SERVICES
services_df.loc[(services_df['Name'] == 'SERVICES')]
# Search
services_df.loc[(services_df['Name'] == 'Search') & (services_df['Tag name'] == 'button')]

# store number of clicks for each variations as variables
FIND = 397
REQUEST = 57
SERVICES = 45
SEARCH = 85
TOTAL_CLICK = 1348

# OTHERS
OTHERS = TOTAL_CLICK - (FIND+REQUEST+SERVICES+SEARCH)
OTHERS

# Calculate CTR
ctr(FIND)
ctr(REQUEST)
ctr(SERVICES)
ctr(SEARCH)
ctr(OTHERS)



