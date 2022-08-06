# willowStudyHelper
A 4 inspired study helper that keeps you accountable and on task
Inspiration
Being students in the digital age, there are a lot of distractions in our lives, especially since the devices we use to do work are also the devices we use for entertainment. We are more at risk of procrastination now more than ever. We all knew that accountability was the best way to help combat this, but holding yourself accountable is extremely difficult. Living in a time where being socially distant is still the best thing to do, having someone else hold you accountable is getting increasingly difficult.

We decided to solve this problem by creating a web app that connects you to friends so they can hold you accountable, and also integrate famous study techniques like the Pomodoro Timer.

What it does
The app works in two parts. The first is the web extension that helps the user log in and record their session. This is important in the gamification aspect because they need to keep track of their progress. Once the user has logged in, they get to select their ‘mission’. A ‘mission’ is the gamification of the Pomodoro technique, where a player selects a certain amount of time to study and gets the reward in XP and Credits. These are to be collected for later purchase.

During a ‘mission’, the web extension tracks what the user is using their web browser for. If it detects that it is for unproductive purposes, then it blocks the user from entering the website, reminding them that they should be studying. It also sends out a message to everyone else on the server so they can hold their friend accountable.

How we built it
We built Willow using various web frameworks since it had a web extension and web server. The web extension was built primarily with JavaScript and carried out frequent listeners to track user activity. It also did background requests to update the server. The web server was built in Python using Flask. The live updates to the website were done using Ajax, and the user stats and login info were stored on a SQL database.

Challenges we ran into
Initially, we spent a lot of time trying to find specific datasets for a project we had in mind, but we couldn’t find any relevant, comprehensive data, so we pivoted to a WebApp. We faced multiple issues with cross-compatibility between various languages, so we spent a lot of time trying to reduce the friction. We had very little knowledge about front-end development, so creating a full-stack app was a massive hurdle. We also had some issues with finding a balance between the education and gaming aspects of our project.

Accomplishments that we're proud of
We figured out the networking and live-update aspect of the project without knowing any javascript upon entering the competition. Knowing so little about javascript, being able to create a full-stack app that so heavily relied on javascript and making it reliable was a major accomplishment. We are also proud of completing our first hackathon!

What we learned
We learned several web development frameworks such as Flask and Ajax and system design. We also learned essential software development skills such as version control and feature implementation. We further developed our problem-solving skills and honed our mindset/persistence throughout the entire hackathon.

What's next for Willow Study App
Some improvements we would make to Willow is to improve the game aspect by changing various features such as adding player stats such as health, damage, etc. that can be upgraded and utilized during “raids” that are essentially co-op Pomodoro sessions. Adding a variety of currencies would also add a level of depth of the missions, which only further incentives users to study.
