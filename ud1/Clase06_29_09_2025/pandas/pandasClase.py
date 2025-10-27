import pandas as pd


data ={'Nombre':['Ana','Luis','Juan'],
       'Edad':[17,21,22],
       'Ciudad':['Madrid','Barcelona','Sevilla'],
       'Ciclo':['Daw2','Daw1','Daw1'],
       'Mayor':[False,True, True]}

df= pd.DataFrame(data)
#print(df)


print(df.iloc[0:3])
print(df.iloc[0,2])
print(df['Edad'].mean())
print(df['Edad'].max())
print(df.sort_values(by='Nombre'))
print(df.sort_values(by='Nombre', ascending=False))
resultado = df[(df['Edad']>=23) & (df['Edad']<30)]
print(resultado)
print(df[(~ df['Mayor'])])

# & and
# ~ not
#