import psutil

<<<<<<< HEAD

def get_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    return cpu_percent, cpu_cores, cpu_threads


def cpu_show(cpu_percent, cpu_cores, cpu_threads):
    print("_" * 61)
    load = "{:░<10}".format("▓" * int(cpu_percent / 10))
    print("|{:<7} {:<9} {:<10}{}{:<21}|".format(" CPU", "Load", str(cpu_percent) + "%", load, ""))
    print("|{:<8}{:<10}{:<10}{:<31}|".format("", "Cores:", str(cpu_cores) + " ", ""))
    print("|{:<8}{:<10}{:<10}{:<31}|".format("", "Threads:", str(cpu_threads) + " ", ""))


def get_memory_info():
    mem_info = psutil.virtual_memory()
    total = mem_info.total,
    available = mem_info.available,
    percent = mem_info.percent
    return total[0], available[0], percent


def memory_show(total, available, percent):
    load = "{:░<10}".format("▓" * int(percent / 10))
    print("|{:<7} {:<9} {:<10}{}{:<21}|".format(" Ram", "Load: ", str(percent) + "%", load, ""))
    print("|{:<8}{:<10}{:<10}{:<31}|".format("", "Total:", str(total // 1024 ** 2) + " Mb.", ""))
    print("|{:<8}{:<10}{:<10}{:<31}|".format("", "Free:", str(available // 1024 ** 2) + " Mb.", ""))


def process_info():
    return [proc_info.info for proc_info in psutil.process_iter(['pid', 'name', 'status'])]


def hat_table_show():
    print("_" * (15 + 25 + 21))
    print("|{:^9}|{:^39}|{:^9}|".format('PID', 'Name', 'Status'))
    print("_" * (15 + 25 + 21))


def show_table_process(info):
    tampe_late = "| {pid:<7} | {name:<37} | {status:<7} | "
    for p in info:
        print(tampe_late.format(**p))


def main():
    cpu_show(*get_cpu_info())
    print("| {:>59}".format("|"))
    memory_show(*get_memory_info())
    hat_table_show()
    show_table_process(process_info())


if __name__ == "__main__":
    main()







=======
def get_cpu_info():
    time_info = psutil.cpu_times()
    return {
        "user": time_info.user,
        "system": time_info.system,
        "idle": time_info.idle,
        "percent": psutil.cpu_percent(percpu=False)
    }
>>>>>>> 94c7f83da28f10d7700e5de993fc0699b3c78d41

def get_memory_info():
    mem_info = psutil.virtual_memory()
    return {
        "total": mem_info.total,
        "available": mem_info.available,
        "used": mem_info.used
    }

def get_process_info():
    process_info = {}
    for proc in psutil.process_iter(['pid', 'name', 'nice', 'status']):
        info = proc.info
        pid = info.get('pid')
        if pid is not None:
            process_info[pid] = {"name": info['name'], "priority": info["nice"], 'status': info['status']}
    return process_info

def hat_table_show():
    print("{:_^10}{:_^35}{:_^15}{:_^12}{:_^14}".format("_", "_", "_", "_", "_"))
    print("|{:5}|{:^35}|{:^15}|{:^12}|{:^13}|".format('№', 'Name', 'PID', 'Status', 'Priority'))
    print("|{:_^5}|{:_^35}|{:_^15}|{:_^12}|{:_^13}|".format("_", "_", "_", "_", "_"))

    def iter_process_info():
        number_column = 0
        for list_iter in psutil.process_iter():
            number_column += 1
            pid = list_iter.as_dict(['pid'])
            name = list_iter.as_dict(['name'])
            priority = list_iter.as_dict(['nice'])
            status = list_iter.as_dict(['status'])
        print (
            "║{:^5}│{:<35}│{:^15}│{:^13}║".format(pid['pid'], name['name'], priority['nice'], status['status']))

    iter_process_info()

def main():
    get_process_info()
    get_cpu_info()
    get_memory_info()
    hat_table_show()

main()

print(get_process_info())








# print(process_table_show())


# print(get_memory_info())
# print(get_cpu_info())
# print(get_process_info())
