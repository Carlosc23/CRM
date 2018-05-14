import os

from flask import Flask, render_template, request

import urllib3
import sys
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

from crm_actions.module1_actions import get_idpaciente, insert_patient, get_profession, get_paciente, delete_patient


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

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        for i in request.form:
            print(i, "-->", request.form[i])
        searchterm = request.form['search']
        filter = request.form['filter']
        data =  get_paciente(filter, searchterm)
        for item in data:
            print(item)
        return render_template('search.html',data=data)
    return render_template('search.html')

@app.route('/delete/<paciente_id>', methods=['POST'])
def delete(paciente_id):
    delete_patient(paciente_id)
    print(paciente_id)
    return render_template('deleteProfile.html')
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
        id = get_idpaciente()
        print(id)
        img = cloudinary.uploader.upload(UPLOAD_FOLDER+'/'+f.filename)
        genurl = img['url']
        os.remove(filename)
        print("URL",'--> ',genurl)
        print(request.form['Name'])
        print(request.form['LastName'])
        print(request.form['DPI'])
        print(request.form['option'])
        print(request.form['Telephone'])
        print(request.form['Email'])
        print(request.form['Birth'])
        print(request.form['Twitter'])
        insert_patient(id, get_profession(request.form['TCareer'],request.form['Career']), request.form['Name'], request.form['LastName'], request.form['DPI'],
                       request.form['option'],
                       request.form['Telephone'], request.form['Email'], request.form['Birth'], genurl,
                       request.form['Twitter'], 0)
        return render_template('add.html')
    else:
        return render_template('add.html')


if __name__ == '__main__':
    app.run()
