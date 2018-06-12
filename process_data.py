import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = 'myspeed.csv'
df = pd.read_csv(filename)
print(list(df.columns.values))

#Important Col. Names and Techniques
#print(df.columns.values.tolist())
#print(df["Data Speed(Mbps)"].mean())
#print(df['Service Provider'].unique())
#print(df['Technology'].unique())
#print('TOTAL STATES: ' + str(len(states)))
#print('TOTAL PROVIDERS: ' + str(len(providers)))

def constant_operator(servicep, technology):

    states = df['LSA'].unique()
    speedsdown =[]
    speedsup = []
    
    for state in states:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == servicep) &(df['Technology'] == technology)])
        down = (ttype[ttype['Test_type'] == 'Download']["Data Speed(Mbps)"]).mean()
        up =(ttype[ttype['Test_type'] == 'Upload']["Data Speed(Mbps)"]).mean()

        if (pd.isnull(down)):
            down = 0
        if (pd.isnull(up)):
            up = 0
        #print(down)
        #print(up)
        speedsdown.append(down)
        speedsup.append(up)
        
    plot_double_bar_state(states, speedsdown, speedsup)
        
        

def constant_state(state, technology):
    operators = df['Service Provider'].unique()
    speedsdown =[]
    speedsup = []

    for servicep in operators:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == servicep) &(df['Technology'] == technology)])
        down = (ttype[ttype['Test_type'] == 'Download']["Data Speed(Mbps)"]).mean()
        up =(ttype[ttype['Test_type'] == 'Upload']["Data Speed(Mbps)"]).mean()

        if (pd.isnull(down)):
            down = 0
        if (pd.isnull(up)):
            up = 0
        #print(down)
        #print(up)
        speedsdown.append(down)
        speedsup.append(up)
    plot_double_bar_operator(operators, speedsdown, speedsup)
    

def plot_double_bar_state(states, speedsdown, speedsup):
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
    plt.title('Avg. Download speed for different operators for Operator')
    plt.xticks(index + bar_width, states, rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_double_bar_operator(operators, speedsdown, speedsup):
    fig, ax = plt.subplots()
    index = np.arange(len(operators))
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
     
    plt.xlabel('Service Providers')
    plt.ylabel('Average Speeds')
    plt.title('Avg. Download speed for different operators for State')
    plt.xticks(index + bar_width, operators, rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.show()

constant_operator('AIRTEL', '3G')
#plot_double_bar_state()

#constant_state('Delhi', '3G')
#plot_double_bar_servicep()


