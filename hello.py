from flask import Flask

app = Flask(__name__)

print(app)
@app.route("/")
def hello_world():
    return "Hello, World!"

print(__name__)
"""
   The if __name__ == "__main__": construct in Python is used to determine whether the current script is 
   being run as the main program or if it is being imported as a module into another script

                                        AND 
                                        
    __name__ is a variable that exists in every Python module, and is set to the name of the module.
    __main__ is the name of the Python environment where top-level code is run (with top-level code being
"""
if __name__ == "__main__":
    app.run()