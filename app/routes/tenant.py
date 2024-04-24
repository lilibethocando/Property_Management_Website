from app import app, db
from flask import render_template, request, jsonify
from app.models import Tenant, Apartment

@app.route('/tenants', methods=['GET'])
def tenants():
    tenants = Tenant.query.all()
    return jsonify([tenant.serialize() for tenant in tenants])



@app.route('/tenants', methods=['POST'])
def create_tenant():
    data = request.json
    required_fields = ['first_name', 'last_name', 'phone_number', 'apartment_id']

    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400

    first_name = data['first_name']
    last_name = data['last_name']
    phone_number = data['phone_number']
    apartment_id = data['apartment_id']

    new_tenant = Tenant(first_name=first_name, last_name=last_name, phone_number=phone_number, apartment_id=apartment_id)
    db.session.add(new_tenant)
    db.session.commit()

    return jsonify(new_tenant.serialize()), 201




@app.route('/tenants/<int:tenant_id>', methods=['GET'])
def get_tenant(tenant_id):
    tenant = Tenant.query.get(tenant_id)
    if tenant:
        return jsonify(tenant.serialize())
    else:
        return jsonify({'error': 'Tenant not found'}), 404
    

@app.route('/tenants/<int:tenant_id>', methods=['PUT'])
def update_tenant(tenant_id):
    tenant = Tenant.query.get(tenant_id)
    if tenant:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        for key, value in data.items():
            if key not in db.Model.metadata.tables['tenant'].columns:
                return jsonify({'error': f'{key} is not a valid field'}), 400
            setattr(tenant, key, value)
        db.session.commit()
        return jsonify(tenant.serialize())
    else:
        return jsonify({'error': 'Tenant not found'}), 404
    

@app.route('/tenants/<int:tenant_id>', methods=['DELETE'])
def delete_tenant(tenant_id):
    tenant = Tenant.query.get(tenant_id)
    if tenant:
        db.session.delete(tenant)
        db.session.commit()
        return jsonify({'message': 'Tenant deleted successfully'})
    else:
        return jsonify({'error': 'Tenant not found'}), 404
    
