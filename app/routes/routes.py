from flask import Blueprint
from app.controllers.controllers import update_item
from app.models.models import Product  # Update the import path

# Definir un blueprint para la actualización de productos
update_bp = Blueprint('update_bp', __name__)

update_bp.route('/update_item/<int:item_id>', methods=['PUT'])(update_item)

