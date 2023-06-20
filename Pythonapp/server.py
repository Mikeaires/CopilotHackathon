# write a flask server that will expose a method call "get" that will return the value of the key passed in the query string
# example: http://localhost:3000/get?key=hello
# if the key is not passed, return "key not passed"
# if the key is passed, return "hello" + key


from flask import Flask, request
import logging

app = Flask(__name__)

@app.route('/get', methods=['GET'])
def get():
    key = request.args.get('key')
    if key is None:
        return "key not passed"
    else:
        return "hello " + key
    
#Calculate days between two dates. receive by query string 2 parameters date1 and date 2 , and calcualte the days that are between those two dates.
#example: http://localhost:3000/days?date1=2020-01-01&date2=2020-01-10

@app.route('/days', methods=['GET'])
def days():
    date1 = request.args.get('date1')
    date2 = request.args.get('date2')
    if date1 is None or date2 is None:
        return "date not passed"
    else:
        return "days between dates: " + date1 + " and " + date2 + " is: " + str((int(date2[8:10]) - int(date1[8:10])))
    
#Receive by querystring a parameter called phoneNumber 
#validate phoneNumber with Spanish format, for example +34666777888
#if phoneNumber is valid return "valid"
#if phoneNumber is not valid return "invalid"
#example: http://localhost:3000/phoneNumber?phoneNumber=%2B34666777888



@app.route('/phoneNumber', methods=['GET'])
def phoneNumber():
    phoneNumber = request.args.get('phoneNumber')
    if phoneNumber is None:
        return "phoneNumber not passed"
    else:
        print(phoneNumber[0:3])
        if phoneNumber[0:3] == "+34" and len(phoneNumber) == 12:
            return "valid"
        else:
            return "invalid"


#Receive by querystring a parameter called color
#read colors.json file and return the rgba field
#get color var from querystring
#iterate for each color in colors.json to find the color
#return the code.hex field
#example: http://localhost:3000/color?color=red

@app.route('/color', methods=['GET'])
def color():
    color = request.args.get('color')
    if color is None:
        return "color not passed"
    else:
        import json
        with open('colors.json') as json_file:
            data = json.load(json_file)
            for p in data['colors']:
                if p['color'] == color:
                    return p['code']['hex']
            return "color not found"




# if the url has other methods, return "method not supported"

@app.errorhandler(404)
def page_not_found(e):
    return "method not supported"



# when server is listening, log "server is listening on port 3000"

if __name__ == '__main__':
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    logging.info('server is listening on port 3000')
    app.run(host='localhost', port=3000, debug=True)