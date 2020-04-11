# -*- encoding:utf-8 -*-
# -*- python:3.8     -*-
# -*- author:LiuBX   -*-

from flask import Flask,render_template,request,make_response
from exts import db
from configs import WEB_HOST
import function
import base64
import io
import model
from PIL import Image


def create_app():
# flask初始化
    app = Flask(__name__)
    app.config.from_object('configs')
    db.init_app(app)
    return app

app = create_app()

@app.route('/')
def index():
# web根目录
    return render_template("upload.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
# 上传文件储存
    error = ''
    tag = ''
    username = 'null'
    save_path = function.creat_path(username)
    file_name = function.file_name(username,'jpg')
    file_path_name = save_path + '/' + file_name
    file_url = function.file_url(username,file_name)
    print(file_path_name)
    if request.method == 'POST':
        f = request.files['file']           # 接受POST表单中的图片
        f.save(file_path_name)              # 上传图片保存至服务器
        img = Image.open(file_path_name)    
        w,h = img.size                      # 获取图片尺寸保存
        function.write_database(username,file_name,file_path_name,file_url,'jpg',h,w,tag)
        return render_template("upload_success.html",url = WEB_HOST + file_url)
    else:
        return render_template("upload_failed.html",error = error)

@app.route('/show/<string:username>/<string:filename>')
def show(username,filename):
# 单张图片request返回，本地址可以储存作为图片URL
    img_path = 'pic_data/'+username+'/'+filename
    figfile = open(img_path, 'rb').read()
    img = make_response(figfile)
    img.headers['Content-Type'] = 'image/png'
    return img

@app.route('/mypic/<string:username>')
def mypic(username):
# 存在于个人页中，用于展现用户上传的所有图片
    pics = model.Image.query.filter_by(username=username).all()
    return render_template("mypic.html",WEB_HOST = WEB_HOST,pics=pics)