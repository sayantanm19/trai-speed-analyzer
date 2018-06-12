import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import click

def constant_operator_compare(df, df2, operator, technology, save):
    states = df['LSA'].unique()
    speedsdown =[]
    speedsup = []
    speedsdown2 = []
    speedsup2 = []
    f_states = []
    
    #print('TOTAL STATES: ' + str(len(states)))
    
    for state in states:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) & (df['Technology'] == technology)])
        ttype2 = (df2[(df2['LSA'] == state) & (df2['Service Provider'] == operator) & (df2['Technology'] == technology)])
        #Used for inconsistencies
        down = (ttype[ttype['Test_type'] == 'download']["Data Speed(Mbps)"]).mean() #extract only download
        up =(ttype[ttype['Test_type'] == 'upload']["Data Speed(Mbps)"]).mean() #extract only upload
        down2 = (ttype2[ttype2['Test_type'] == 'download']["Data Speed(Mbps)"]).mean() #extract only download
        up2 =(ttype2[ttype2['Test_type'] == 'upload']["Data Speed(Mbps)"]).mean() #extract only upload

        #discard values if mean nan and append only the needed speeds
        if (pd.isnull(down)):
            down = 0
            up = 0
        else:
            f_states.append(state)
            speedsdown.append(down)
            speedsup.append(up)
            speedsdown2.append(down2)
            speedsup2.append(up2)
        if(v):            
            print('download: ' + str(down) + '  upload: ' + str(up) + ' for state: ' + str(state))
            print('download: ' + str(down2) + '  upload: ' + str(up2) + ' for state: ' + str(state))


    #call plotting function    
    plot_double_bar_state_comp(f_states, operator, speedsdown, speedsup, speedsdown2, speedsup2, save)

def constant_state_compare(df, df2, state, technology, save):
    operators = df['Service Provider'].unique()
    speedsdown =[]
    speedsup = []
    speedsdown2 = []
    speedsup2 = []
    f_operators = []
    
    #print('TOTAL STATES: ' + str(len(states)))
    
    for operator in operators:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) & (df['Technology'] == technology)])
        ttype2 = (df2[(df2['LSA'] == state) & (df2['Service Provider'] == operator) & (df2['Technology'] == technology)])
        #Used for inconsistencies
        down = (ttype[ttype['Test_type'] == 'download']["Data Speed(Mbps)"]).mean() #extract only download
        up =(ttype[ttype['Test_type'] == 'upload']["Data Speed(Mbps)"]).mean() #extract only upload
        down2 = (ttype2[ttype2['Test_type'] == 'download']["Data Speed(Mbps)"]).mean() #extract only download
        up2 =(ttype2[ttype2['Test_type'] == 'upload']["Data Speed(Mbps)"]).mean() #extract only upload

        #discard values if mean nan and append only the needed speeds
        if (pd.isnull(down)):
            down = 0
            up = 0
        else:
            f_operators.append(operator)
            speedsdown.append(down)
            speedsup.append(up)
            speedsdown2.append(down2)
            speedsup2.append(up2)
        if(v):            
            print('download: ' + str(down) + '  upload: ' + str(up) + ' for state: ' + str(state))
            print('download: ' + str(down2) + '  upload: ' + str(up2) + ' for state: ' + str(state))


    #call plotting function    
    plot_double_bar_state_comp(f_operators, state, speedsdown, speedsup, speedsdown2, speedsup2, save)

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
            speedsdown.append(down)
            speedsup.append(up)
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
        down = (ttype[ttype['Test_type'] == 'Download']["Data Speed(Mbps)"]).mean() #extract only download
        up =(ttype[ttype['Test_type'] == 'Upload']["Data Speed(Mbps)"]).mean()  #extract only upload
        
        #discard values if mean is nan and append only the needed speeds
        if (pd.isnull(down)):
            down = 0
            up = 0
        else:
            f_operators.append(operator)
            speedsdown.append(down)
            speedsup.append(up)
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
    plt.title('Avg. Download and Upload speed for different operators for ' + str(operator))
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

