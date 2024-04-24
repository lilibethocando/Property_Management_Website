from app import app, db
from flask import render_template, request, jsonify
from sqlalchemy import or_
from app.models import Complaint

@app.route('/complaints', methods=['POST'])
def complaint():
    data = request.get_json()
    complaint = Complaint(data['name'], data['email'], data['message'])
    db.session.add(complaint)
    db.session.commit()
    return jsonify({'message': 'Complaint submitted successfully!'})


@app.route('/complaints', methods=['GET'])
def complaints():
    complaints = Complaint.query.all()
    return jsonify([complaint.serialize() for complaint in complaints])


@app.route('/complaints/<int:complaint_id>', methods=['GET'])
def get_complaint(complaint_id):
    complaint = Complaint.query.get(complaint_id)
    if complaint:
        return jsonify(complaint.serialize())
    else:
        return jsonify({'error': 'Complaint not found'}), 404
    

@app.route('/complaints/<int:complaint_id>', methods=['PUT'])
def update_complaint(complaint_id):
    complaint = Complaint.query.get(complaint_id)
    if complaint:
        data = request.json
        if 'name' in data:
            complaint.name = data['name']
        if 'email' in data:
            complaint.email = data['email']
        if 'message' in data:
            complaint.message = data['message']
        db.session.commit()
        return jsonify(complaint.serialize())
    else:
        return jsonify({'error': 'Complaint not found'}), 404
    

@app.route('/complaints/<int:complaint_id>', methods=['DELETE'])
def delete_complaint(complaint_id):
    complaint = Complaint.query.get(complaint_id)
    if complaint:
        db.session.delete(complaint)
        db.session.commit()
        return jsonify({'message': 'Complaint deleted successfully'})
    else:
        return jsonify({'error': 'Complaint not found'}), 404
    

@app.route('/complaints/<int:complaint_id>/resolve', methods=['PUT'])
def resolve_complaint(complaint_id):
    complaint = Complaint.query.get(complaint_id)
    if complaint:
        complaint.status = 'resolved'  # Update the status to 'resolved'
        db.session.commit()
        return jsonify(complaint.serialize())
    else:
        return jsonify({'error': 'Complaint not found'}), 404

    

@app.route('/complaints/resolved', methods=['GET'])
def resolved_complaints():
    complaints = Complaint.query.filter_by(status='resolved').all()
    return jsonify([complaint.serialize() for complaint in complaints])


@app.route('/complaints/unresolved', methods=['GET'])
def unresolved_complaints():
    complaints = Complaint.query.filter(or_(Complaint.status != 'resolved', Complaint.status.is_(None))).all()
    return jsonify([complaint.serialize() for complaint in complaints])



@app.route('/complaints/count', methods=['GET'])
def count_complaints():
    count = Complaint.query.count()
    return jsonify({'count': count})


