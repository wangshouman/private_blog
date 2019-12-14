from flask import render_template, current_app, jsonify, request, redirect, url_for

from info.constants import resp_success
from info.models import Category
from . import index_blue


@index_blue.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/MyLove.ico')


@index_blue.route('/index')
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
    return redirect(url_for('index.detail_page'))




