# Willow Study Helper
<img src="https://github.com/shrishayap/willowStudyHelper/blob/main/logo.png" align="right" alt="Willow Study Helper Logo" width="235" height="200">
Willow is a study helper web application inspired from the Pomodoro technique to help user stay focused and accountable by connecting you to your friends during a collaborative study session. The purpose of the app is to combat procrastination and micro-distractions that are more than prevalent in the digital age. 

<hr>

<h2>What it does</h2>
The app works in two parts: 
<ol>  
  <li><b>Gamification Functionality:</b> The web extension that helps the user log in and record their session to track their progress. Once the user has logged in, they get to select their ‘mission’. A ‘mission’ is the gamification of the Pomodoro technique, where a player selects a certain amount of time to study and gets the reward in XP and Credits. These are to be collected for later purchase.</li>
  <br>
  <p align="center">
  <img src="https://github.com/shrishayap/willowStudyHelper/blob/main/gamification.png" alt="Gamification" width=75% height=auto>
  </p>
  
  <li><b>Distraction Detection Functionality:</b> During a ‘mission’, the web extension tracks what the user is using their web browser for. If it detects that it is for unproductive purposes, then it blocks the user from entering the website, reminding them that they should be studying. It also sends out a message to everyone else on the server so they can hold their friend accountable.
  <br>
  <p align="center">
  <img src="https://github.com/shrishayap/willowStudyHelper/blob/main/distraction.png" alt="Distraction Detection" width=75% height=auto>
  </p>
</ol>

<hr>

<h2>What it's made of</h2>
We built Willow using various web frameworks since it had a web extension and web server. The web extension was built primarily with JavaScript and carried out frequent listeners to track user activity. It also did background requests to update the server. The web server was built in Python using Flask. The live updates to the website were done using Ajax, and the user stats and login info were stored on a SQL database.
<br>
<p align="left">
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/javascript-colored.svg" width="36" height="36" alt="JavaScript" /></a>
<a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/html5-colored.svg" width="36" height="36" alt="HTML5" /></a>
  <a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/css3-colored.svg" width="36" height="36" alt="CSS3" /></a>
<a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/flask-colored-dark.svg" width="36" height="36" alt="Flask" /></a>
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/mysql-colored.svg" width="36" height="36" alt="MySQL" /></a>
</p>


<hr>
<b>Submitted to HooHacks 2022</b> | <a href="https://devpost.com/software/willow-study-app">Devpost Link</a>
