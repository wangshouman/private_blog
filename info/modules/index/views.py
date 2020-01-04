import hashlib

import time
import xmltodict
from flask import render_template, current_app, jsonify, request, redirect, url_for, abort, make_response

from info.constants import resp_success, WECHAT_TOKEN
from info.models import Category
from . import index_blue


@index_blue.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/MyLove.ico')


@index_blue.route('/')
def index():
    current_app.logger.info("1111")
    # 查询出category表的数据
    category_list = [_.name for _ in Category.query.all()]
    return render_template('news/html/index.html', category_list=category_list)


@index_blue.route('/loginPage')
def login_page():

    return render_template('news/html/login.html')


@index_blue.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    return jsonify(resp_success)


@index_blue.route('/detail')
def detail_page():
    return render_template('news/html/detail.html')


@index_blue.route('/getArticle/<int:news_id>', methods=['GET'])
def get_article(news_id):
    print(news_id)
    html_content = {
        "content": "<p>在不能满足设备安全运行的恶劣天气，无法抗拒的自然灾害情况下"
                   "（如雷电、雨雪、冰雹、大雾、暴雨、台风等），景区部分项目将临时关闭或部分关闭，表演会取消或部分取消。1</p><p>&nbsp;</p>"}
    return jsonify(html_content)


@index_blue.route('/wechatInfo', methods=["GET", "POST"])
def wechat_info():
    if request.method == 'GET':
        signature = request.args.get("signature")
        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")
        echostr = request.args.get("echostr")
        current_app.logger.info("1111")
        if not all([signature, timestamp, nonce, echostr]):
            abort(400)
        current_app.logger.info("1111")
        # 按照微信的要求排序
        li = [WECHAT_TOKEN, timestamp, nonce]
        li.sort()
        tmp_str = "".join(li)
        # sha1加密
        sign = hashlib.sha1(tmp_str.encode()).hexdigest()
        # 将计算的签名和微信值进行对比
        if signature != sign:
            abort(403)
        else:
            return echostr
    else:
        xml_str = request.data
        xml_dict = xmltodict.parse(xml_str).get('xml')
        tmp_dict = dict()
        for _k, _v in xml_dict.items():
            tmp_dict[_k] = _v
        ToUserName = tmp_dict.get('ToUserName')
        FromUserName = tmp_dict.get('FromUserName')
        CreateTime = tmp_dict.get('CreateTime')
        MsgType = tmp_dict.get('MsgType')
        Content = '一起学习，一起进步！'
        if MsgType == 'text':
            Content = tmp_dict.get('Content')
            MsgId = tmp_dict.get('MsgId')
            print("Content", Content)
        elif MsgType == 'image':
            MsgId = tmp_dict.get('MsgId')
            MediaId = tmp_dict.get('MediaId')
            PicUrl = tmp_dict.get('PicUrl')
            print("PicUrl", PicUrl)
        elif MsgType == 'voice':
            MediaId = tmp_dict.get('MediaId')
            Format = tmp_dict.get('Format')
            MsgId = tmp_dict.get('MsgId')
            Recognition = tmp_dict.get('Recognition')
        elif MsgType == 'event':
            Event = tmp_dict.get('Event')
            EventKey = tmp_dict.get('EventKey')

        resp_dict = {
            "xml": {
                "ToUserName":  FromUserName,
                "FromUserName": ToUserName,
                "CreateTime": int(time.time()),
                "MsgType": MsgType,
                "Content": Content,
            }
        }

        resp_xml_str = xmltodict.unparse(resp_dict)

        return resp_xml_str






