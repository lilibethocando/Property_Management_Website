from app import app
from flask import render_template, request, jsonify
from app.models import Apartment

# Create Apartment
@app.route('/apartments', methods=['POST'])
def create_apartment():
    apartment = Apartment()

    data = request.json
    required_fields = ['name', 'description', 'rent_amount']

    for field in required_fields:
        if not data:
            return jsonify({'error': 'Request data is required'}), 400
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
        

    name = data['name']
    description = data['description']
    rent_amount = data['rent_amount']
    
    # Create new apartment
    new_apartment = apartment.create_apartment(name, description, rent_amount)
    return jsonify(new_apartment.serialize()), 201

# Read All Apartments
@app.route('/apartments', methods=['GET'])
def get_all_apartments():
    apartments = Apartment.query.all()
    return jsonify([apartment.serialize() for apartment in apartments])

# Read Apartment by ID
@app.route('/apartments/<int:apartment_id>', methods=['GET'])
def get_apartment(apartment_id):
    apartment = Apartment.query.get(apartment_id)
    if apartment:
        return jsonify(apartment.serialize())
    else:
        return jsonify({'error': 'Apartment not found'}), 404

# Update Apartment
@app.route('/apartments/<int:apartment_id>', methods=['PUT'])
def update_apartment(apartment_id):
    # Retrieve the apartment object from the database
    apartment = Apartment.query.get(apartment_id)
    if apartment:
        # Parse request data
        data = request.json
        if not data:
            return jsonify({'error': 'Request data is required'}), 400
        # Update the apartment object with the provided data
        updated_apartment = apartment.update_apartment(apartment_id, **data)
        if updated_apartment:
            return jsonify(updated_apartment.serialize())
        else:
            return jsonify({'error': 'Failed to update apartment'}), 500
    else:
        return jsonify({'error': 'Apartment not found'}), 404


# Delete Apartment
@app.route('/apartments/<int:apartment_id>', methods=['DELETE'])
def delete_apartment(apartment_id):
    apartment = Apartment.query.get(apartment_id)
    if apartment:
        success = apartment.delete_apartment(apartment_id)
        if success:
            return jsonify({'message': 'Apartment deleted successfully'})
    return jsonify({'error': 'Apartment not found'}), 404
