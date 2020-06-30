# plot-jobs

##### Tool created in Python to plot job status using Slurm accounting.

This tool works using Slurm sacct command to make a total of the jobs that failed, were canceled and ended to display them in a pie chart with the percentage values of these.

    Prerequisites:
1. python3.6;
2. Slurm; 
3. Slurmdbd; 
4. sacct working properly.

**To-do:**
- add `explode` to the highest value identified in the analysis (done)
- change colors (done)
- NEW: add RED color for Failed state;
- allow the user to make an analysis between periods;
- implement gif for graphics;

## How it works?

The script has a simple parser for you assign the date you want to analyze. It will create the chart based on this date until the current date.

Example:

Date at time of execution: *2020-02-01*

> python3 plot-jobs.py -d (or --date) 2020-01-01

This will generate a graphical analysis from 01-01 to 02-01.

You will get a graph like this:


![alt text](https://github.com/lmagdanello/plot-jobs/blob/master/pie-plot-2020-01-01.png?raw=true)
