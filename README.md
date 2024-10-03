# sign_language_detection_yolov8
Link to the web app: https://sign-new-ushjjtf8amvnjfvqsj7phc.streamlit.app/


Precision: metrics/precision(B) = 0.8918
Precision measures the ratio of true positives (correctly detected objects) to the sum of true positives and false positives (incorrectly detected objects).

Recall: metrics/recall(B) = 0.9
Recall measures the ratio of true positives to the sum of true positives and false negatives (missed objects).


mAP (mean Average Precision):


- metrics/mAP50(B) = 0.9599: Average precision at an IoU (Intersection over Union) threshold of 0.5. This measures the model's ability to detect objects with moderate accuracy.
- metrics/mAP50-95(B) = 0.7968: Average precision across IoU thresholds from 0.5 to 0.95 (in increments of 0.05). This measures the model's ability to detect objects with high accuracy.


Fitness: fitness = 0.8131
Fitness is a composite metric that balances precision, recall, and mAP. Higher fitness values indicate better overall performance.


Interpretation:


- The model has high precision (89.18%) and recall (90%), indicating good detection accuracy.
- The model excels at moderate accuracy (mAP50 = 95.99%) but struggles slightly at higher accuracy thresholds (mAP50-95 = 79.68%).
- The overall fitness score (81.31%) suggests a well-balanced performance.
