from flask import render_template, flash, redirect, request, url_for
from app import app, db
from .forms import ParticipantForm
from .models import User, Answer

curent_user = 0 #User number who has logged in
logged_in = 0 #Set when someone is logged in 

session = {"pid":0, "username":""}
length_of_survey = 1; #Number of questions here

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = ParticipantForm()
    if form.validate_on_submit():
        
        #Store Participant details in DB
        p = User(form.username.data, form.email.data, form.age.data,
                 form.eyesightl.data, form.eyesightr.data, form.gender.data,
                 form.profession.data)
        db.session.add(p)
        db.session.commit()
        pid = p.id
        uname = p.username

        #Start session with pid and uname from DB
        session["pid"] = pid
        session["username"] = uname
        
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)


# put logout button on every page of the survey
@app.route('/logout')
def logout():
  session['pid']=0
  session['username']=""
  print session
  return redirect('/login')


@app.route('/index', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		favourite_color_chosen = request.form.get("favorite-color-chosen")
		#Update Participant information in DB with favorite color 
		participant = User.query.get(session["pid"])
        participant.favorite_color = favourite_color_chosen
        db.session.commit()


@app.route('/survey/<question_num>', methods=['GET', 'POST'])
def survey(question_num):
    image = files_for_survey[int(question_num)-1] 
    next_ques=str(int(question_num)+1)
    
    if request.method == "POST":
        dominant_color_chosen = request.form.get("dominant-color-chosen")
       
        #Answers(userid, surveynum(1,2,3), questionnum(1-10), answerstring)
        ans = Answers(session['pid'], 1, int(question_num), image+","+dominant_color_chosen)
        db.session.add(ans)
        db.session.commit()


        if int(next_ques)>length_of_survey:
           #Update User Info with completion of survey
           participant = Users.query.get(session['pid'])
           participant.survey_one=True
           db.session.commit()

           return redirect(url_for('index', message="Survey Completed!"))
        else:
           return redirect(url_for('survey',question_num=next_ques))
    

    return render_template('question.html', image=image)