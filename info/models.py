"""
    数据库表模型定义处
"""
from datetime import datetime

from info import db


class BaseModel(object):
    """
    模型基类，为每个模型补充创建时间和更新时间以及是否删除
    """
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_delete = db.Column(db.Integer, default=1)


class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "info_user"

    id = db.Column(db.Integer, primary_key=True, index=True)
    nick_name = db.Column(db.String(32), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    avatar_url = db.Column(db.String(512))
    mobile = db.Column(db.String(11), unique=True, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.now)
    is_admin = db.Column(db.Boolean, default=False)
    signature = db.Column(db.String(512))
    gender = db.Column(
        db.Enum(
            "MAN",
            "WOMAN"
        ),
        default="MAN"
    )
    news_list = db.relationship("News", backref="user", lazy="dynamic")


class News(BaseModel, db.Model):
    """
    资讯
    """
    __tablename__ = "info_news"

    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(256), nullable=False)
    source = db.Column(db.String(64), nullable=False)
    digest = db.Column(db.String(512), nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    clicks = db.Column(db.Integer, default=0)
    index_image_url = db.Column(db.String(256))
    category_id = db.Column(db.Integer, db.ForeignKey("info_category.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("info_user.id"))
    status = db.Column(db.Integer, default=0)
    reason = db.Column(db.String(256))


class Category(BaseModel, db.Model):
    """资讯的分类"""
    __tablename__ = 'info_category'
    # 分类编号
    id = db.Column(db.Integer, primary_key=True)
    # 分类名称
    name = db.Column(db.String(64), nullable=False)
    # 关系
    news_list = db.relationship('News', backref='category', lazy='dynamic')

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "name": self.name
        }
        return resp_dict


class Joke(BaseModel, db.Model):
    """笑话表"""
    __tablename__ = 'info_joke'
    # 主键
    id = db.Column(db.Integer, primary_key=True, index=True)
    # 内容
    joke_content = db.Column(db.String(256), unique=True)
    # title 标题
    title = db.Column(db.String(256), index=True)
