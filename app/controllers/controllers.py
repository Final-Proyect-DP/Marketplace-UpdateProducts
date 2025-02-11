from flask import request, jsonify
from app.models.models import Product, Category  # Update the import path
from app.extensions.extensions import db
import requests
import base64  # To encode the image in Base64
import os  # Add import for os

def update_item(item_id):
    data = request.get_json()  # Use JSON data instead of form data
    image_data = data.get('image_data')  # Get image data from JSON

    # Find the product by ID
    product = Product.query.get(item_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    # Update product fields
    if 'name' in data:
        product.name = data['name']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'userId' in data:
        product.userId = data['userId']
    if 'category_id' in data:
        category_id = data['category_id']
        category = Category.query.filter_by(id=category_id).first()
        if not category:
            return jsonify({"message": "Category not found"}), 404
        product.category_id = category_id

    # Update image if provided
    if image_data:
        product.image_data = base64.b64decode(image_data)

    try:
        db.session.commit()
        return jsonify({
            "message": "Product updated successfully",
            "product": product.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error updating product: {str(e)}"}), 500
