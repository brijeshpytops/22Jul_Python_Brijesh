1] Git/Github

- create your account
- create a new repository - copy the repo URL
- install the git client on your computer
- open the terminal[open CMD on specific location]
- >>> git clone [repo URL]
- >>> cd [repo name]
- >>> code .

2]  Download Visual Studio Code
- Open the downloaded file and follow the installation instructions.
- Once installed, open Visual Studio Code.
- You can now start coding and creating projects in Visual Studio Code.


git commands:
- git add .
- git commit -m "message"
- git push -u origin master
- git pull origin master
- git branch -a
- git checkout -b [branch name]
- git merge [branch name]
- git remote add origin [repo URL]
- git remote -v


3] project commands for pip

- Check installed modules and packages
>>> pip list/pip freeze

- modules and packages install/uninstall command
>>> pip install [module-and-pakcage-name]==3.x.x
>>> pip uninstall [module-and-pakcage-name]==3.x.x

- create virtual env.
>>> python -m venv [your-virtual-env-name]

- activate and deactivate your virtual env.
>>> [your-virtual-env-name]\Scripts\activate
([your-virtual-env-name])...>>> [your-virtual-env-name]\Scripts\deactivate

- installed modules and packages add in requirements.txt file
>>> pip freeze > requirements.txt
- install/update modules and packgaes from requirements.txt
>>> pip install -r requirements.txt