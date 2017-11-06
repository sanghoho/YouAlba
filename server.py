import re
from pymongo import MongoClient
from flask import Flask, render_template, redirect, request, url_for, session, flash, Markup
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'Nosecret'


# client = MongoClient()

# db = client["nrnr"]
# collection_user, collection_place = db.User_info, db.Place_info


# 0. 대문 페이지
@app.route("/", methods=["GET", "POST"])
def main():
    """
    로그인 눌렀을 경우
     1. 회원 -> '/'로 리다이렉트
     2. 비회원 -> '/signup'으로 리다이렉트
     jinja2에서 로그인 정보 받아와서 상단바 변형
     """
    # if request.method == 'POST':
    #     if request.form["isMember"]:
    #         return redirect('/')
    #     else:
    #         return redirect('/signup')
    if request.method == 'POST':
        return  ["user"] + request.form["content"]
    else:
        # place = ####
        return render_template('facebook.html', place = place)

#
# 0.1. 로그인 페이지
@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    프로필 디자인에 따라 달라질듯
    Step1, Step2, Step3?
    """
    if request.method == 'POST':
        if request.form["isMember"]:
            pass
        else:
            return redirect('/signup')

    else:
        return render_template('map.html')

#
# 1. 위치기반
@app.route('/store', methods=["GET", "POST"])
def store():
    """
    클릭이벤트 발생할 때마다 다시 필터링해서 출력
    지도에는 리스트...
    오른쪽 글목록에는 20개씩...
    :return:
    """
    pageNum = request.args.get('pageNum', '')
    posts = collection_place.find({"gu": re.compile(place_id)}).skip(0).limit(20)
    return render_template('location.html', posts=posts)

#
## 1.1. 위치기반 매장 상세
@app.route('/store', methods=["GET", "POST"])
def location_detail():
    # <a href="/store?_id={{post._id}}"></a>
    # 위의 페이지에서 각 제목에 이런 href 걸려있어야됨
    _id = request.args.get('_id', '')
    post = collection_place.find_one({"_id": ObjectId(_id)})  # path variable querry string
    return render_template('detail.html', post=post)


## 1.2. 위치기반 리뷰 추가
@app.route('/store/add', methods=["GET", "POST"])
def location_add():
    if request.method == 'POST':
        # DB에 데이터 쓰기
        # collection.save({
        #     "title": request.form["title"],
        #     "content": request.form["content"]
        # })
        return redirect('/store')
    else:
        return render_template('add.html')

#
if __name__ == '__main__':
    app.run(debug=True, port=5000)
