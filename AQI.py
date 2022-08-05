import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Line Graph

gas = pd.read_csv('600 data day5.csv')
#print(gas)
plt.figure(figsize=(8,5))

plt.title('AQI plot')
plt.plot(gas['Sample'],gas['PM(2.5)'],'b.-',label = 'PM2.5', )
plt.plot(gas['Sample'],gas['HCHO'],'r.-',label = 'HCHO')
plt.plot(gas['Sample'],gas['TVOC'],'y.-',label = 'TVOC')

plt.plot(gas['Sample'],gas['TEMP'],'g.-',label = 'TEMP')


#or we can set up a loop and loop through all the countries
'''for quality in gas:
    if quality != 'Sample':
        plt.plot(gas.Sample,gas[quality],marker='.')
'''


#print(gas.Year[::3]) #skips every 3 years to make it easier to read graph
plt.xticks(gas.Sample[::3])


plt.legend()

plt.show()


#PieCharts


plt.style.use('ggplot')


light = gas.loc[gas.Weight < 125].count()[0]
light_medium = gas.loc[(gas.Weight >= 125) & (gas.Weight < 150)].count()[0]
medium = gas.loc[(gas.Weight >= 150) & (gas.Weight < 175)].count()[0]
medium_heavy = gas.loc[(gas.Weight >= 175) & (gas.Weight < 200)].count()[0]
heavy = gas.loc[gas.Weight > 200].count()[0]


weights = [light,light_medium,medium,medium_heavy,heavy]

label = ['Under 125','125-150','150-175','175-200','Over 200']

