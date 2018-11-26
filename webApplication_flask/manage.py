# -*- coding: utf-8 -*-
'''
flaskrの起動 
'''

from flaskr import app

# URL, ポート, デバックモードの設定
app.run(host='127.0.0.1', port=5000, debug=True)
