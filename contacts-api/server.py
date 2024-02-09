from flask import Flask, request

app = Flask(__name__)

next_id = 3
contacts = [
    {'id': "1", 'name': 'Foo', 'phone': '123-456-789'},
    {'id': "2", 'name': 'Bar', 'phone': '123-456-789'}
]

@app.route('/hello')
def hello_route():
    print('received request on /Hello endpoint')
    return 'Hello'

@app.get('/contacts')
def list_contacts():
    return contacts

@app.get('/contacts/<id>')
def read_single_contact(id):
    return ([t for t in contacts if t['id'] == id]) or '404 not found'

@app.post('/contacts')
def create_contact():
    global next_id
    new_contact = {
        'id': f'{next_id}',
        'name': request.json['name'],
        'phone': request.json['phone']
    }
    contacts.append(new_contact)
    next_id += 1
    return new_contact

@app.put('/contacts/<id>')
def update_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contact['name'] = request.json['name'] if 'name' in request.json else contact['name']
            contact['phone'] = request.json['phone'] if 'phone' in request.json else contact['phone']
            return contact
    return "Contact not found with given id"

@app.delete('/contacts/<id>')
def delete_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contacts.remove(contact)
            return contact
    return "Contact not found with given id"

if __name__ == '__main__':
    app.run(debug=True)