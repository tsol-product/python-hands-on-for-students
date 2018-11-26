# -*- coding: utf-8 -*-

# __init__.py に記述された db の読み込み
from flaskr import db

# DB のデータ構造定義クラス
class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
                id=self.id, title=self.title)

# DBの作成関数
def init():
    db.create_all()
