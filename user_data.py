import csv
from spider import douban_spider
import numpy as np

genre_classes = ['剧情', '家庭', '犯罪', '传记', '喜剧', '爱情', '惊悚', '冒险', '动作', '科幻', '恐怖', '奇幻', '悬疑', '音乐', '动画', '儿童', '历史', '古装', '战争', '灾难', '运动', '歌舞', '同性', '纪录片', '短片', '情色']

class user(object):
    def __init__(self,id):
        self.id = id
        self.movies = get_user(id)
        self.vector, self.vector_norm = self.get_vector()
    def get_vector(self):
        ul = self.movies#电影列表：片名，类型
        vector = np.zeros(26)

        for movie in ul:
            title, genres = movie[0],movie[2][1:-1].split(', ')
            genres = [i[1:-1] for i in genres]
            for genre in genres:
                if genre != '':
                #if genre not in genre_classes:
                #    genre_classes.append(genre)
                    idx = genre_classes.index(genre)
                    vector[idx]+=1
        
        normalized_vector = vector/np.sqrt(np.sum(vector**2))
        #print(genre_classes)
        return vector,np.round(normalized_vector,4)

def save_user(user_id):

    print('正在保存用户: {} 的观影信息至CSV文件>>>'.format(user_id))
    user = douban_spider(user_id).movies

    with open('users/'+user_id+'.csv','w+',newline='') as t:
        writer = csv.writer(t)
        writer.writerows(user)
    print('CSV文件已保存!')

def get_user(user_id):

    with open('users/'+user_id+'.csv','r+',newline='') as t:
        reader = csv.reader(t)
        list = []
        for i in reader:
            list.append(i)
    return list

#save_user('angy617')