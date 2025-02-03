# Reaction Speed Test

## Contents

## Bugs

### Reaction time is artificially incremented

Suspectedly due to the DOM manipulations the time that is recorded is ~100~200ms higher than what it actually is.

## Future Features

### Update Game JavaScript

In an attempt to fix the time recorded being slower than what it is in reality, I plan to adjust the game to add additional time checks before and after DOM manipulations, as well as including the event listener within the same function itself rather than in one of the functions that it goes through - to try and reduce the amount of code that is run through before the time of the user click is created.

### Profile Pages

In future I would like to create a profile page for each user, showing the number of tests they have completed, their best result, worst result as well as an average.

## Deployment

1) Add the required files to the git repository with the command `git add .`

2) Commit the changes to the repository with the command commit command `git commit -m "Final project commit"`

3) [Create new app on Heroku](https://dashboard.heroku.com/new-app)

![Creating Heroku App](docs/readme/deploy-createApp.png)

4) Connect to GitHub repo

![Github Repository Linking](docs/readme/deploy-connectGithub.png)

5) Set Config vars to replicate what is in env.py - heroku-config-vars.png
link to github

![Heroku Config Vars](docs/readme/deploy-configVars.png)

6) Manual deploy on heroku - heroku-deploy.png

![Heroku Deployment](docs/readme/deploy-deploy.png)

7) Wait for deployment to finish

![Heroku Deployment Check](docs/readme/deploy-deploying.png)

8) Check project deployed as expected

![Heroku Deployment Check](docs/readme/deploy-success.png)

###### [*Back to contents*](#contents)


## Testing

### AI Testing



![alt text](docs/readme/CoPilot-Tests.png)

![alt text](docs/readme/AutomatedTests.png)

## Credits

### Code Institute

#### Codestar blog CSS

[Using the codestar blog css as a template to go off](static/css/codestar.css)

#### Queuing up & Displaying messages

## Video Game Tracker Project

### CSS

[Borrowing the CSS from my Video Game Tracker Project for styling](static/css/style.css)