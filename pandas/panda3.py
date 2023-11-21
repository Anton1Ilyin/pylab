import pandas as pd

s=set()
dfs=pd.read_excel('students_info.xlsx')
dfe=pd.read_html('results_ejudge.html')
print(dfs)
print(dfe)
df=pd.merge(dfs,dfe)
print(df)
