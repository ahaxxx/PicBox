# -*- encoding:utf-8 -*-
# -*- python:3.8     -*-
# -*- author:LiuBX   -*-
import os
import time
from model import Image
from exts import db

def creat_path(path):
    # 生成文件储存目录
    abspath = './pic_data/' + path
    isExists=os.path.exists(abspath)
    if isExists:
        print("目录已存在")
    else:
        os.makedirs(abspath)
    return abspath

def file_name(username,filetype):
    # 重命名上传的文件，命名规则为 username_timestamp.filetype
    filename = username + '_' + str(time.time()) + '.' + filetype
    return filename

def file_url(username,filename):
    # 用于生成相对站点的图片url
    file_url = 'show/'+username+'/'+filename
    return file_url

def write_database(username,filename,filepath,fileurl,filetype,size_h,size_w,tag):
    # 用于将上传的图片信息写入数据库
    image_msg = Image(  username = username,
                        filename = filename,
                        filepath = filepath,
                        fileurl = fileurl,
                        filetype = filetype,
                        size_h = size_h,
                        size_w = size_w,
                        tag = tag
                        )
    db.session.add(image_msg)
    db.session.commit()
    print("写入成功")