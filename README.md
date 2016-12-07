# Django CRM

## Dependencies:

To start this project, first create virtualenv using python3. You need to have venv module installed. Example command:

```
python3 -m venv env
```

To activate your local environment use this command (Windows):

```
env\Scripts\activate.bat
```

Now you can install all the requiremenets for the project. This should work:

```
python3 -m pip install -r requirements.txt
```

## Running the website:

To run the website do as follows:

1) Activate your local environment (if it is not activated already):

```
env\Scripts\activate.bat
```

2) Apply migrations:

```
python3 manage.py migrate
```

3) Run the server:

```
python3 manage.py runserver
```

By default, your website should be hosted at: http://127.0.0.1:8000/.


## Additional tools:

If you want to exit local environment, then just put:

```
deactivate
```
