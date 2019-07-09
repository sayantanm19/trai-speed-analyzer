
# TRAI SpeedAnalyze

SpeedAnalyze is a script written in python that can analyze dataspeeds sourced from [TRAI MySpeed Portal](www.myspeed.trai.gov.in), and can sort data on the basis of network operators and states. It can also compare and plot bar-graphs.

A guide was written for the GeeksForGeeks Technical Scripter contest where the process is described and the code is explained. **Check out:** [Analyzing Mobile Data Speeds from TRAI with Pandas](https://www.geeksforgeeks.org/analyzing-mobile-data-speeds-from-trai-with-pandas/).
Won a prize for that! 🕺

![Example barplot:](/images/bar_chart_jio.png)


### Prerequisites

  - pandas - to process/clean the csv data
  - numpy - various functions used as helper
  - matplotlib - to plot he bar-graph
  - click - to incorporate a CLI environment
  
 ### Usage:
   
```
  -f, --filename TEXT    Name of the CSV file
  -f2, --filename2 TEXT  Name of the CSV file you want to compare to
  -i, --inp INTEGER      Option to specify the type of operation
  -c, --common TEXT      Option to specify the common operator/state
  -t, --tech [3G|4G]     Option to specify the technology
  -s, --save [0|1]       Option to save the graph
  -v, --verbose [0|1]    Option for verbosity
  --help                 Show this message and exit.
 ```
 
##### Example:
 - speedanalyze.py -f march18_publish.csv -i 1 -c jio -t 4G

This will use the common operator JIO across all states available in dataset plot a bargraph.

### Installation

SpeedAnalyze requires [Python](https://www.python.org/) to run.

Install the dependencies from pip:

```sh
$ python -m pip install pandas
$ python -m pip install numpy
```

### Development

This was a test project to learn working with pandas and matplotlib. There are many inconsistencies in code and it does not follow any proper standards. You are free to adapt and improve this piece of code if you find this useful.

### Todos

 - Make a simple website which can display the data interactively.
 - Add more ways to represent data
 
### Links

 - [TRAI MySpeed Portal](www.myspeed.trai.gov.in)

### License

MIT License

