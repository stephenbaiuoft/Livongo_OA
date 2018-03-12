from parser_process import *
import numpy as np
import matplotlib.pyplot as plt

def main():
    p = parser_process("usage.csv")
    # process the file and get max_running_days for each user
    p.process()
    # array
    data_points = p.get_result()

    # now perform analysis
    run_analysis(data_points)


# analyze
def run_analysis(data_points):
    data = np.array(data_points)
    show_image(data)
    display_result(data)

def display_result(data):
    count = np.shape(data)[0]
    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data)
    min = np.min(data)
    quarter = np.percentile(data, 25)
    half = np.percentile(data, 50)
    three_quarters = np.percentile(data, 75)
    max = np.max(data)

    print("day")
    print("count:\t", count)
    print("mean:\t", mean)
    print("median:\t", median)
    print("std:\t", std)
    print("min:\t", min)
    print("25%:\t", quarter)
    print("50%:\t", half)
    print("75%:\t", three_quarters)
    print("max:\t", max)


def show_image(data):
    plt.plot(data)
    plt.title("Data Chart")
    plt.ylabel("longest running inactive days")
    plt.xlabel("user_id")
    plt.show()


if __name__ == '__main__':
    main()