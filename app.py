from flask import Flask, render_template, request, url_for ,send_from_directory
from datetime import datetime 



app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
   


     if request.method == 'POST':
        # Get the data from the POST request
        name= request.form['name']
        email = request.form['email']
        # print(name)
        # print(email)
        return  render_template('index.html')
     return render_template('index.html')

# @app.route('/favicon.ico')
# def fav():
#     return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')



if __name__ == '__main__':
    app.run()
    
    # app.run(host='0.0.0.0', port=80)
