import requests
from bs4 import BeautifulSoup
import urllib.request

#获取豆瓣用户观影数据
class douban_spider(object):
    def __init__(self, id):
        self.url = 'https://movie.douban.com/people/' + id + '/collect'
        page = self.get_response(0)
        title = self.get_title(page)
        self.movie_num = self.get_total(title)
        self.movies = self.get_movies(self.movie_num)

    def set_header(self):
        self.header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
            'cookie': 'douban-fav-remind=1; _ga=GA1.2.2038204987.1579101915; _vwo_uuid_v2=D150CFA056EE9B6EB124CF8BE7C183D4F|1bb0f6bab6f0daef15bda67b95b8cbc5; gr_user_id=2f69af20-a5bc-4f04-9fdf-2a832fc020ca; douban-profile-remind=1; __utmv=30149280.13336; __yadk_uid=gSkthFlYRI34QGEjdVx1m3yNiLLV8KeW; viewed="6895444_3016422_19346510_2340262_20414177_3314260_3256124_4819818"; bid=94CdEjVXe-4; ll="108288"; _vwo_uuid_v2=D150CFA056EE9B6EB124CF8BE7C183D4F|1bb0f6bab6f0daef15bda67b95b8cbc5; push_noty_num=0; push_doumail_num=0; ct=y; __utmz=30149280.1623339423.164.153.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utmc=223695111; dbcl2="133364029:qj3eME9BPHk"; ck=EM6b; __utmz=223695111.1623660856.32.30.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/66702150/; __gads=ID=a53a4ee1dd4a2d4c-22dd65d364c9001c:T=1623661558:RT=1623661558:S=ALNI_Mazs1CxYafvdlnZRf8sxFnWUB-0lA; __utma=30149280.2038204987.1579101915.1623660682.1623664136.169; __utmb=30149280.0.10.1623664136; __utma=223695111.2038204987.1579101915.1623660856.1623664136.33; __utmb=223695111.0.10.1623664136; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1623664137%2C%22https%3A%2F%2Fwww.douban.com%2Fpeople%2F66702150%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=0f44658fecd681bc.1609263325.34.1623665147.1623661802.'
        }
        return self.header

    def get_response(self,page_num):
        #爬取网页
        url = self.url + '?start=%d&sort=time&rating=all&filter=all&mode=grid'%page_num
        s = requests.Session()
        header = self.set_header()
        response = s.get(url, headers=header).content
        page = BeautifulSoup(response, 'lxml')

        #print(page)
        return page

    def get_title(self,page):
        #网页主题
        title = page.find('title')
        return str(title)

    def get_total(self,title):
        #看过电影总数
        left_bracket = title.find('(')
        right_bracket = title.find(')')
        num_str = title[left_bracket+1:right_bracket]
        num = int(num_str)
        return num

    def get_movies(self,num):
        #获取影片列表
        num_of_pages = int(num//15+1) # 豆瓣每页展示15部电影
        list = []
        for i in range(0,num_of_pages*15,15):
            print('获取电影 {}/{} ...'.format(i,num))
            page_i = self.get_response(i)

            for movie in page_i.find_all('div',{'class':'item'}):
                name = movie.find('a',{'class':'nbg'})
                tit = name['title']
                link = name['href']
                popularity, type = self.get_movie_info(link)
                list.append([tit,popularity,type])

        return list

    def get_movie_info(self,movie_url):
        #根据电影id，爬取影片类型
        s = requests.Session()
        header = self.set_header()
        response = s.get(movie_url, headers=header).content
        page = BeautifulSoup(response, 'lxml')
        types = [type.text for type in page.find_all('span',{'property':'v:genre'})]
        popularity = page.find('span',{'property':'v:votes'})
        if popularity!= None: popularity = popularity.text
        return popularity, types

#zkx = netease_spider('186591345')
#print(zkx.movies)

