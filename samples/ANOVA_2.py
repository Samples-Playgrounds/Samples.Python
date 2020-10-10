###########
# ANOVA 2 #
###########

from pyvttbl import DataFrame

df=DataFrame()
df.read_tbl("Babies.csv")
aov_pyvttbl = df.anova1way('x1', 'Age')
print aov_pyvttbl