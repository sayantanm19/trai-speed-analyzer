import pandas as pd
import click
from process_single import constant_operator, constant_state
from process_compare import constant_operator_compare, constant_state_compare

@click.command()
@click.option('--filename', '-f', default='april18_publish.csv', help='Name of the CSV file')
@click.option('--filename2', '-f2', help='Name of the CSV file you want to compare to')
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
            constant_operator(df, common.upper(), tech, save, v) #upper() to convert for operator's case
        else:
            df = pd.read_csv(filename)
            df2 = pd.read_csv(filename2)
            df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            df2.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            #df['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            #df2['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            constant_operator_compare(df, df2, common.upper(), tech, save, v)
    elif (inp == 2):
        if (filename2 is None):
            df = pd.read_csv(filename)
            df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            #df['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            constant_state(df, common.capitalize(), tech, save, v) #capitalize() to convert for state's case
        else:
            df = pd.read_csv(filename)
            df2 = pd.read_csv(filename2)
            df.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            df2.columns = ['Service Provider', 'Technology', 'Test_type', 'Data Speed(Mbps)', 'Signal_strength', 'LSA']
            #df['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            #df2['Test_type'].replace({'Download': 'download', 'Upload': 'upload'}, inplace=True)
            constant_state_compare(df, df2, common.capitalize(), tech, save, v)
    elif (inp == 3):
        print(df['LSA'].unique())
    elif (inp == 4):
        print(df['Service Provider'].unique())
    else:
        print('Incorrect Options')

if __name__ == '__main__':
    processthis()





