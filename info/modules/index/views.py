import hashlib

from flask import render_template, current_app, jsonify, request, redirect, url_for, abort

from info.constants import resp_success, WECHAT_TOKEN
from info.models import Category
from . import index_blue


@index_blue.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/MyLove.ico')


@index_blue.route('/')
def index():
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


@index_blue.route('/wechatInfo')
def wechat_info():
    # 获取微信的信息
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    if not all([signature, timestamp, nonce, echostr]):
        abort(400)

    # 按照微信的要求排序
    li = [WECHAT_TOKEN, timestamp, nonce]
    # sha1加密
    sign = hashlib.sha1("".join(li.sort())).hexdiges()
    # 将计算的签名和微信值进行对比
    if signature != sign:
        abort(403)
    else:
        return echostr





