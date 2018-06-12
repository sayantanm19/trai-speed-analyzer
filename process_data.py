import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import click

def constant_operator(df, operator, technology, save):
    states = df['LSA'].unique()
    speedsdown =[]
    speedsup = []
    f_states = []
    #print('TOTAL STATES: ' + str(len(states)))
    
    for state in states:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) & (df['Technology'] == technology)])
        down = (ttype[ttype['Test_type'] == 'download']["Data Speed(Mbps)"]).mean() #extract only download
        up =(ttype[ttype['Test_type'] == 'upload']["Data Speed(Mbps)"]).mean() #extract only upload

        #discard values if mean nan and append only the needed speeds
        if (pd.isnull(down)):
            down = 0
            up = 0
        else:
            f_states.append(state)
            speedsdown.append(down/1024) #convert to mbps
            speedsup.append(up/1024)    #convert to mbps
        if(v):            
            print('download: ' + str(down) + '  upload: ' + str(up) + ' for state: ' + str(state))

    #call plotting function    
    plot_double_bar_state(f_states, operator, speedsdown, speedsup, save)        

def constant_state(df, state, technology, save):
    operators = df['Service Provider'].unique()
    speedsdown =[]
    speedsup = []
    f_operators = []
    #print('TOTAL PROVIDERS: ' + str(len(providers)))

    for operator in operators:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) &(df['Technology'] == technology)])
        down = (ttype[ttype['Test_type'] == 'download']["Data Speed(Mbps)"]).mean() #extract only download
        up =(ttype[ttype['Test_type'] == 'upload']["Data Speed(Mbps)"]).mean()  #extract only upload
        
        #discard values if mean is nan and append only the needed speeds
        if (pd.isnull(down)):
            down = 0
            up = 0
        else:
            f_operators.append(operator)
            speedsdown.append(down/1024)
            speedsup.append(up/1024)
        if(v):            
            print('download: ' + str(down) + '  upload: ' + str(up) + ' for operator: ' + str(operator))
    #call plotting function        
    plot_double_bar_operator(f_operators, state, speedsdown, speedsup, save)
    
def plot_double_bar_state(states, operator, speedsdown, speedsup, save):
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
    plt.title('Avg. Download speed for different operators for ' + str(operator))
    plt.xticks(index + bar_width, states, rotation=90)
    plt.legend()
    plt.tight_layout()

    if (save):
        plt.savefig('stats_const_operator_' + str(operator) + '.svg')
    plt.show()

def plot_double_bar_operator(operators, state, speedsdown, speedsup, save):
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
    plt.title('Avg. Download and Upload speed for different operators for ' + str(state))
    plt.xticks(index + bar_width, operators, rotation=90)
    plt.legend()
    plt.tight_layout()

    if (save):
        plt.savefig('stats_const_operator' + str(operator) + '.svg', dpi=1000)
    plt.show()

@click.command()
@click.option('--filename', '-f', default='myspeed.csv', help='Name of the CSV file')
#@click.option('--inp','-i', prompt='Enter the option followed by operator/state', type=(int, str), help='Specifies the type of operation:\n1. Common Operator\n2. Common State\nFollowed by the common operator/state\n')
@click.option('--inp', '-i', type=int, prompt='Enter the operation:\n1.Common Operator\n2.Common State\n3.List of all States\n4.List of all Operators',
              help='Option to specify the type of operation\n1.Common Operator\n2.Common State\n3.List of all States\n4.List of all Operators')
@click.option('--common', '-c', help='Option to specify the common operator/state')
@click.option('--tech', '-t', type=click.Choice(['3G', '4G']), help='Option to specify the technology')
@click.option('--save', '-s', type=click.Choice(['0', '1']), default='0', help='Option to save the graph')
@click.option('--verbose', '-v', type=click.Choice(['0', '1']), default='0', help='Option for verbosity')


def processthis(filename, inp, common, tech, save, verbose):
    global v
    v = verbose
    if ((inp in {1,2}) & ((common is None) or (tech is None))):
        print('Common State/Operator/Technology not specified')
        exit()
    df = pd.read_csv('may18_publish.csv', header=None)
    df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
    if (inp == 1):
        constant_operator(df, common.upper(), tech, save)
    elif (inp == 2):
        constant_state(df, common.lower(), tech, save)
    elif (inp == 3):
        print(df['LSA'].unique())
    elif (inp == 4):
        print(df['Service Provider'].unique())
    else:
        print('Incorrect Options')

if __name__ == '__main__':
    processthis()

'''
v = 1
df = pd.read_csv('may18_publish.csv', header=None)
df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
#df2 = pd.read_csv('myspeed_reduced.csv')
#print(df.columns.values)
print(df.describe)
constant_operator(df, 'JIO', '4G', 'n')'''



