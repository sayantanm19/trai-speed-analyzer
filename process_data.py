import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = 'may18_publish.csv'
df = pd.read_csv(filename)

#print(df.columns.values.tolist())
#print(df.loc[df['Service Provider'] == 'VODAFONE'])
#print(df["Data Speed(Mbps)"].mean())
#print(df['Service Provider'].unique())
#print(df['Technology'].unique())
#print('TOTAL STATES: ' + str(len(states)))
#print('TOTAL PROVIDERS: ' + str(len(providers)))

speedsdown = []
speedsup = []
states = df['LSA'].unique()

def process(operator):
    for state in states:
        avg_speed_down = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) & (df['Test_type'] == 'Download')]['Data Speed(Mbps)'].mean())
        if (pd.isnull(avg_speed_down)):
            avg_speed_down = 0
        speedsdown.append(avg_speed_down)
        #upload
        avg_speed_up = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) & (df['Test_type'] == 'Upload')]['Data Speed(Mbps)'].mean())
        if (pd.isnull(avg_speed_up)):
            avg_speed_up = 0
        speedsup.append(avg_speed_up)
    plot_double_bar(operator)

def plot_double_bar(op):
    fig, ax = plt.subplots()
    index = np.arange(len(states))
    bar_width = 0.35
    opacity = 0.8
     
    rects1 = plt.bar(index, speedsdown, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Download')
     
    rects2 = plt.bar(index + bar_width, speedsup, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Upload')
     
    plt.xlabel('States')
    plt.ylabel('Average Speeds')
    plt.title('Avg. Download speed for different operators for' + str(op))
    plt.xticks(index + bar_width, states, rotation=90)
    plt.legend()
     
    plt.tight_layout()
    plt.show()


process('JIO')




