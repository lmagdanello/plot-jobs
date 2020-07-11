import subprocess
import matplotlib.pyplot as plt
import argparse
import sys
import os
from datetime import date

def plot_jobs(starttime,endtime):
    """
    Plot_jobs is responsible for collecting data (using slurm accounting) from completed, failed and canceled jobs, mapping them in a dictionary and creating the pie chart
    """

    failed_j = subprocess.getoutput('sudo sacct --starttime {} --endtime {} -X | egrep -E \'FAILED\' | wc -l'.format(starttime, endtime))
    complete_j = subprocess.getoutput('sudo sacct --starttime {} --endtime {} -X | egrep -E \'COMPLETED\' | wc -l'.format(starttime, endtime))
    cancelled_j = subprocess.getoutput('sudo sacct --starttime {} --endtime {} -X | egrep -E \'CANCELLED\' | wc -l'.format(starttime, endtime))

    state_dict = { 'completed': int(complete_j), 'failed': int(failed_j), 'cancelled': int(cancelled_j) }

    states = list(state_dict.keys())
    values = list(state_dict.values()) 
	
    colors = ('green', 'red', 'grey')
    plt.figure(figsize=(10,10))
    explode = (0, 0.1, 0)
    plt.pie(values, explode=explode, shadow=True, wedgeprops={'linewidth' : 1, 'edgecolor' : 'black'}, colors=colors, autopct='%8.1f%%')
    title = 'Job Status from {} to {} '.format(starttime, endtime)

    plt.legend(
        loc='center left',
        labels=['%s: %1.1f%%' % (
                 s, (float(v) / sum(values)) * 100) for s, v in zip(states, values)], 
                 title=''.join('{:^50}'.format(s) for s in title.split('\n')), 
                 bbox_to_anchor=(1, 0, 0, 1.3)
               )
    plt.axis('equal')
    plt.tight_layout()

    '''
    Saves the file as: pie-plot-{OS.HOSTNAME}-{CURRENT DATE}.png in the current directory
    '''
    host = os.uname()[1]
    today = date.today()
    d = today.strftime("%y-%m-%d")
    plt.savefig('./pie-plot-{0}-{1}.png'.format(host, d))

def parser():
    """
    Parser is responsible for receiving the arguments for the plot (start time and end time)
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--starttime',
            action='store',
            help='Starting time, format: 2020-02-02')

    parser.add_argument('-e', '--endtime',
            action='store',
            help='Starting time, format: 2020-02-02')
    args = vars(parser.parse_args())

    if len(sys.argv) <= 1:
       sys.argv.append('--help')
       options = parser.parse_args()
       options.func()

    plot_jobs((args['starttime']), (args['endtime']))

if __name__ == "__main__":
	parser()
