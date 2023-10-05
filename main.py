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
    for proc in psutil.process_iter(['pid', 'name']):
        info = proc.info
        pid = info.get('pid')
        if pid is not None:
            process_info[pid] = {"name": info['name']}
    return process_info



print(get_memory_info())
print(get_cpu_info())
print(get_process_info())
