"""

Process Running Observer (PRO)

If anything in watch_list changes, the processes are restarted

"""
from glob import glob
import os
from subprocess import Popen
import time

class Runner(object):
    def __init__(self):
        self.run_list = []
    def run(self, *commands, **kwargs):
        watch_list = []
        for watch_path in kwargs.get('watch_list', []):
            watch_list.extend(glob(watch_path))
        self.run_list.append(handle_run(commands, watch_list))
    def update_run_list(self):
        self.run_list = [handle_run(*args) for args in self.run_list]
    def run_updates(self):
        while True:
            time.sleep(1)
            self.update_run_list()


def handle_run(commands, watch_list, processes=None, stats=None):
    if processes is None:
        processes = []
    new_stats = [os.stat(f) for f in watch_list]
    if new_stats != stats:
        print '..'
        # kill all the processes
        print 'Diff detected. Killing processes...'
        for p in processes: p.terminate()
        # wait for all the processes to die
        for p in processes: p.wait()
        print 'Processes killed. Respawning...'
        # respawn
        def run(cmd):
            cd = ''
            if isinstance(cmd, CMD):
                cd = 'cd ' + (cmd.cd or '.') + ' && '
                for c in cmd.commands[:-1]:
                    Popen(cd + 'exec ' + c, shell=True).wait()
                cmd = cmd.commands[-1]
            return Popen(cd + 'exec ' + cmd, shell=True)
        processes = [run(cmd) for cmd in commands]
    return commands, watch_list, processes, new_stats

class CMD(object):
    def __init__(self, *commands, **kwargs):
        self.cd = kwargs.get('cd')
        self.commands = commands

# python wart:
#def run(*commands, watch_list=None):
#    print commands, watch_list

runner = Runner()
run = runner.run

