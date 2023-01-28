'''from Load_data import Load_data
data = []
dataset = Load_data.get_data(Load_data,'dataset/data.csv')
print(dataset)'''
from Load_data import Load_data

import pandas as pd

df = pd.read_csv('data_credit.csv')
df.pop('Unnamed: 0')
print(df.columns)
print(df)
print(df.shape)
data_train = df[:800]
print(len(data_train))
data_tes = df[-200:]
print(len(data_tes))
print(data_tes)
print(data_train)

data_tes.to_csv("data_credit_uji.csv")
data_train.to_csv("data_credit_latih.csv")
'''k = 2

def tes1():
    temp = 0
    for i in range(10):
        temp+=i
        print(temp)
    print("halo")
    return temp
print(tes1())
def tes2():
    b = tes1()
    return b+10
print(tes2())
'''
'''data_mentah = Load_data.get_data(Load_data,'dataset/data_uji.csv')

# mencari nilai maksimum setiap kolom


# Melakukan normalisasi data menggunakan nilai minimum dan maksimum
data_normalisasi = Load_data.preproses(Load_data, data_mentah)
print(len(data_mentah[0]))

prediksi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(len(prediksi))

for x in range(len(data_mentah)):
    data_mentah[x].append(prediksi[x])
    print(data_mentah[x])
print(len(data_mentah[0]))

import pandas as pd
df = pd.read_csv('dataset/data_uji.csv')
df_tes = df.head()
prediksi = [1,1,0,1,0]
df.pop('Unnamed: 0')
print(df_tes)
df2 = df_tes.assign(prediksi=prediksi)
print(df2)

row = 0
print("tessssss")

print(df2.columns)
for x in range(len(df2)):
    for y in range(len(df2.columns)):
        print(df2[x][y])'''