def plot_double_bar_state_comp(states, operator, speedsdown, speedsup, speedsdown2, speedsup2, save):
    fig, ax = plt.subplots()
    index = np.arange(len(states))
    bar_width = 0.2
    opacity = 0.8
     
    rects1 = plt.bar(index, speedsdown, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Download')
     
    rects2 = plt.bar(index + bar_width, speedsup, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Upload')

    rects3 = plt.bar(index + 2 * bar_width, speedsdown2, bar_width,
                     alpha=opacity,
                     color='y',
                     label='Download')
    rects4 = plt.bar(index + 3 * bar_width, speedsup2, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Upload')
    plt.xlabel('States')
    plt.ylabel('Average Speeds')
    plt.title('Avg. Download and Upload speed for different operators for ' + str(operator))
    plt.xticks(index + bar_width, states, rotation=90)
    plt.legend()
    plt.tight_layout()

    if (save):
        plt.savefig('stats_const_operator_' + str(operator) + '.svg')
    plt.show()

def plot_double_bar_operator_comp(operators, state, speedsdown, speedsup, speedsdown2, speedsup2, save):
    fig, ax = plt.subplots()
    index = np.arange(len(operators))
    bar_width = 0.2
    opacity = 0.8
     
    rects1 = plt.bar(index, speedsdown, bar_width,
                     alpha=opacity,
                     color='b',
                     label='Download')
     
    rects2 = plt.bar(index + bar_width, speedsup, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Upload')

    rects3 = plt.bar(index + 2 * bar_width, speedsdown2, bar_width,
                     alpha=opacity,
                     color='y',
                     label='Download')
    rects4 = plt.bar(index + 3 * bar_width, speedsup2, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Upload')
    plt.xlabel('States')
    plt.ylabel('Average Speeds')
    plt.title('Avg. Download and Upload speed for different state for ' + str(state))
    plt.xticks(index + bar_width, states, rotation=90)
    plt.legend()
    plt.tight_layout()

    if (save):
        plt.savefig('stats_const_state_' + str(state) + '.svg')
    plt.show()

'''filename = 'myspeed_reduced.csv'
df = pd.read_csv('april18_publish.csv')
#df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
df2 = pd.read_csv('may18_publish.csv', header=None)
df2.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
v = 1
constant_operator_compare(df, df2, 'JIO', '4G', 'n')
#constant_operator_compare(df, df2, 'JIO', '4G', 'n')
'''

@click.command()
@click.option('--filename', '-f', default='april18_publish.csv', help='Name of the CSV file')
@click.option('--filename2', '-f2', help='Name of the CSV file you want to compare to')
#@click.option('--inp','-i', prompt='Enter the option followed by operator/state', type=(int, str), help='Specifies the type of operation:\n1. Common Operator\n2. Common State\nFollowed by the common operator/state\n')
@click.option('--inp', '-i', type=int, prompt='Enter the operation:\n1.Common Operator\n2.Common State\n3.List of all States\n4.List of all Operators',
              help='Option to specify the type of operation\n1.Common Operator\n2.Common State\n3.List of all States\n4.List of all Operators')
@click.option('--common', '-c', help='Option to specify the common operator/state')
@click.option('--tech', '-t', type=click.Choice(['3G', '4G']), help='Option to specify the technology')
@click.option('--save', '-s', type=click.Choice(['0', '1']), default='0', help='Option to save the graph')
@click.option('--verbose', '-v', type=click.Choice(['0', '1']), default='0', help='Option for verbosity')


def processthis(filename, filename2, inp, common, tech, save, verbose):
    global v
    v = verbose
    if ((inp in {1,2}) & ((common is None) or (tech is None))):
        print('Common State/Operator/Technology not specified')
        exit()        
    #uncomment if there are differences in data names    

    if (inp == 1):
        if (filename2 is None):
            df = pd.read_csv(filename)
            df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            #df['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            constant_operator(df, common.upper(), tech, save)
        else:
            df = pd.read_csv(filename)
            df2 = pd.read_csv(filename2)
            df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            df2.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            #df['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            #df2['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            constant_operator_compare(df, df2, common.upper(), tech, save)
    elif (inp == 2):
        if (filename2 is None):
            df = pd.read_csv(filename)
            df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            #df['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            constant_operator(df, common.upper(), tech, save)
        else:
            df = pd.read_csv(filename)
            df2 = pd.read_csv(filename2)
            df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            df2.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            #df['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            #df2['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            constant_state_compare(df, df2, common.capitalize(), tech, save)
    elif (inp == 3):
        print(df['LSA'].unique())
    elif (inp == 4):
        print(df['Service Provider'].unique())
    else:
        print('Incorrect Options')

if __name__ == '__main__':
    processthis()





