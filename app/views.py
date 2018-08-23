from flask import render_template, flash, redirect, request, url_for
from app import app, db
from .forms import ParticipantForm
from .models import User, Answer

curent_user = 0 #User number who has logged in
logged_in = 0 #Set when someone is logged in 

session = {"pid":0, "username":""}
length_of_survey = 10 #Number of questions here
files_for_survey= ["../static/image_1/out_A_24_1.jpg","../static/image_1/out2.jpg",
				 "../static/image_1/out4.jpg","../static/image_1/out5.jpg",
				 "../static/image_1/out6.jpg","../static/image_1/out7.jpg",
				 "../static/image_1/out8.jpg","../static/image_1/out9.jpg",
				 "../static/image_1/out10.jpg","../static/image_1/out12.jpg"]


@app.route('/login', methods=['GET', 'POST'])
def login():
	session['pid']=0
	session['username']=""
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
	# print (session)
	return redirect('/login')


@app.route('/finished_survey/<pid>')
def finished_survey(pid):
	session['pid']=0
	session['username']=""
	return render_template("completed_survey.html",pid=pid)

# This page first collects favorite color data and gives instructions for THE SURVEY
# and then asks you to begin the survey.
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	
  #   if request.method == 'POST':
	 #    # favourite_color_chosen = request.form.get("favorite-color-chosen")
		# # Update Participant information in DB with favorite color 
		# participant = User.query.get(session["pid"])
  #       # print participant.username
  #       # participant.favorite_color = favourite_color_chosen
  #       # db.session.commit()
  #       redirect(url_for(survey, question_num="1"))
	message = "Hello"
	if session["pid"] and session["username"]:
		return render_template('index.html', message=message, title="Survey Home", 
							   username=session['username'], pid=session['pid'])
	else:
		return redirect('login') 



@app.route('/survey/<question_num>', methods=['GET', 'POST'])
def survey(question_num):
	if session['pid']==0 or session['username']=="":
		return redirect(url_for('login'))

	image = files_for_survey[int(question_num)-1] 

	next_ques=str(int(question_num)+1)
	
	if request.method == "POST":
		hue = request.form.get('hue')
		sat = request.form.get('sat')
		light = request.form.get('light')
		dominant_color_chosen = "hue:"+hue+",sat:"+sat+",light:"+light
		#Answers(userid, surveynum(1,2,3), questionnum(1-10), answerstring)
		ans = Answer(session['pid'], int(question_num), image+","+dominant_color_chosen)
		db.session.add(ans)
		db.session.commit()


		if int(next_ques)>length_of_survey:
		   #Update User Info with completion of survey
		   # participant = User.query.get(session['pid'])
		   # db.session.commit()
		   return redirect(url_for('finished_survey', pid=session['pid']))
		else:
		   return redirect(url_for('survey',question_num=next_ques))
	

	return render_template('question.html', image=image)
