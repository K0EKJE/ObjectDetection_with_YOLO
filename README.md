# ObjectDetection_with_YOLOV2

## Example ouput

<img src="Example Detected Objects/westwood1.jpeg" style="width:400px;height:300px;">  <img src="Example Detected Objects/pedestrian.jpeg" style="width:450px;height:300px;" title = "Figure">   
Figure 1 & 2

<img src="Example Detected Objects/example_IDLE_group.jpg" style="width:450px;height:300px;">  <img src="Example Detected Objects/person.jpg" style="width:400px;height:300px;">  
Figure 3(with customized filter function) & 4

## Purpose 

In order to better understand the implementation and application of YOLO algorithm, I implemented some of the key functions of the YOLO algorithm, made my customized improvement on the `yolo_filter_boxes` function, and finally applied the algorithm to two short videos in this project. 

## Process

First, I directly clone the project from https://github.com/allanzelener/yad2k.git in order to get access to some of the helper functions, and I used the pretrained model from the official YOLO website https://pjreddie.com/darknet/yolo/. The pretrained model supports object detection for over 80 classes of objects. Then I implemented the following functions in sequence.

    yolo_filter_boxes : Filters YOLO boxes by thresholding on object scores.
    improved_yolo_filter_boxes : Filters YOLO boxes by thresholding on object scores and class confidence.
    iou & box_iou : Calculate and visualizes iou area.
    NonMax_suppression : Applies Non-max suppression (NMS) to set of boxes.
    yolo_eval : Converts the output of YOLO encoding to predicted boxes.
    predict : Predict and draw boxes on input image.
    video_with_prediction : Helper function to predict and draw bounding boxes from input image folder, then outputs to output folder
    to_video : Create video in folder video/Output Videos/default or video/Output Videos/improved/ according to mode input value

## Result

The main modification I did in the `improved_yolo_filter_boxes` function is that I add an additional threshold on class confidence. According to the design of this algorithm, the ouput of neural network will contain a class confidence value for each anchor(five in total) in each grid(19 * 19 in total). It predicts the probability of having an object in that anchor. Originally, the algotithm filters the boxes by the scores obtained from multiplying box confidence and class probability. I added an additional criteria to ensure that the probablity of having an object in that anchor exceeds 0.4(by default; can be tuned). 
In some cases, it is effective in filtering out overlapping boxes that predict the same class. Examples can be seen as follow(pictures produced by improved function is on the right, and default is on the left): 

Old & New

<img src="Example Detected Objects/example_IDLE_group_default.jpg" style="width:450px;height:300px;"> <img src="Example Detected Objects/example_IDLE_group.jpg" style="width:450px;height:300px;"> 

<img src="video/Output Images/horses/000143.jpg" style="width:450px;height:300px;">	 <img src="video/Output Images Improved/horses/000143.jpg" style="width:450px;height:300px;">	

These are some of the positive examples. However, the low class confidence can also result from distance and inadaquate information. For example, in the case where there are a lot of cars, the improved version fails to detect cars that are largely concealed. Examples can be seen as follow(one random frame in the video westwood1): 

<img src="video/Output Images/westwood1/000290.jpg" style="width:450px;height:300px;"> <img src="video/Output Images Improved/westwood1/000290.jpg" style="width:450px;height:300px;">

## Reflection 

There are multiple ways to control the threshold. By design, the algorithm can adjust it by changing the threshold on scores. It may have advantage on some cases; but in this project I chose an another implementation because I beleive the problem of overlapping boxes that predict on same classes can be better addressed by a condition on class confidence. To further improve the accuracy on specific classes, I can overfit the pretrained model on those classes. 

