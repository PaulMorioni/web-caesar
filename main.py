from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" id="rot" value="0">
            <textarea rows="10" cols="30" id="box" name="box">{0}</textarea>
            <input type="submit" value="Submit">

        </form>
    </body>
</html>S
"""
@app.route("/", methods=['POST'])
def encrypt():
    text = str(request.form['box'])
    rot = int(request.form['rot'])
    encrypted = rotate_string(text,rot)
    return form.format(encrypted)

@app.route("/")
def index():
    empty_string = ""
    return form.format(empty_string)
    
    

    



app.run()