import psutil

def get_cpu_info():
    time_info = psutil.cpu_times()
    return {
        "user": time_info.user,
        "system": time_info.system,
        "idle": time_info.idle,
        "percent": psutil.cpu_percent(percpu=False)
    }

def get_memory_info():
    mem_info = psutil.virtual_memory()
    return {
        "total": mem_info.total,
        "available": mem_info.available,
        "used": mem_info.used
    }

def get_process_info():
    process_info = {}
    for proc in psutil.process_iter(['pid', 'name', 'nice', 'cpu_percent', 'status']):
        info = proc.info
        pid = info.get('pid')
        if pid is not None:
            process_info[pid] = {"name": info['name'], "priority": info["nice"], 'status': info['status']}
    return process_info

def hat_table_show():
    print("{:_^10}{:_^35}{:_^10}{:_^12}{:_^14}".format("_", "_", "_", "_", "_", "_"))
    print("|{:^5}|{:^35}|{:^10}|{:^12}|{:^13}|".format('№', 'Name', 'Priority', 'PID', 'Status'))
    print("|{:_^5}|{:_^35}|{:_^10}|{:_^12}|{:_^13}|".format("_", "_", "_", "_", "_", "_"))

def process_table_show:






# print(process_table_show())


# print(get_memory_info())
# print(get_cpu_info())
print(get_process_info())
