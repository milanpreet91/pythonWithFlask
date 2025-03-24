from flask import Flask, render_template

app = Flask(__name__) # name references app.py file
#app is object of class Flask
#__name__ : refers to how the script is invoked. 
# If invoked from app.py it refers to __main__
#print(__name__): prints __main__

#Tell flask when a certain URL is requested, 
# what shuld be returned.
#Thats why we register a route
#<domain_name>/<route>: jovian.com/profile
#Use decorator for registering
#when url / accessed, print "hello_world"
@app.route('/') #pass url route for home
def home_page():
    return render_template('home_page.html')

#if running app.py as a script, 
# then start the app using below command
if __name__ == "__main__":
    app.run(debug=True)