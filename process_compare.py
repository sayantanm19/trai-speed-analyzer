import pandas as pd
from barplot_double_compare import plot_double_bar_state_comp, plot_double_bar_operator_comp

def constant_operator_compare(df, df2, operator, technology, save, v):
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
    plot_double_bar_operator_comp(f_states, operator, speedsdown, speedsup, speedsdown2, speedsup2, save)

def constant_state_compare(df, df2, state, technology, save, v):
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
