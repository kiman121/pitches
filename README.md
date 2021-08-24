# PitchMaster Web Application
#### A pitch application.

#### By **Patrick Mwangangi**
## Description
A pitch can make or break someone's life. PitchMaster a carefully crafted application that serve as a platform where interested users are able to view other users' pitches as well as post their unique master piece pitches.

Further to the above usage, this master piece was created as practice on concepts learnt in Python Flask (at Moringa School).
## Demo
Here is a working live demo : https://zetufeed.herokuapp.com/
## Setup/Installaction Requirements
- Clone the repository (repo).
    ```
    git clone https://github.com/kiman121/pitches.git
    ```
- Open the project on VS Code or any editor of choice.
- Navigate to the projects root directory.
- Open the virtual environment by running the `source virtual/bin/activate` command.
- Install the required packages: `pip install -r requirements.txt`
- Create a start.sh file and add the following data instances
    ```
    MAIL_USERNAME = <'email_username'>
    MAIL_PASSWORD = <'email_password>
    ```
- Run migrations to update the changes to db: `python3 manage.py db migrate -m <"your comment">` then `python3 manage.py db upgrade`
- Configure a start.sh file to execute your app
- Execute you start.sh file from terminal to lauch app
- open this url on your browser "http://127.0.0.1:5000/"
## Known Bugs

No Known bugs

## Technology Used
- HTML
- CSS
- Javascript
- Bootstrap
- Python
- Flask

## Support and contact details

If you want to contact us, email us on info@pitches.com

### License

[MIT licence](https://github.com/kiman121/pitches/blob/master/LICENCE)
Copyright (c) 2021 **PitchMaster**