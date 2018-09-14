# Red Aerodrome Detection For Drones

This repository for red circle shape aerodrome detection for Drones. We supplied a demo script which can show result on given videos. We also supplied two different cases. You can easily test the project using these videos. In following figure, You can see 3 different detection results. 

<p align="center">
  <img src="Output/1.jpg" width="280"/>  
  <img src="Output/370.jpg" width="280"/>  
  <img src="Output/570.jpg" width="280"/> 
</p>

Projects uses Opencv and skimage libraries to find red circle and determine its position and also radius as well. To find circle model we used ransac algorithm. You can run demo with one of our video, please using following command.
```
$ python demo.py Input/video2.mp4
```
