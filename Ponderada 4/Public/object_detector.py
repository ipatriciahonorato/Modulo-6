# Import libraries
from ultralytics import YOLO
from flask import request, Response, Flask
from flask import render_template
from waitress import serve
from PIL import Image
import json
import sqlite3
import io

app = Flask(__name__, template_folder='template')

@app.route("/")
def root():
    return render_template("index.html")

# Detection route which accepts POST requests
@app.route("/detect", methods=["POST"])
def detect():
    """
    Handler for /detect POST endpoint.
    Takes the uploaded file "image_file", 
    passes it through YOLOv8 object detection model
    and returns an array of bounding boxes.
    """
    buf = request.files["image_file"]
    boxes = detect_objects_on_image(Image.open(buf.stream), buf.filename)
    return Response(
      json.dumps(boxes),  
      mimetype='application/json'
    )

# Function to apply YOLOv8 model on an image and return detected objects
def detect_objects_on_image(buf, filename):
    """
    Takes an image, passes it through YOLOv8 neural network
    and returns an array of detected objects.
    """
    model = YOLO("C:/Users/Inteli/OneDrive/Documents/GitHub/Modulo-6/ponderada 4/Public/YoloModel/best.pt")
    results = model.predict(buf)
    result = results[0]
    output = []

    # Save the detection to a file and read it into a byte array
    if '.' not in filename:
        filename += '.png' 
        buf.save(filename)
    with open(filename, "rb") as f:
        image_byte_arr = f.read()

    # Iterate over each box (detected object) and save the result to a database
    for box in result.boxes:
        x1, y1, x2, y2 = [
          round(x) for x in box.xyxy[0].tolist()
        ]
        class_id = box.cls[0].item()
        prob = round(box.conf[0].item(), 2)
        output.append([
          x1, y1, x2, y2, result.names[class_id], prob
        ])

        conn = sqlite3.connect('detections.db')  # Connect to database
        cursor = conn.cursor()  # Create a cursor

        # Insert the detection result into the table
        cursor.execute('''
            INSERT INTO detections (x1, y1, x2, y2, object_type, probability, image)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (x1, y1, x2, y2, result.names[class_id], prob, image_byte_arr))

        conn.commit()  # Commit the transaction
        conn.close()  # Close the connection

    return output

serve(app, host='0.0.0.0', port=8080)



