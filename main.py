import psutil


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








