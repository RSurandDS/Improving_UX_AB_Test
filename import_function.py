# import libraries
import pandas as pd 
import matplotlib.pyplot as plt


# define function to calculate the clickthrough rate

# var = number of click on the variations
# TOTAL_CLICK = number of total users who view the variation page

def ctr(var):
	return round((var/TOTAL_CLICK)*100, 1)

