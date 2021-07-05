from user_data import user
import matplotlib.pyplot as plt
import numpy as np
#from spider import netease_spider
import math

zkx = '167121278'
zly = '168998711'

def mse(a,b):
    return ((a - b) **2).mean()

def psnr(a,b,max_val=1.0):
    return 10*np.log10(max_val**2/mse(a,b))

def naive_match(user_a,user_b):
    #基于共同观影
    a_list = [i[0] for i in user_a.movies]
    b_list = [j[0] for j in user_b.movies]
    ll = min(len(a_list), len(b_list))
    same_count = 0
    for mov in a_list:
        if mov in b_list:
            same_count += 1
    score = round(same_count / ll * 100, 2)
    return score

def weighted_match(user_a,user_b,weighted_factor=5):
    #电影小众程度加权的共同观影
    lamda = weighted_factor

    a_list = [i[0] for i in user_a.movies]
    a_pop = [i[1] for i in user_a.movies]
    b_list = [j[0] for j in user_b.movies]

    ll = min(len(a_list), len(b_list))
    same_count = 0
    for i in range(len(a_list)):
        if a_list[i] in b_list and a_pop[i]!=None:
            same_count += 1/math.log10(int(a_pop[i]))/math.log10(lamda)
    score = round(same_count / ll * 100, 2)
    return score

def search_best_match(metric,id1,id_list):
    #找到一个列表中匹配度最高的id
    max_score = 0.0
    for idx in id_list:
        score = metric(id1,idx)
        if score>=max_score:
            max_score = score
            best_match = idx
    return best_match, max_score

