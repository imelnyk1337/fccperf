import matplotlib.pyplot as plt
import json


def plot_graph(data: list, y_lims: [], xrange: list, name: str, title: str):
    plt.figure(figsize=(12, 8), facecolor='white')
    ax = plt.axes()
    ax.set_facecolor('white')
    ax.set_alpha(0.1)
    plt.grid()
    plt.xlim([0, 65])
    plt.ylim(y_lims)
    plt.title(title, fontsize=14)
    plt.plot([x for x in range(*xrange)], data, linewidth=2.5, color="red", label=title)
    plt.legend(fontsize=12)
    plt.xlabel("Number of threads", fontsize=12)
    plt.ylabel(title, fontsize=18)
    plt.show()
    plt.savefig("/home/ihor/PycharmProjects/fccperf/plots/" + name + ".png")


def divide_by_threads(data: list, xrange: list) -> list:
    threads = range(*xrange)
    divided = []
    for x, n in zip(data, threads):
        divided.append(x / n)
    return divided


def json2dict(file: str, xrange: list) -> dict:
    datadict = {
        "bench_time": [],
        "n_events": [],
        "real_time": [],
        "user_time": [],
        "sys_time": []
    }
    with open(file) as perf_js:
        data = json.load(perf_js)
        for i in range(*xrange):
            datadict["bench_time"].append(float(data[str(i)]["time"]))
            datadict["n_events"].append(float(data[str(i)]["nevents"]))
            datadict["real_time"].append(float(data[str(i)]["real"]))
            datadict["user_time"].append(float(data[str(i)]["user"]))
            datadict["sys_time"].append(float(data[str(i)]["sys"]))
    return datadict


def json2dict_cpp(file: str, xrange: list) -> dict:
    datadict = {
        "bench_time": [],
        # "n_events": [],
        "real_time": [],
        "user_time": [],
        "sys_time": []
    }
    with open(file) as perf_js:
        data = json.load(perf_js)
        for i in range(*xrange):
            datadict["bench_time"].append(float(data[str(i)]["time"]))
            # datadict["n_events"].append(float(data[str(i)]["nevents"]))
            datadict["real_time"].append(float(data[str(i)]["real"]))
            datadict["user_time"].append(float(data[str(i)]["user"]))
            datadict["sys_time"].append(float(data[str(i)]["sys"]))
    return datadict


def json2dict_cpp_updated(file: str, xrange: list) -> dict:
    datadict = {
        "time": [],
        "elapsed": [],
        "cputime": [],
        "real_time": [],
        "user_time": [],
        "sys_time": []
    }
    with open(file) as perf_js:
        data = json.load(perf_js)
        for i in range(*xrange):
            datadict["time"].append(float(data[str(i)]["time"]))
            datadict["elapsed"].append(float(data[str(i)]["elapsed"]))
            datadict["cputime"].append(float(data[str(i)]["cputime"]))
            datadict["real_time"].append(float(data[str(i)]["real"]))
            datadict["user_time"].append(float(data[str(i)]["user"]))
            datadict["sys_time"].append(float(data[str(i)]["sys"]))
    return datadict


def json2dict_py(file: str, xrange: list) -> dict:
    datadict = {
        "time": [],
        "cputime": [],
        "real_time": [],
        "user_time": [],
        "sys_time": []
    }
    with open(file) as perf_js:
        data = json.load(perf_js)
        for i in range(*xrange):
            datadict["time"].append(float(data[str(i)]["time"]))
            datadict["cputime"].append(float(data[str(i)]["cputime"]))
            datadict["real_time"].append(float(data[str(i)]["real"]))
            datadict["user_time"].append(float(data[str(i)]["user"]))
            datadict["sys_time"].append(float(data[str(i)]["sys"]))
    return datadict


def json2dict_py_updated(file: str, xrange: list) -> dict:
    datadict = {
        "elapsed": [],
        "cputime": [],
        "real_time": [],
        "user_time": [],
        "sys_time": []
    }
    with open(file) as perf_js:
        data = json.load(perf_js)
        for i in range(*xrange):
            datadict["elapsed"].append(float(data[str(i)]["elapsed"]))
            datadict["cputime"].append(float(data[str(i)]["cputime"]))
            datadict["real_time"].append(float(data[str(i)]["real"]))
            datadict["user_time"].append(float(data[str(i)]["user"]))
            datadict["sys_time"].append(float(data[str(i)]["sys"]))
    return datadict


def json2dict_fcc_updated(file: str, xrange: list) -> dict:
    datadict = {
        "bench_time": [],
        "n_events": [],
        "elapsed": [],
        "cputime": [],
        "real_time": [],
        "user_time": [],
        "sys_time": []
    }
    with open(file) as perf_js:
        data = json.load(perf_js)
        for i in range(*xrange):
            datadict["bench_time"].append(float(data[str(i)]["time"]))
            datadict["n_events"].append(float(data[str(i)]["nevents"]))
            datadict["elapsed"].append(float(data[str(i)]["elapsed"]))
            datadict["cputime"].append(float(data[str(i)]["cputime"]))
            datadict["real_time"].append(float(data[str(i)]["real"]))
            datadict["user_time"].append(float(data[str(i)]["user"]))
            datadict["sys_time"].append(float(data[str(i)]["sys"]))
    return datadict


def sysbench(file: str) -> dict:
    datadict = {
        "time": [],
        "nevents": [],
        "real": [],
        "user": [],
        "sys": []
    }
    with open(file) as perf_js:
        data = json.load(perf_js)
        for i in range(1, 65):
            time = (data[str(i)]["time"]).strip(" ").split("s")[0]
            time = float(time)
            datadict["time"].append(time)
            nevents = (data[str(i)]["nevents"]).strip(" ")
            nevents = float(nevents)
            datadict["nevents"].append(nevents)
            real = data[str(i)]["real"]
            real = float(real)
            datadict["real"].append(real)
            usr = data[str(i)]["user"]
            usr = float(usr)
            datadict["user"].append(usr)
            syst = data[str(i)]["sys"]
            syst = float(syst)
            datadict["sys"].append(syst)

    return datadict


def compute_nevents(total: int, datatime: list) -> list:
    result = list()
    for time in datatime:
        result.append(total / time)
    return result


def calculate_ratio(target_lists: list, default_list: list) -> list:
    ratio = [target / default for target, default in zip(target_lists, default_list)]
    return ratio

