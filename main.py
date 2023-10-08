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
