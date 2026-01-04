'''

Flask in Client-Server Model:
    Flask is server-side: handles requests, runs backend logic, talks to databases.
    Browser (or frontend app) is client-side: renders HTML/CSS/JS, executes JS, shows UI.


        
Folder Structure:
    templates/ → HTML files, rendered by Flask.
    static/ → JS, CSS, images, downloadable files.
    Backend Python code → handles authentication, database queries, APIs (for diff services.). (its Never exposed to user.).

    

Frontend-Backend Communication:
    Frontend can be:
        Server-rendered HTML (Flask templates)
        Separate frameworks (ReactJS, VueJS)

    Backend exposes APIs (HTTP endpoints) to send/receive data.  [api endpoints are accessible to client code but the implementation details remain hidden (diff api for diff service, i.e what the purpose is for frontend and backend right, frontend gives users the features and then when asked, via api endpoints backend serves those features)]

    Example: 
        Frontend request                                                                Backend response
       User clicks “Get Profile” → JS fetches /api/profile             Flask checks DB → returns JSON with user info
       User submits form → JS POSTs /api/register                      Flask validates → adds user to DB → returns success/failure

       

Full-stack App = Frontend + Flask Backend + Database
    Frontend: HTML/CSS/JS or React for UI
    Backend: Flask for server-side logic
    Database: SQL/NoSQL for persistent storage

    

Key intuition:
    Server-side code: hidden, processes logic and data.
    Client-side code: visible, executes in browser, communicates via APIs.

'''

# Now lets create a flask server

from flask import Flask, render_template, redirect, flash, request, jsonify

app = Flask(__name__,
            static_folder='assets',
            static_url_path='/files/')

app.secret_key = 'secret_key'

@app.route('/', methods=["GET","POST"])
def hello_one():
    name = "ADITYA SINGH"
    lst = [11,22,33,44,55,66,77]
    yolo = "<b> HELLO WORLD! </b>"
    flash("welcome to homepage.")
    return redirect('/about') # this will take us to the about route and load hello_two function.
    return render_template("home.html", nm=name, lst=lst, html_txt=yolo )  # goes straight to template folder to look for this "index.html" file.

@app.route('/about', methods=["GET","POST"])
def hello_two():
    flash("Welcome to about page")
    name = request.args.get("nm", default="noname")
    lang = request.args.get("lng",default="nolang")
    # some machine learning or sql process here that generates a data.
    return render_template("about.html", name_var=name,lang_var=lang)


@app.route('/api', methods=["GET","POST"])
def api_data():
    # some ml or sql backend process here that generates the data, for now we'll use synthetic data.
    data = {"Output": 55, "Accuracy": 95.58}
    return jsonify(data), 200

''' 
See, flask only show/execute those function's output (return) that are mapped with a specific route. 
In case 1 you can see that only hello_one() gets executed, hello_two() does not get executed (not even on the terminal/console).
    case 1 code: (for you to test)
        @app.route('/')

        def hello_one():=
            return "<p> BYE ADITYA! </p>"

        def hello_two():
            return "<p> BYE ADITYA! </p>"


In case 2 you can see that still only hello_one() gets executed, hello_two() is still not shown on the browser as its still got nothing to do with the routed function's output (return line). But it does get executed in the terminal this time since its been called. (but not in the browser's console).
    case 2 code:    (for you to test)
        @app.route('/')

        def hello_one():
            hello_two()
            return "<p> BYE ADITYA! </p>"   

        def hello_two():
            #return "<p> BYE ADITYA! </p>"   # this will not be shown anywhere as it'll be ignored for the browser..and it wont be printed in the terminal either.
            print("hello") # prints hello in your terminal (not in browser's console.).

In case 3 you can see that both the function have been executed/shown on the browser page, as this time the function "hello_two" was called in the return line, i.e this time its execution was used or was necessary in order for the mapped function's execution line (return line) 
    case 3 code:     (for you to test)

        @app.route('/')

        def hello_one():
            return hello_two() + "<p> BYE ADITYA! </p>"

        def hello_two():
            # return "<p> BYE ADITYA! </p>"
            print("hello")   # prints hello in your terminal (not in browser's console.).
    
'''



app.run(debug=True)


'''
Let us understand how this flask server code works:

1. We import flask.
2. we create a flask app.
3. we define what will happen when we'll hit the default route, i.e '/'.
4. when the app is run via "app.run(debug=True)" .......
4. upon hitting that route, the functions inside it will be executed and we'll see output depending on what we wrote.
'''


'''

OK ONE MORE THING TO KNOW, its that:

    Flask only serves the client side script...to the browser, then the browser executes it, not the FLASK server.

'''



'''

Now we're learning how to modify the default static files containing folder [called 'static'] and how to modify the default url path shown ['static/'] on the webpage in order to get the static files.

we'll be using the url_for('static', file_name='xyz.abc') in order to access any static file irrespective of the folder its in (modified name or static) and irrespective of the path we'll need to take to access it (could be static or modified name or even other name (even though we got a modified name...i.e by overriding it.))...its considered a good practice as we're not hard coding the folder name or its access url...so even if they're changed...our code is bulletproof and versatile.


'''


'''

GET AND POST IN FLASK:

    1️⃣ GET request (default behavior)

    A GET request is used to request a resource.
    In Flask, when you define a route like:

    @app.route("/login")
    def login():
        return render_template("login.html")

    Flask implicitly assumes methods=["GET"].

    This means:
        - User types /login in the browser
        - Browser sends a GET request
        - Flask runs the mapped function
        - You usually return a template or some data

    So yes, GET is commonly used to load a page / URL.

    
    2️⃣ POST request (form submission or data sending)

        A POST request is used to send data to the server.

        In Flask, POST has two things to care about (you said this correctly):
            1. Where the data is submitted (URL)
            2. What to do with the submitted data

        <form method="POST" action="/login">
        <input name="username">
        <input name="password">
        <button type="submit">Login</button>
        </form>

        action="/login" → URL the data goes to

        method="POST" → type of request


    3️⃣ Handling GET and POST in the same route (very common)

        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "POST":
                username = request.form["username"]
                password = request.form["password"]
                # process data here
                return "Logged in"

            # GET request
            return render_template("login.html")

        What happens:
            GET /login
                Shows the form
            
            POST /login
                Submits form data
                Executes POST logic

            This is the standard Flask pattern.

'''


'''

Jinja template prevents html injection, i.e it does not accept the html code in variables and just treats it as a normal string, if we want the html to work then we use ' | safe ' .

'''


'''

Template inheritance in flask allows us to create a base template that has a certain design and then we can build custom pages of the website based off of that base template.

'''


'''

Message flashing is used to send mssg/notification/updates/alerts from the backend to the frontend.

'''


'''

Query Parameters are just taking user input values (from url) and putting them to use in backend and then showing related output in the frontend (using jinja 2 template).

'''


'''

APIs are used for data exchange btw frontend and backend as per the service i.e called for. It happens in json format.

along with passing api data we also pass certain http status codes which basically tell the browser what happened when it tried talking to the website/api


200 – Everything OK

201 – Created successfully

400 – Bad input

401 vs 403 – Not authenticated vs not allowed

404 – Not found

500 – Server messed up

503 – Server temporarily unavailable

'''