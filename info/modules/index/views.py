from flask import render_template, current_app, jsonify

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

