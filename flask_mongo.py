from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

#Example dbname in python
app.config['MONGO_DBNAME'] = 'restdb'

#Example port for MongoDB port setup
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

mongo = PyMongo(app)

#READ ALL ENTRIES
@app.route('/stars',methods=['GET'])
def get_all_frameworks():
    star = mongo.db.stars
    output = []
    for q in star.find():
        output.append({'name': q['name'],'distance': q['distance']})
    return jsonify({'result':output})

# READ ID wise
@app.route('/stars/<name>',methods=['GET'])
def get_single_frameworks(name):
    output = []
    star = mongo.db.stars
    q = star.find_one({'name': name})
    if q:
        output.append({'name': q['name'],'distance': q['distance']})
    else:
        output =[]
    return jsonify({'result':output})

#CREATE
@app.route('/stars',methods=['POST'])
def add_single_framework():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']

    #Function will assign star_id
    star_id = star.insert({'name':name,'distance':distance})
    new_star = star.find_one({'_id': star_id})
    output = {'name':new_star['name'],'distance':new_star['distance']}
    return jsonify({'result': output})

#UPDATE
@app.route('/stars/<name>',methods=['PUT'])
def update_single_framework(name):
    star = mongo.db.stars
    new_star = star.find_one({'name': name})
    new_star['name'] = request.json['name']
    new_star['distance'] = request.json['distance']
    star.save(new_star)
    return jsonify({'result': 'Update successful'})

#DELETE
@app.route('/stars/<name>',methods=['DELETE'])
def delete_single_framework(name):
    star = mongo.db.stars
    new_star = star.find_one({'name': name})
    star.delete_one(new_star)
    return jsonify({'result': 'Delete successful'})


if __name__=='__main__':
    app.run(debug=True)
    #Uncomment the line in case the port number you want to give manually
    #app.run(debug=True,port=5002)
