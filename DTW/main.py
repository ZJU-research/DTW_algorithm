'''
--------------------------------------- description----------------------------------------
@author:Mengcheng Fang
@time:2021.5.8
@Use: Run DTW_function() directly.
@funtion:DTW_function(s1, s2)
@Parameter Description:
    Input:s1 and s2 are the two one-dimensional time series data you input. There is no requirement for the length of s1 and s2.
    Output:The output is a numeric value indicating the degree of difference between the two input time series. The matching path of the two data will be printed at the same time.
'''
import numpy as np
from matplotlib.pylab import plt
import pandas as pd
from matplotlib.ticker import MultipleLocator
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # Specify the default font
mpl.rcParams['axes.unicode_minus'] = False  # Solve the problem that the minus sign'-' is displayed as a square in the saved image


def DTW_function(s1, s2):#Used to calculate the degree of difference between two pieces of data
    dp = np.zeros([len(s1), len(s2)], dtype=float)
    id = np.zeros([len(s1), len(s2)], dtype=int)
    ans = 0
    dic = {}#dic is used to record our path
    for i in range(len(s1)):#Initialize dp data, dp[i][j] represents the degree of difference between data s1[0:i] and data s2[0:j].
        for j in range(len(s2)):
            dp[i][j] = 1e18
            id[i][j] = ans
            dic[ans] = (i, j)
            ans += 1

    dp[0][0] = abs(s1[0] - s2[0])
    path = {}
    path[0] = 0  # Initialization path.
    for i in range(len(s1)):  # Start dynamic planning.
        for j in range(len(s2)):
            #Start the data transfer and update, and record the state of the smallest difference program.
            if i - 1 >= 0:
                if dp[i - 1][j] + abs(s1[i] - s2[j]) < dp[i][j]:
                    dp[i][j] = dp[i - 1][j] + abs(s1[i] - s2[j])
                    path[id[i][j]] = id[i - 1][j]
            if j - 1 >= 0:
                if dp[i][j - 1] + abs(s1[i] - s2[j]) < dp[i][j]:
                    dp[i][j] = dp[i][j - 1] + abs(s1[i] - s2[j])
                    path[id[i][j]] = id[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                if dp[i - 1][j - 1] + abs(s1[i] - s2[j]) < dp[i][j]:
                    dp[i][j] = dp[i - 1][j - 1] + abs(s1[i] - s2[j])
                    path[id[i][j]] = id[i - 1][j - 1]

    ax = plt.subplot(111)

    x = len(s1) - 1
    y = len(s2) - 1
    PATH = []
    while id[x][y] != 0:
        PATH.insert(0, (x, y))
        ax.fill_between([x, x + 1], y, y + 1, facecolor='red')
        x, y = dic[path[id[x][y]]]
    PATH.insert(0, (x, y))
    ax.fill_between([x, x + 1], y, y + 1, facecolor='red')
    plt.xlim(0, len(s1) - 1)
    plt.ylim(0, len(s2) - 1)
    plt.xlabel('s1')
    plt.ylabel('s2')
    plt.title('DTW data matching path diagram The error result is ' + str(dp[len(s1) - 1][len(s2) - 1]))
    ax.xaxis.set_major_locator(MultipleLocator(1))  # Set the y main coordinate interval 1
    ax.yaxis.set_major_locator(MultipleLocator(1))  # Set the y main coordinate interval 1

    ax.xaxis.grid(True, which='major')
    ax.yaxis.grid(True, which='major')

    plt.show()
    print('error =', dp[len(s1) - 1][len(s2) - 1])
    print('path=', PATH)


if __name__ == '__main__':
    # Load data
    df = pd.read_csv('data.csv')
    n, m = df.shape
    print('A total of ' + str(m) + ' data, each data length is ' + str(n))
    print('Pairwise DTW matching ')
    for i in range(n):
        for j in range(i + 1, n):
            print('data' + str(i + 1) + 'and data' + str(j + 1))
            DTW_function(df.iloc[:, i], df.iloc[:, j])
