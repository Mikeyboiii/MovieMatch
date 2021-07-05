from user_data import user
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from utils import *
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

users = {'zkx':'186591345','zly':'133364029'}


def plot_user(us):
    #观看电影偏好直方图
    data = us.vector
    labels = ['剧情', '家庭', '犯罪', '传记', '喜剧', '爱情', '惊悚', '冒险', '动作', '科幻', '恐怖', '奇幻', '悬疑', '音乐', '动画', '儿童', '历史', '古装', '战争', '灾难', '运动', '歌舞', '同性', '纪录片', '短片', '情色']
    combined = []
    for i in range(len(data)):
        combined.append([data[i],labels[i]])
    combined = sorted(combined,reverse=True)
    colors = ['#840000','#bb3f3f','#e50000','#fc824a','#f97306','#f9bc08','#ffdf22','#d0e429','#99cc04','#5cb200','#419c03','#4f9153','#75bbfd','#448EE4','#056EEE','#2976bb','#436BAD','#4B57DB','#6258C4','#6241C7']
    plt.bar(range(len(data)), [i[0] for i in combined], tick_label=[i[1] for i in combined],color=colors)
    plt.show()

zkx = user(users['zkx'])
zly = user(users['zly'])
print(zly.vector_norm)
#print(matplotlib.matplotlib_fname())

#print(naive_match(zkx,zly))