from flask import Flask, request, jsonify
import json
import pandas as pd

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello Cool Cat!'

@app.route('/pet', methods = ['POST', 'PUT'])
def pet_records():
    if request.method == 'PUT':
        # Update an existing pet
        #Get record from the request
        record = json.loads(request.data)
        with open('/Users/nsuguitan/git/pet-store-api/data/pet.txt', 'r') as f:
            data = f.read()
        records = json.loads(data)
        for item in records:
                #print("Item:",item['id'])
                #print("record:",record['id'])
                if item['id'] == record['id']:
                    item.update(record)
    if request.method == 'POST':
        #Add new record
        #Get new record from the request
        record = json.loads(request.data)
        #read data from txt file
        with open('/Users/nsuguitan/git/pet-store-api/data/pet.txt', 'r') as f:
            data = f.read()
        if not data:
            #If there is no data in the file, this is the first record
            records = [record]
        else:
            #Otherwise append the record to existing records
            records = json.loads(data)
            #Checking to make sure the pet isn't already there
            #If it is, we will not write the new pet and let the user know
            for item in records:
                #print("Item:",item['id'])
                #print("record:",record['id'])
                if item['id'] == record['id']:
                    return 'That pet is already in the system dummy!'
            records.append(record)
    with open('/Users/nsuguitan/git/pet-store-api/data/pet.txt', 'w') as f:
        #update the file
        f.write(json.dumps(records, indent=2))
        return jsonify(record)


if __name__ == "__main__":
    app.run(debug=True)