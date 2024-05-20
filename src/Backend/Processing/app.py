from flask import Flask, request, jsonify
import numpy as np
import cv2

app = Flask(__name__)

def apply_filter(frame, filter_name):
    if filter_name == "Original":
        return frame
    elif filter_name == "Black&White":
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
    elif filter_name == "Negative":
        return cv2.bitwise_not(frame)
    elif filter_name == "Rotate 90°":
        return cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif filter_name == "Rotate 180°":
        return cv2.rotate(frame, cv2.ROTATE_180)
    elif filter_name == "Rotate 270°":
        return cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif filter_name == "Canny":
        edges = cv2.Canny(frame, 100, 200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Check if the POST request contains a file named 'image'
        if 'image' not in request.files:
            return jsonify({'error': 'No image found in the request'}), 400
        
        # Read the image file from the request
        image_file = request.files['image']
        
        # Convert the image file to a NumPy array
        nparr = np.frombuffer(image_file.read(), np.uint8)
        
        # Decode the image array to OpenCV format
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Get the filter name from the request
        filter_name = request.form.get('filter')
        
        # Apply filter to the image
        processed_image = apply_filter(frame, filter_name)
        
        if processed_image is None:
            return jsonify({'error': 'Invalid filter name'}), 400
        
        # Encode the processed image to JPEG format
        success, encoded_image = cv2.imencode('.jpg', processed_image)
        
        if not success:
            return jsonify({'error': 'Failed to encode image'}), 500
        
        # Return the processed image as bytes
        return encoded_image.tobytes(), 200, {'Content-Type': 'image/jpeg'}
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500