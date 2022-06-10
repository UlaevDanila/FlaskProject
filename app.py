from flask import Flask, render_template, request, flash

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def HomePage():
    return render_template('homepage.html')

@app.route('/FreedomPage.html')
def FreedomPage():
    return render_template('FreedomPage.html')

@app.route('/ElementarySchoolPage.html')
def ElementarySchoolPage():
    return render_template('ElementarySchoolPage.html')

@app.route('/LovePage.html')
def LovePage():
    return render_template('LovePage.html')

@app.route('/OtherPage.html')
def OtherPage():
    return render_template('OtherPage.html')

if __name__ == '__main__':
    app.run()
