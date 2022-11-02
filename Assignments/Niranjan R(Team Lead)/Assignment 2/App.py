from flask import Flask, url_for, render_template, request, redirect from markupsafe import escape
app = Flask( name ) app.config['SECRET_KEY']="KIIU54RYBMKLO8321S"  all_posts= [  
{  
'title':"Blog post 1",  
'content': "This is first Post",  
'author':'DEV'  
},  
{  
'title':"Blog post 2",  
'content':"This is second Post"  
}  
]  
  
  
@app.route("/")  
def index():  
return '<h1>Welcome to home Page</h1>'  
  
  
@app.route("/login") def 
login():  
return 'login'  
  
  
@app.route('/blog')  def blog():  
return render_template('blog.html', posts=all_posts)  
  
  
#dynamic routing  
@app.route("/users/<username>") 
def profile(username):  
return render_template('profile.html', username=username)  
  
  
@app.route("/signin")  
def signin():  
return render_template('signin.html')  
  
  
@app.route("/signup") def 
signup():  
return render_template('signup.html')  
@app.route("/home") def homepage():  
return render_template('home.html')  
  
  
@app.route("/about") def 
about():  
return render_template('about.html')  
  
  
messages = [{'title': 'Message One',  
'content': 'IAM DEEPA'},  
{'title': 'Message Two',  
'content': 'FLASK APP DEMO'}  
  
]  
@app.route("/chat")  def chat():  
return render_template("chat.html", messages=messages) SIGNUP.HTML  
  
  
{% extends “base.html” %}  
{% block title %}Signuppage{% endblock %}  
{% block body %}  
<body>  
<!—Main div code  
<div id=”main”>  
<div class=”h-tag”>  
<h2>Create Your Account</h2>  
</div>  
<!—create account div  
<div class=”login”>  
<table cellspacing=”2” align=”center” cellpadding=”8” border=”0”>  
<tr>  
<td align=”right”>Enter Name :</td>  
<td><input type=”text” placeholder=”Enter user here” class=”tb” /></td>  
</tr>  
<tr>  
<td align=”right”>Enter Email ID :</td>  
<td><input type=”text” placeholder=”Enter Email ID here” class=”tb” /></td>  
</tr>  
<tr>  
<td align=”right”>Enter Username :</td>  
<td><input type=”text” placeholder=”Enter Username here” class=”tb” /></td>  
</tr>  
<tr>  
<td align=”right”>Enter Password :</td>  
<td><input type=”password” placeholder=”Enter Password here” class=”tb” /></td>  
</tr>  
<tr>  
<td align=”right”>Enter Confirm Password :</td>  
<td><input type=”password” placeholder=”Enter Password here” class=”tb” /></td>  
</tr>  
<tr>  
<td></td>  
<td>  
<input type=”reset” value=”Clear Form” id=”res” class=”btn” />  
<input type=”submit” value=”Create Account” class=”btn” /></td>  
</tr>  
</table>  
</div>  
<!—create account box ending here..  
</div>  
<!—Main div ending here…  
</body>  
{% endblock %}  
