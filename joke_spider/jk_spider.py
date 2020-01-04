"""
爬取笑话，存入表中
"""
import logging
import os
import random
import requests
import sys
from lxml import etree
from info.constants import ua_pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


def public_log(logger_name='default_log', log_file=os.path.join(BASE_DIR, 'logs', 'log'), level=logging.DEBUG):
    """
    重新定义下logger 对象
    :param logger_name:
    :param log_file:
    :param level:
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # 创建控制台　console.handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 创建文件handler
    fh = logging.FileHandler(filename=log_file, encoding='utf-8')
    # 设置写入文件的日志等级
    fh.setLevel(logging.DEBUG)
    # 创建日志格式
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(name)s %(levelname)s %(message)s')

    # 添加formatter
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把ch fh 添加到logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


class Response(object):
    """
    构造一个响应类,对于请求失败的返回的值
    """
    def __init__(self, url):
        self.status_code = 999
        self.content = ""
        self.url = url


def req_res(url=None, headers=None, params=None, data=None, proxies=None, timeout=6, method="GET", logger=None):
    """
    请求参数,获取响应,返回响应
    :param url:
    :param headers:
    :param params:
    :param data:
    :param proxies:
    :param timeout:
    :param method:
    :return:
    """
    response = Response(url)
    try:
        if method == "GET":
            response = requests.get(url=url, headers=headers, params=params,
                                    proxies=proxies, verify=False,
                                    allow_redirects=False, timeout=timeout)
        else:
            response = requests.post(url=url, headers=headers, data=data,
                                     proxies=proxies, verify=False,
                                     allow_redirects=False, timeout=timeout)
    except Exception as e:
        logger.info("请求失败: {}".format(e))
        pass
    finally:
        return response


class JSpider(object):

    def __init__(self):
        self.base_url = "https://m.zol.com.cn/xiaohua/"
        self.logger = public_log()
        pass

    def get_detail_content(self):
        pass

    def run(self):
        resp = req_res(url=self.base_url, headers={"User-Agent": random.choice(ua_pool)}, logger=self.logger)
        if resp.status_code != 200:
            self.logger.info("请求失败")
            return
        html_et = etree.HTML(resp.content.decode('gbk'))
        joke_url_list = html_et.xpath('//div[@class="joke-section"]/a/@href')
        print("joke_url_list", joke_url_list)
        pass


if __name__ == '__main__':
    j_spider = JSpider()
    j_spider.run()

