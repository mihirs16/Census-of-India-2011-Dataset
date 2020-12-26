# imports
import data
import os, dotenv
import flask, flask_cors

# server setup
app = flask.Flask(__name__)
flask_cors.CORS(app, support_credentials = True)

# database setup
dotenv.load_dotenv()
username = os.getenv("GCP_SQL_USER")
password = os.getenv("GCP_SQL_PASS")
hostname = os.getenv("GCP_SQL_HOST")
db = data.Database("may_db", username, password, hostname)

# default route | returns homepage
@app.route("/", methods = ["GET"])
def home():
    return flask.render_template("index.html")

# database route | returns filtered table
@app.route("/database", methods = ["POST"])
def get_data():
    received = flask.request.json
    return db.fetch(
        table_name = received.get("table_name"), 
        filter_column = received.get("column_filter"),
        filter_values = received.get("filter_values")
    ).to_json()

# app run
if __name__ == '__main__':
    # for hot reload and tracking static files and templates
    from os import path, walk

    extra_dirs = ['templates/', 'static/']
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)

    # flask app run
    app.run(debug=True, extra_files=extra_files)
