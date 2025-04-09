from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Folder Paths
UPLOAD_FOLDER = os.path.join("uploads", "epics")
TESTING_IMAGES_FOLDER = os.path.join(UPLOAD_FOLDER, "testing_images")

# Allowed Extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# Config Paths
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["TESTING_IMAGES_FOLDER"] = TESTING_IMAGES_FOLDER

# Create folders if not exist
for folder in [UPLOAD_FOLDER, TESTING_IMAGES_FOLDER]:
    os.makedirs(folder, exist_ok=True)

# Check for allowed file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Home Page
@app.route("/")
def index():
    return render_template("index.html")


# Scan Page → Upload to testing_images
@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400
        
        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["TESTING_IMAGES_FOLDER"], filename)
            file.save(file_path)
            return jsonify({
                "message": "File uploaded successfully to testing_images folder",
                "path": file_path
            })
        else:
            return jsonify({"error": "Invalid file format"}), 400

    return render_template("scan.html")


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Generic Upload API → Upload to uploads/epics
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)
        return jsonify({
            "message": "File uploaded successfully to uploads/epics folder",
            "path": file_path
        })
    else:
        return jsonify({"error": "Invalid file format"}), 400


if __name__ == "__main__":
    app.run(debug=True)
