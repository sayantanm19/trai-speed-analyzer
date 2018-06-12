import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import click

#Important Col. Names and Techniques
#print(df.columns.values.tolist())
#print(df["Data Speed(Mbps)"].mean())
#print(df['Service Provider'].unique())
#print(df['Technology'].unique())

def constant_operator(df, operator, technology, save):
    states = df['LSA'].unique()
    speedsdown =[]
    speedsup = []
    f_states = []
    #print('TOTAL STATES: ' + str(len(states)))
    
    for state in states:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) & (df['Technology'] == technology)])
        down = (ttype[ttype['Test_type'] == 'Download']["Data Speed(Mbps)"]).mean()
        up =(ttype[ttype['Test_type'] == 'Upload']["Data Speed(Mbps)"]).mean()

        if (pd.isnull(down)):
            down = 0
            up = 0
        else:
            f_states.append(state)
            speedsdown.append(down)
            speedsup.append(up)
        if(v):            
            print('download: ' + str(down) + '  upload: ' + str(up))

        
    plot_double_bar_state(f_states, operator, speedsdown, speedsup, save)        

def constant_state(df, state, technology, save):
    operators = df['Service Provider'].unique()
    speedsdown =[]
    speedsup = []
    f_operators = []
    #print('TOTAL PROVIDERS: ' + str(len(providers)))

    for operator in operators:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) &(df['Technology'] == technology)])
        down = (ttype[ttype['Test_type'] == 'Download']["Data Speed(Mbps)"]).mean()
        up =(ttype[ttype['Test_type'] == 'Upload']["Data Speed(Mbps)"]).mean()

        if (pd.isnull(down)):
            down = 0
            up = 0
        else:
            f_operators.append(operator)
            speedsdown.append(down)
            speedsup.append(up)
            print('download: ' + str(down) + '  upload: ' + str(up))
            
    plot_double_bar_operator(f_operators, state, speedsdown, speedsup, save)
    

def plot_single_bar_x():
    index = np.arange(len(states))
    plt.bar(index, speeds)
    plt.xlabel('States', fontsize=5)
    plt.ylabel('Download Speed', fontsize=5)
    plt.xticks(index, states, fontsize=5, rotation=30)
    plt.title('Avg. Download speed for different operators for Operator')
    plt.show()

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
    plt.title('Avg. Download speed for different operators for ' + str(state))
    plt.xticks(index + bar_width, operators, rotation=90)
    plt.legend()
    plt.tight_layout()

    if (save):
        plt.savefig('stats_const_operator' + str(operator) + '.svg', dpi=1000)
    plt.show()

#constant_operator('AIRTEL', '4G')
#plot_double_bar_state()

#constant_state('Delhi', '3G')
#plot_double_bar_servicep()

@click.command()
@click.option('--filename', '-f', default='myspeed.csv', help='Name of the CSV file')
@click.option('--op', type=(int, str), help='Specifies the type of operation:\n1. Common Operator\n2. Common State\nFollowed by the common operator or state')
@click.option('--tech', '-t', prompt='Enter the technology needed', type=click.Choice(['3G', '4G']), help='Option to specify the technology')
@click.option('--save', '-s', type=click.Choice(['0', '1']), default='0', help='Option to save the graph')
@click.option('--verbose', type=click.Choice(['0', '1']), default='0', help='Option for verbosity')


def processthis(filename, op, tech, save, verbose):
    global v
    v = verbose
    '''if (verbose == 'y'):
        v = 1
    else:
        v = 0'''
    df = pd.read_csv(filename)
    if (op[0] == 1):
        constant_operator(df, op[1], tech, save)
    elif (op[0] == 2):
        constant_state(df, op[1], tech, save)
    else:
        print('Incorrect Input')
        

if __name__ == '__main__':
    processthis()


