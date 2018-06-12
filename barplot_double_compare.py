import numpy as np
import matplotlib.pyplot as plt

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
    plt.xticks(index + bar_width, operators, rotation=90)
    plt.legend()
    plt.tight_layout()

    if (save):
        plt.savefig('stats_const_state_' + str(state) + '.svg')
    plt.show()

