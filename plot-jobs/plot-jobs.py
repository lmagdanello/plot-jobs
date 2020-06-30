import subprocess
import matplotlib.pyplot as plt
import argparse
import sys

def plot_jobs(date):

        # vars_j: Utiliza o slurm accounting para capturar os estados dos Jobs a partir da data informada pelo usuário

        failed_j = subprocess.getoutput('sudo sacct --starttime {} | egrep -E \'FAILED\' | wc -l'.format(date))
        complete_j = subprocess.getoutput('sudo sacct --starttime {} | egrep -E \'COMPLETED\' | wc -l'.format(date))
        cancelled_j = subprocess.getoutput('sudo sacct --starttime {} | egrep -E \'CANCELLED\' | wc -l'.format(date))

        # state_dict: Armazena os estados dos Jobs em um dicionario

        state_dict = { 'completed': int(complete_j), 'failed': int(failed_j), 'cancelled': int(cancelled_j) }

        # sorted_dict: Mapeia o dicionario de estados de forma crescente

        sorted_dict = {k: state_dict[k] for k in sorted(state_dict, key=state_dict.get)}

        '''
         Definimos (x,y):
                - X sao os estados dos Jobs e as chaves do dicionario
                - Y sao os valores contabilizados para cada estado e os valores de cada chave no dicionario
        '''

        states = list(sorted_dict.keys())
        values = list(sorted_dict.values()) 

        # Realizamos a criacao do graph
        colors = ('red', 'grey', 'green')
        plt.figure(figsize=(10,10))
        explode = (0, 0, 0.1)

        plt.pie(values, explode=explode, shadow=True, wedgeprops={'linewidth' : 1, 'edgecolor' : 'black'}, colors=colors, autopct='%8.1f%%')
        title = 'Job Status since: "{}"'.format(date)

        # Criamos a box de legendas
        plt.legend(
            loc='center left',
            labels=['%s: %1.1f%%' % (
                s, (float(v) / sum(values)) * 100) for s, v in zip(states, values)], 
            title=''.join('{:^50}'.format(s) for s in title.split('\n')), 
            bbox_to_anchor=(1, 0, 0, 1.3)
        )
        plt.axis('equal')
        plt.tight_layout()

        # Salvamos a figura no dir presente, com o sufixo da data utilizada como parametro

        plt.savefig('./pie-plot-{}.png'.format(date))

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--date',
            type=plot_jobs,
            action='store',
            help='Starting time, format: 2020-02-02')

date = parser.parse_args()

if len(sys.argv) <= 1:
    sys.argv.append('--help')
    options = parser.parse_args()
    options.func()
