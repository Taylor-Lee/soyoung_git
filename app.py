import pymongo
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = pymongo.MongoClient('localhost', 27017)
db = client.syproject
db.createCollection(foodcollection, [options])


@app.route('/')
def home():
    return render_template('my_fridge.html')


@app.route('/food', methods=['POST'])
def post_food():

    name = request.form['name']
    date = request.form['date']
    comment = request.form['comment']

    foodcollection = {
       'name': name,
       'date': date,
       'comment': comment,
    }

    return jsonify({'result': 'success', 'msg': '추가되었습니다'})


# @app.route('/food', methods=['GET'])
# def read_food():

#     result = list(db.foodcollection.find({}, {'_id': False}))

#     return jsonify({'result': 'success', 'foodcollection': result})
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)
