# ObjectDetection_with_YOLO
Some example ouput

<img src="Example Detected Objects/westwood1.jpeg" style="width:400px;height:300px;">  <img src="Example Detected Objects/pedestrian.jpeg" style="width:450px;height:300px;" title = "Figure">   
Figure 1 & 2

<img src="Example Detected Objects/example_IDLE_group.jpg" style="width:450px;height:300px;">  <img src="Example Detected Objects/person.jpg" style="width:400px;height:300px;">  
Figure 3(with customized filter function) & 4

In order to better understand the implementation and application of YOLO algorithm, I implemented some of the key functions of the YOLO algorithm, made my customized improvement on the `yolo_filter_boxes` function, and finally applied the algorithm to two short videos in this project. 

First, I directly clone the project from https://github.com/allanzelener/yad2k.git in order to get access to some of the helper functions, and I used the pretrained model from the official YOLO website https://pjreddie.com/darknet/yolo/. The pretrained model supports object detection for over 80 classes of objects. Then I implemented the following functions in sequence.

    yolo_filter_boxes : Filters YOLO boxes by thresholding on object scores.
    improved_yolo_filter_boxes : Filters YOLO boxes by thresholding on object scores and class confidence.
    iou & box_iou : Calculate and visualizes iou area.
    NonMax_suppression : Applies Non-max suppression (NMS) to set of boxes.
    yolo_eval : Converts the output of YOLO encoding to predicted boxes.
    predict : Predict and draw boxes on input image.
    video_with_prediction : Helper function to predict and draw bounding boxes from input image folder, then outputs to output folder
    to_video : Create video in folder video/Output Videos/default or video/Output Videos/improved/ according to mode input value




<img src="Example Detected Objects/example_IDLE_group_default.jpg" style="width:450px;height:300px;">






