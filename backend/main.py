#contains main routes and endpoints

from flask import request, jsonify
from config import app, db
from models import Contact

#decorator (root, request type)
@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})


@app.route("/contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("first_name")
    last_name = request.json.get("last_name")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "Ypu must include first name, last name and email"}), 
            400,
        )
    new_contact = Contact(first_name = 'firstName')

if __name__ == '__main__':
    #create database
    with app.app_context():
        db.create_all()

    app.run(debug=True)