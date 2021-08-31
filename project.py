from flask import Flask,jsonify,request

#creating constructor
app = Flask(__name__)

tasks = [
    {
        'id':1,
        'Name':'Raju',
        'Contact':'9987644456',
        'done':False,
    },
    {
        'id':2,
        'Name':'RAhul',
        'Contact':'9876543222',
        'done':False,
    }
]
 
#assigning task
@app.route('/')
def helloworld():
    return 'helloworld' 

@app.route('/add-data',methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide valid data'
        },400)
    task = {
        'id':tasks[-1]['id'] + 1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',''),
        'done':False,
    }
    tasks.append(task)
    return jsonify({
            'status':'success',
            'message':'Successfully loaded'
        })

@app.route('/get-data')
def get_task():
    return jsonify({
            'data':tasks  
        })


#running
if __name__ == '__main__':
    app.run()