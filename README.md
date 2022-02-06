# pet-store-api
Forward Motion API Module - Create a pet store API using Python Flask

This pet store API allows you to add, update, upload images, and remove pet data to a pet.txt file. To configure this example, please do the following:<br />
1. Create a venv, activate, and clone this repository within the venv
2. install packages included in requirements.txt
3. Update [petstore.py](petstore.py) so that the filepath points to the pet.txt in this repo
4. In your venv, run the following code to export the FLASK_APP variable and launch your flask builtin server: <br />
```
$ export FLASK_APP=hello.py
$ flask run
```
5. Your built-in server should now be running. This example includes four options: <br />

| Method        | HTTP Request  | Description  |
| ------------- |-------------| -----------------------------------------|
| pet_records | POST/pet | Add new pet record |
| pet_records | PUT/pet | Update existing pet record |
| pet_image | POST/pet/&lt;id>/uploadImage | Add an image to an existing pet record |
| pet_delete | DELETE/pet/&lt;id> | Delete a pet record |

6. To start, send an http post request to add a pet. The json below can be passed as the body of the request as an example:
```
{
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "id": 12,
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "status": "available",
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ]
}
```
7. If you open pet.txt file, the new record should hav populated. Congrats! You added your first pet. Try changing the id and other values to add another pet. Or you can use the example body above for a pet_records put request (update pet) and change the name of your dog.

Bonus: If you would like to add a picture of a furry friend to the data store. follow the HTTP Request structurefor pet_image (POST/pet/&lt;id>/uploadImage) and add the following params to the body of your request: <br/>

| Param        | Example  | Description  |
| ------------- |-------------| -----------------------------------------|
| additionalMetadata | "This is a puppy photo" | A brief description of the file being uploaded |
| file | "/Users/nsuguitan/tmp/pomeranian-puppy.jpeg" | The filepath of the picture that is going to be loaded to the our data folder|

This will load the image to the data folder in the directory and add the file destination to the "photoUrls" attribute for your pet. 
