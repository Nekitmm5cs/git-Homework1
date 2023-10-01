import datetime
import psutil

processes = []
for proc in psutil.process_iter():
    try:
        process = []
        process.append(str(proc.pid))
        process.append(str(proc.username()))
        process.append(str(proc.nice()).replace("Priority.", "").replace("_PRIORITY_CLASS", ""))
        process.append(str(proc.cpu_percent()))
        process.append(str(round(proc.memory_info().rss / (1024 * 1024), 2)))
        process.append(str(datetime.datetime.fromtimestamp(proc.create_time()).strftime("%H:%M:%S")))
        process.append(str(proc.cmdline()[0]))
        processes.append(process)
    except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
        pass
print("_____________________________________________________________________________________________________________________________________")
print("|  PID   |          USER          |         PRI         |   CPU%   |   MEM   |     TIME     |                Command                |")
print("|________|________________________|_____________________|__________|_________|______________|_______________________________________|")
for string in processes:
    print("| {:7}| {:23}| {:20}| {:9}| {:8}| {:13}| {:38}| ".format(string[0], string[1], string[2], string[3], string[4], string[5], string[6].ljust(34)[:34]))

