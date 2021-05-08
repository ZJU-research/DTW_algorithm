import numpy as np
from matplotlib.pylab import plt
import pandas as pd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#如遇中文显示问题可加入以下代码
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
def DTW_function(s1,s2):
    dp=np.zeros([len(s1),len(s2)],dtype=float)
    id=np.zeros([len(s1),len(s2)],dtype=int)
    ans=0
    dic={}
    for i in range(len(s1)):
        for j in range(len(s2)):
            dp[i][j]=1e18
            id[i][j]=ans
            dic[ans]=(i,j)
            ans+=1

    dp[0][0]=abs(s1[0]-s2[0])
    path={}
    path[0]=0#初始化路径
    for i in range(len(s1)):#开始动态规划
        for j in range(len(s2)):
            if i-1>=0:
                if dp[i-1][j]+abs(s1[i]-s2[j])<dp[i][j]:
                    dp[i][j]=dp[i-1][j]+abs(s1[i]-s2[j])
                    path[id[i][j]]=id[i-1][j]
            if j-1>=0:
                if dp[i][j-1]+abs(s1[i]-s2[j])<dp[i][j]:
                    dp[i][j]=dp[i][j-1]+abs(s1[i]-s2[j])
                    path[id[i][j]]=id[i][j-1]
            if i-1>=0 and j-1>=0:
                if dp[i-1][j-1]+abs(s1[i]-s2[j])<dp[i][j]:
                    dp[i][j]=dp[i-1][j-1]+abs(s1[i]-s2[j])
                    path[id[i][j]]=id[i-1][j-1]

    ax=plt.subplot(111) #注意:一般都在ax中设置,不再plot中设置

    x=len(s1)-1
    y=len(s2)-1
    PATH=[]
    while id[x][y]!=0:
        PATH.insert(0,(x,y))
        ax.fill_between([x, x+1], y, y+1, facecolor='red')
        x,y=dic[path[id[x][y]]]
    PATH.insert(0,(x,y))
    ax.fill_between([x, x+1], y, y+1, facecolor='red')
    plt.xlim(0, len(s1)-1)
    plt.ylim(0, len(s2)-1)
    plt.xlabel('数据s1')
    plt.ylabel('数据s2')
    plt.title('DTW数据匹配路径图  误差结果为'+str(dp[len(s1)-1][len(s2)-1]))
    ax.xaxis.set_major_locator(MultipleLocator(1))#设置y主坐标间隔 1
    ax.yaxis.set_major_locator(MultipleLocator(1))#设置y主坐标间隔 1

    ax.xaxis.grid(True,which='major')#major,color='black'
    ax.yaxis.grid(True,which='major')#major,color='black'

    plt.show()
    print('误差=',dp[len(s1)-1][len(s2)-1])
    print('路径=',PATH)

if __name__ == '__main__':
    #加载数据
    df=pd.read_csv('data.csv')
    n,m=df.shape
    print('共'+str(m)+'条数据，每条数据长度为'+str(n))
    print('两两进行DTW匹配')
    for i in range(n):
        for j in range(i+1,n):
            print('data'+str(i+1)+'与data'+str(j+1))
            DTW_function(df.iloc[:,i],df.iloc[:,j])