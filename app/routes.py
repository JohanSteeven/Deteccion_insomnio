from flask import Blueprint, request, jsonify, render_template
import cv2
import numpy as np
import dlib
from imutils import face_utils
from .utils import compute, blinked

api = Blueprint('api', __name__)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

@api.route('/')
def home():
    return render_template('index.html')

@api.route('/detect', methods=['POST'])
def detect():
    try:
        image_data = request.files.get('image')
        if not image_data:
            return jsonify({"error": "No se proporcionó ninguna imagen"}), 400

        file_bytes = np.frombuffer(image_data.read(), np.uint8)
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        status = "No face detected"
        for face in faces:
            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            left_blink = blinked(landmarks[36], landmarks[37], landmarks[38],
                                 landmarks[41], landmarks[40], landmarks[39])
            right_blink = blinked(landmarks[42], landmarks[43], landmarks[44],
                                  landmarks[47], landmarks[46], landmarks[45])

            if left_blink == 0 or right_blink == 0:
                status = "DORMIDO !!!"
            elif left_blink == 1 or right_blink == 1:
                status = "Somnoliento !"
            else:
                status = "Despierto :)"

        return jsonify({"status": status}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
