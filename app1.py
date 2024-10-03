import cv2
import streamlit as st
import numpy as np
import pyttsx3  # Text-to-speech engine
from ultralytics import YOLO
import time  # For controlling frame processing frequency

def app():
    st.set_page_config(page_title="Sign Language Translator", page_icon=":camera:", layout="wide")

    st.markdown("""
    <style>
    body {
        background-color: #33FFD1;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #00698f;'>Sign Language Detection (Real-time with Speech Output)</h1>", unsafe_allow_html=True)

    model = YOLO('best.pt')

    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Function to convert text to speech
    def speak_text(text):
        engine.say(text)
        engine.runAndWait()

    # Placeholder for video feed
    video_frame = st.empty()

    # Button to start and stop video capture
    start_button = st.button("Start Video")
    stop_button = st.button("Stop Video")

    # If "Start Video" is clicked, initiate video capture
    if start_button:
        cap = cv2.VideoCapture(0)

        # Set the video capture resolution
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # Frame processing settings
        frame_skip = 3  # Process every 3rd frame
        frame_counter = 0

        # Continue capturing video until "Stop Video" is clicked
        while not stop_button:
            ret, frame = cap.read()

            if not ret:
                st.error("Failed to capture video")
                break

            # Increment frame counter
            frame_counter += 1

            # Process every 'frame_skip' frames
            if frame_counter % frame_skip == 0:
                # Resize frame for faster processing
                frame_resized = cv2.resize(frame, (320, 240))  # Resize to a smaller dimension

                # Process the resized frame with YOLO model
                result = model(frame_resized)

                detected_signs = []

                # Annotate the frame with detections
                for detection in result[0].boxes.data:
                    x0, y0 = (int(detection[0] * (640 / 320)), int(detection[1] * (480 / 240)))  # Scale back to original size
                    x1, y1 = (int(detection[2] * (640 / 320)), int(detection[3] * (480 / 240)))  # Scale back to original size
                    score = round(float(detection[4]), 2)
                    cls = int(detection[5])
                    object_name = model.names[cls]
                    label = f'{object_name} {score}'
                    detected_signs.append(object_name)  # Add detected sign to list
                    cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 0, 0), 2)
                    cv2.putText(frame, label, (x0, y0 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), 3)

                # Convert the frame from BGR to RGB for display
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Display the frame in the Streamlit app
                video_frame.image(frame_rgb, caption="Real-time Sign Language Detection", use_column_width=True)

                # If signs are detected, speak them out loud
                if detected_signs:
                   for sign in detected_signs:
                       speak_text(f'Detected {sign}')

                # Optional: Add a short delay to further reduce CPU usage
                time.sleep(0.01)

        # Release the video capture when stopped
        cap.release()

if __name__ == "__main__":
    app()
