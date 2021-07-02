Steps to run the application:


1. Download python
2. Go to the application main directory
3. Open cmd/terminal in that directory
4. Create virtual environment (command: virtualenv <virtual environment name>)
        If virtualenv is not installed install virtualenv (command: pip install virtualenv)

5. After virtual environment is created, activate virtual environment
    (Command:
        For windows: .\<virtual environment name>\Scripts\activate
        For linux: source <virtual environment name>/bin/activate
    )

6. After virtual environment is activated go to directory sb_assignment
        (Command: cd sb_assignment)

7. Install all the requirements
        (pip install -r requirements.txt)

8. On the directory sb_assignment run the program
        (Command: python manage.py runserver)
9. After program is up and running go to web browser
10. Enter the address: http://127.0.0.1:8000/
11. Use the Application
