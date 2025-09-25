
import os


def urllist():
    list_file = os.path.join('piclist/baidu.txt')
    url_list = []
    with open(list_file, 'r') as f:
        url_list = [line.strip() for line in f]
    return url_list[:]