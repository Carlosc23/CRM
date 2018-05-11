import os

from flask import Flask, render_template, request

import urllib3
import sys
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

urllib3.disable_warnings()

cloudinary.config(
    cloud_name = 'drc2h3d9n',
    api_key = '596916237749538',
    api_secret = '78HRHwp-Ceo7DktRXeMh2gDNdU0'
    )


UPLOAD_FOLDER = 'static/tmpImages'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        print("hola")
        print(request.form["option"])
        for i in request.form:
            print(i, "-->", request.form[i])
        f = request.files['file']
        filename = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(filename)
        print(filename)
       # img = cloudinary.uploader.upload(UPLOAD_FOLDER+'/'+f.filename)
       # genurl = img['url']
       # os.remove(filename)
       # print("URL",'--> ',genurl)
        #insert_patient('(select max(id) from paciente)+1', idprofesion, nombre, apellido, dpi, sexo, telefono, correo, fechanacimiento, foto,
         #              usuariotwitter, pagomedicinas=0):
        return render_template('add.html')
    else:
        return render_template('add.html')


if __name__ == '__main__':
    app.run()
