import datetime
import psutil

def get_pid_info(proc):
    return str(proc.info['pid'])

def get_username_info(proc):
    return str(proc.info['username'])

def get_priority_info(proc):
    return str(proc.info['nice']).replace("Priority.", "").replace("_PRIORITY_CLASS", "")

def get_cpu_info(proc):
    return str(proc.info['cpu_percent'])

def get_memory_info(proc):
    return str(round(proc.info['memory_info'].rss / (1024 * 1024), 2))

def get_create_time_info(proc):
    return str(datetime.datetime.fromtimestamp(proc.info['create_time']).strftime("%H:%M:%S"))

def get_command_info(proc):
    cmdline = proc.info['cmdline']
    return str(cmdline[0]) if cmdline else 'None'

def main():
    processes = []
    try:
        for proc in psutil.process_iter(attrs=['pid', 'username', 'nice', 'cpu_percent', 'memory_info', 'create_time', 'cmdline']):
            process = [
                get_pid_info(proc),
                get_username_info(proc),
                get_priority_info(proc),
                get_cpu_info(proc),
                get_memory_info(proc),
                get_create_time_info(proc),
                get_command_info(proc)
            ]
            processes.append(process)
    except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
        pass

    print_process_table(processes)

def print_process_table(processes):
    print(
        "_____________________________________________________________________________________________________________________________________")
    print(
        "|  PID   |          USER          |         PRI         |   CPU%   |   MEM   |     TIME     |                Command                |")
    print(
        "|________|________________________|_____________________|__________|_________|______________|_______________________________________|")
    for string in processes:
        print("| {:7}| {:23}| {:20}| {:9}| {:8}| {:13}| {:38}| ".format(string[0], string[1], string[2], string[3], string[4], string[5],
            string[6].ljust(34)[:34]))

if __name__ == "__main__":
    main()
