---
title: DUMY
description: autonomous robot arm to play laser tag fetch with my cat
date: 10/13/2023
---

*I am a big believer in the ideology that defining a problem results in the solution building itself. So if you have an attention-seeking feline while you're in class, it makes only sense to build her an autonomous robot arm that can play laser tag fetch with her.* 

<br>
## system design

I have a 3 D.O.F. robot arm that I 3D printed during a summer. The extensible claw allows me to grip anything, in this case a laser pointer. The initial idea was to connect a webcam to a RP 2040 and send RPCs to my server. I would have a model running on my server that could identify a bounding box over the kitty, and determine where to move the laser pointer so she can't catch it.

<!-- <img src="../assets/dumy/5.jpg" width="200"> -->
<div class="grid grid-cols-2 my-6 gap-4">
  <div class="bg-gray-200 rounded-lg p-3">
      <img class="w-full h-auto" src="../assets/dumy/5.jpg"></img>
      <p class="text-center text-sm mt-2">left</p>
  </div>
  <div class="bg-gray-200 rounded-lg p-3">
      <img class="w-full h-auto" src="../assets/dumy/5.jpg"></img>
      <p class="text-center text-sm mt-2">left</p>
  </div>
</div>

However, I was fortunate enough to obtain a Nvidia Jetson Nano not too long ago. The Jetson is supposed to be robotics base, which means that I can run compute on edge. With GPIO pins, I could also completely ditch the need for running a daughterboard with the RP 2040. Based on some initial benchmarks, I was getting comparable TFLOPs to a 3070 which is sufficient for running a very basic off-the-shelf object detection model.
