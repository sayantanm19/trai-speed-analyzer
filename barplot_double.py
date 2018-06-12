import numpy as np
import matplotlib.pyplot as plt

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
        plt.savefig('stats_const_operator_' + str(operator) + '.svg', dpi=1000)
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
        plt.savefig('stats_const_state' + str(state) + '.svg', dpi=1000)
    plt.show()

