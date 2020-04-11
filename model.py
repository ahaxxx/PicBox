# -*- encoding:utf-8 -*-
# -*- python:3.8     -*-
# -*- author:LiuBX   -*-
from exts import db
from datetime import datetime

class Image(db.Model):
    __tablename__ = 'image_table'
    uid = db.Column(db.Integer,primary_key = True,autoincrement = True) # 图片上传编号
    username = db.Column(db.String(50),nullable = False)                # 上传者username
    filename = db.Column(db.String(50),nullable = False)                # 另存后的图片名
    filepath = db.Column(db.String(150),nullable = False)               # 图片在服务器中的相对储存路径
    fileurl = db.Column(db.String(150),nullable = False)                # 图片可以被调用的URL
    filetype = db.Column(db.String(50),nullable = False)                # 图片文件类型
    tag = db.Column(db.String(150),nullable = True)                     # 图片标签
    size_h = db.Column(db.Integer,nullable = False)                     # 图片高度
    size_w = db.Column(db.Integer,nullable = False)                     # 图片宽度
    img_album = db.Column(db.String(1024),nullable = True)              # 图片所属相册，默认为空(未分类)
    used_article = db.Column(db.String(2048),nullable = True)           # 引用该图片的文章，CMS预留
    add_time = db.Column(db.DateTime, default=datetime.now)             # 图片上传时间
    