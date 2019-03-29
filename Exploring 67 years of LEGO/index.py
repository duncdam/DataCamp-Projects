import pandas as pd
number = [1,2,3,4,3,4,1,2]
alpha = ['a','b','c','d','a','b','c','d']

ab_list = list(zip(number,alpha)) 
# print(ab_list)

df = pd.DataFrame(ab_list)
# print(df)
# print(df)

df.index.name = 'Index number'
df.columns =['number', 'alpha']
# print(df)

# print(df[1:0:-1])
# print(df[2:1:-1])
# print(df[:2:1])
# print(df[:7:3])

df['new_col'] = df['number'].astype('str') + df['alpha']
# print (df)


df['country'] = ['Vietnam', 'USA', 'Thailand', 'Australia', 'UK', 'Scotland', 'Ireland', 'Madagascar']
# print(df)

df = df.set_index(['number','alpha'])
print(df)



