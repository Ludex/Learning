from flask import Flask, render_template
import connexion

# Create the application instance
# app = Flask(__name__, template_folder="templates")
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

@app.route('/')
def home():
    '''
    This function just responds to the browser URL localhost:5000/
    
    '''
    return render_template("home.html")


# Run the application if we're running in stand-alone mode
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)