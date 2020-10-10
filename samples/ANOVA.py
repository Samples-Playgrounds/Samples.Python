#########
# ANOVA #
#########


# pip install statsmodels # Install the Python package Statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols # Import statsmodels api and ols
import pandas as pd
# pip install matplotlib
import matplotlib.pyplot as plt


data = pd.read_csv("Babies.csv")

# Recoding value from numeric to string
data['Age'].replace({3: 'Three', 12: 'Twelve', 24: 'Twenty-four'}, inplace= True)


mod = ols('x1 ~ Age', data=data).fit() # Set up your model
aov_table = sm.stats.anova_lm(mod, typ=2) # Carry out the ANOVA
print(aov_table) # Print the results

mod = ols('x2 ~ Age', data=data).fit() # Set up your model
aov_table = sm.stats.anova_lm(mod, typ=2) # Carry out the ANOVA
print(aov_table) # Print the results


# Create a boxplot
data.boxplot('x1', by='Age', figsize=(12, 8))
plt.show()

data.boxplot('x2', by='Age', figsize=(12, 8))
plt.show()


# Multiple comparison set
mult_comp = sm.stats.multicomp.MultiComparison(data['x1'], data['Age']) 
print(mult_comp.tukeyhsd()) # Tukey post-hoc testing, for example

mult_comp = sm.stats.multicomp.MultiComparison(data['x2'], data['Age']) 
print(mult_comp.tukeyhsd()) # Tukey post-hoc testing, for example
