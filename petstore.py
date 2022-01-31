from flask import Flask, request, jsonify
import json
#import pandas as pd
from PIL import Image as PImage
import os

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

@app.route('/pet/<id>/uploadImage', methods = ['POST']) 
def pet_image(id):
    record = json.loads(request.data)
    pet_id = id
    additional_metadata = record['additionalMetadata']
    img  = PImage.open(record['file'])
    head, tail = os.path.split(record['file'])
    destination = os.getcwd()+'/data/photos/'+ tail
    img.save(destination, 'JPEG')
    try:
        with open('/Users/nsuguitan/git/pet-store-api/data/pet.txt', 'r') as f:
            data = f.read()
            records = json.loads(data)
            for item in records:
                    print("Item:",item['id'])
                    print("PetId:", pet_id)
                    print(int(pet_id) == int(item['id']))
                    if int(item['id']) == int(pet_id):
                        item['photoUrls'].append(destination)
                        with open('/Users/nsuguitan/git/pet-store-api/data/pet.txt', 'w') as f:
                            f.write(json.dumps(records, indent=2))
                            return jsonify(records)
    except ValueError:
        return 'A pet with this ID does not exist in our database, please try a different ID'

@app.route('/pet/<id>', methods = ['DELETE']) 
def pet_delete(id):
    with open('/Users/nsuguitan/git/pet-store-api/data/pet.txt', 'r') as f:
            data = f.read()
            records = json.loads(data)
            #records = [x for x in records if int(x['id']) != int(id)]
            #filter applied to remove pet with ID given
            records = list(filter(lambda x: int(x['id']) != int(id), records))
    #overwrite existing file with record removed
    with open('/Users/nsuguitan/git/pet-store-api/data/pet.txt', 'w') as f:
            f.write(json.dumps(records, indent=2))
            return "Deletion of ped id:" + str(id)
if __name__ == "__main__":
    app.run(debug=True)