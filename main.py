from os import sendfile
from flask import Flask,render_template,request,send_from_directory
import pytesseract
import os
from PIL import Image

app = Flask('__name__')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(APP_ROOT,'static/images/')


@app.route('/', methods=["GET","POST"])
def index():
    destination = "/".join([target, 'ip.png'])

    if request.method == 'GET':
        return render_template('index.html')
    if request.method ==    'POST':
        fl = request.files['file']
        print("file params "+ str(fl.content_type))
        if fl.content_type not in ['image/png','image/jpeg','image/tif']:
            return render_template('index.html',errmsg="Please use valid image file! (jpg,png,jpeg,tif)")
        fl.save(destination)
        pytesseract.pytesseract.tesseract_cmd = './.apt/usr/bin/tesseract'
        txt = pytesseract.image_to_string(Image.open(destination))
        return render_template('result.html',scmsg="Success !! OCR completed !", outputtxt=txt)



# if __name__ == '__main__':
#     uvicorn.run(app)
    # app.run(debug = True)
