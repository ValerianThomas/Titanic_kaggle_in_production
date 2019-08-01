from marshmallow import fields, Schema
from .. import db
class Product (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    dscription = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
      self.name = name
      self.description = description
      self.price = price
      self.qty = qty

    def save(self):
      db.session.add(self)
      db.session.commit()
    
    def delete(self):
      db.session.delete(self)
      db.session.commit()

    def update(self, data):
      for key, item in data.items():
        setattr(self, key, item)
      db.session.commit()



class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    qty = fields.Int(required=True)