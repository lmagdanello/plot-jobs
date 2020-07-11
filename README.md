# plot-jobs

##### Tool created in Python to plot job status using Slurm accounting

This tool works with Slurm's sacct command to count a total of tasks that have failed, canceled and completed and to display them on a pie chart with percentage values.

    Prerequisites:
1. python3.6;
2. Slurm; 
3. Slurmdbd; 
4. sacct working properly;
5. matplotlib;
6. root.

**To-do:**
- implement gif for graphics;

## How it works?

The script has a parser for you to assign the period you want to analyze. It will create a pie chart with job status data for this period.

---

Usage example:

*python3.6 plot_jobs.py -s 2020-01-01 -e 2020-07-11*

   You will get a graph like this:
   
![alt text](https://github.com/lmagdanello/plot-jobs/blob/master/pie-plot-2020-01-01.png?raw=true)
