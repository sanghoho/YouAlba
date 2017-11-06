from pymongo import MongoClient, ASCENDING
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup

app = Flask(__name__)

client = MongoClient()
# client = pymongo.MongoClient()  #pymongo만 import 할시

db = client.TT  # MongoClient 아무거나 점찍고 뒤에 쓸 수 있음
collection = db["2"]  # collect


@app.route('/')
def entrance():
    if 'user' in session:
        return render_template("entrance2.html")
    return render_template("entrance2.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['user'] = request.form['user']
        return redirect(url_for('entrance'))


@app.route('/logout')
def logout():
    # remove the username from the session if its there
    session.pop('user', None)
    return redirect(url_for('entrance'))


@app.route('/store')
def store():
    if 'user' in session:
        pageNum = request.args.get('pageNum', '')
        gu = request.args.get('gu', '')
        # posts = collection.find().skip(10 * int(pageNum)).limit(10 * (1 + int(pageNum)))
        if gu is not "":
            posts = collection.find({"gu": gu}).sort("name",ASCENDING)
        else:
            posts = collection.find().sort("name",ASCENDING)
        return render_template("location.html", **locals())
    return "Bad Request"

#
@app.route('/store/add', methods=["GET", "POST"])
def store_add():
    if request.method == "POST":
        # DB에 데이터 쓰기
        # collection.save({
        #     "title": request.form["title"],
        #     "content": request.form["content"]
        # })
        # return redirect('/store/add')
        add_review = {'name': request.form["name"],
        'Pay': request.form["pay"],
        'Subtract': request.form["deduct"],
        'Working' : request.form["period"]}
        return render_template('location_step1.html', data = add_review)
    else:
        return render_template('location_step1.html')


# @app.route('/store')
# def store():
#     if 'user' in session:
#         return render_template("Add-Review-Store.html")
#     return "Bad Request"

# @app.route('/static/img/<filename>')
# def static_img(filename):
#     return send_from_directory('static', filename)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#
if __name__ == '__main__':
    app.run(port = 5000,debug=True)
