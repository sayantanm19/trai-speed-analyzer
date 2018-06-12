import pandas as pd
from barplot_double import plot_double_bar_state, plot_double_bar_operator

def constant_operator(df, operator, technology, save, v):
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

def constant_state(df, state, technology, save, v):
    operators = df['Service Provider'].unique()
    speedsdown =[]
    speedsup = []
    f_operators = []
    #print('TOTAL PROVIDERS: ' + str(len(providers)))

    for operator in operators:
        ttype = (df[(df['LSA'] == state) & (df['Service Provider'] == operator) & (df['Technology'] == technology)])
        down = (ttype[ttype['Test_type'] == 'download']["Data Speed(Mbps)"]).mean() #extract only download
        up =(ttype[ttype['Test_type'] == 'upload']["Data Speed(Mbps)"]).mean()  #extract only upload
        
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

