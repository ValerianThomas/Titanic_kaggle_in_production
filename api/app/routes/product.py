from flask import request, jsonify, Response, Blueprint
from ..models.Product import Product, ProductSchema

product_end_point = Blueprint('product_end_point', __name__)
product_schema = ProductSchema()

@product_end_point.route('/',methods = ['GET'])
def get_all_products ():
  all_product = Product.query.all()
  return jsonify({"success":True, "data":all_product})


@product_end_point.route('/',methods = ['POST'])
def create_new_product ():
  req_data = request.get_json()

  data, error = product_schema.load(req_data)

  if error :
    return jsonify({"success":False, "error":error})
  
  # see if product already exist
  product = Product.query.filter_by(name=data.get('name')).first()

  if product :
    return jsonify({"success":False, "error":"product already exist"})

  new_product = Product(data)
  ser_product = product_schema.dump(new_product).data

  return jsonify({"success": True, "data":ser_product})

@product_end_point.route('/<int:product_id>',methods = ['PUT'])
def update_product(product_id):
  req_data = request.get_json()

  data, error = product_schema.load(req_data, partial=True)

  if error :
    return jsonify({"success":False, "error":error})

  product = Product.query.get(product_id)

  if not product :
    return jsonify({"success":False, "error":"this product id doesn't exist"})

  product.update(data)

  ser_product = product_schema.dump(product).data

  return jsonify({"success": True, "data":ser_product})



@product_end_point.route('/<int:product_id>',methods = ['DELETE'])
def delete_product(product_id):

  product = Product.query.get(product_id)
  if not product :
    return jsonify({"success":False, "error":"this product id doesn't exist"})

  product.delete()

  return jsonify({"success": True, "message":"product deleted"})




