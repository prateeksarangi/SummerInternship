from pandas import DataFrame, read_csv
import pandas as pd 

file = r'data.csv'
df = pd.read_csv(file)
#print(df)


background = df.Class.str.count("background").sum()
aeroplane = df.Class.str.count("aeroplane").sum()
bicycle = df.Class.str.count('bicycle').sum()
bird = df.Class.str.count('bird').sum()
boat = df.Class.str.count('boat').sum()
bottle = df.Class.str.count('bottle').sum()
bus = df.Class.str.count('bus').sum()
car = df.Class.str.count('car').sum()
cat = df.Class.str.count('cat').sum()
chair = df.Class.str.count('chair').sum()
cow = df.Class.str.count('cow').sum()
diningtable = df.Class.str.count('diningtable').sum()
dog = df.Class.str.count('dog').sum()
horse = df.Class.str.count('horse').sum()
motorbike = df.Class.str.count('motorbike').sum()
person = df.Class.str.count('person').sum()
pottedplant = df.Class.str.count('pottedplant').sum()
sheep = df.Class.str.count('sheep').sum()
sofa = df.Class.str.count('sofa').sum()
train = df.Class.str.count('train').sum()
tvmonitor = df.Class.str.count('tvmonitor').sum()


print('background: ', background)
print('aeroplane: ', aeroplane)
print('bicycle: ', bicycle)
print('bird: ', bird)
print('boat: ', boat)
print('bottle: ', bottle)
print('bus: ', bus)
print('car: ', car)
print('cat: ', cat)
print('chair: ', chair)
print('cow: ', cow)
print('diningtable: ', diningtable)
print('dog: ', dog)
print('horse: ', horse)
print('motorbike: ', motorbike)
print('person: ', person)
print('pottedplant: ', pottedplant)
print('sheep: ', sheep)
print('sofa: ', sofa)
print('train: ', train)
print('tvmonitor: ', tvmonitor)


