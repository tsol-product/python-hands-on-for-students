# -*- coding: utf-8 -*-
'''
初期設定とモジュール化
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask を app として扱う
app = Flask(__name__)

# flaskr/config.py から設定を読み込み
app.config.from_object('flaskr.config')

# app で SQLAlchemy を使用し db として扱う
db = SQLAlchemy(app)

import flaskr.views
