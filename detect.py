import cv2
from pycoral.utils.edgetpu import make_interpreter, run_inference
from pycoral.adapters.common import input_size
from pycoral.adapters.detect import get_objects

interpreter = make_interpreter('vision/tflite_model/yolov5n_edgetpu.tflite')
interpreter.allocate_tensors()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    image = cv2.resize(frame, input_size(interpreter))
    run_inference(interpreter, image.tobytes())
    objs = get_objects(interpreter, score_threshold=0.4)

    for obj in objs:
        bbox = obj.bbox
        cv2.rectangle(frame, (bbox.xmin, bbox.ymin), (bbox.xmax, bbox.ymax), (0, 255, 0), 2)

    cv2.imshow('YOLOv5n Coral Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
