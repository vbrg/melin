# melin
Melinian shorthand synthesizer

# Introduction
The rise in popularity of computers in the 90's completely removed the need for shorthand writing, and it is today just some weird niche tool for specific and uncommon situations... At least that's what I hear. But I'd argue otherwise. Melinan shorhand is (amongst many other systems) a wonderful way of taking notes, and it beats in speed even the fastest keyboard warrior when it comes to getting the information down. A skilled shorthand writer may clock upwards of 300 syllables per minute in Swedish -- thats sports commentary speed right there. Try doing that with a qwerty keyboard.. you won't manage. Also, a gentlemen would not use a laptop to take notes during a meeting, only plebs would do that. So we still need to be able to take notes quickly using a pen and a paper, people just forgot how to. 

There are computer programs out there that should not exist.. and you might think this is an example of such. However, this is just a component of something bigger that will come later. You see, after having taken notes using shorthand, you'll need to translate the information back to 'långskrift' if you want to share what you wrote with others. A way of doing that is by just going though your manuscript and rewriting it on your computer, but thats dull. Wouldn't it be a lot nicer if you could just use an automatic translator that would translate the shorthand writing back to långskrift immediately? We can use deep learning for that. As you know, one of the first successful products built on top of convolutional neural networks was LeNet (http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf), a network for reading handwritten digits. This is similar but trickier. We will need a lot of labelled data to achieve this, and that's where this project comes in.

# how does it work? 
Letters and abbreviations are stored as bezier curves and stitched together by joining several of those and traversing the entire path. Thats not enough though, if you want to mimic human writing, as the connections between letters change depending on what velocity (speed and direction) that your pen tip has entering a new letter or syllable. To try and solve this, the package use a tracking algorithm with inertia and a spring force. So one point moves (the thought) and another point (the pen) follows the first point. Every sign can be fitted with its own speed multiplier. For instance, you'd have a greater speed writing 'skap' (a large signature) compared to 'rätt' (a small signature). The system calculates a speed itself that can be overridden. You can probably figure out how this all work by looking at the animation below. The two large 'skap' at the end has a much higher speed than the rest of the word. The word, by the way, says 'abmskapskap' which would probably translate to 'arbetsmarknadsskapskap' which is bogus word obviously. 

<p align="center">
  <img src="https://github.com/vbrg/melin/blob/main/ezgif.com-gif-maker.gif"/>
</p>

# todo
 - implement variable speed controller for each letter. Right now everything is linear
 - add a way to write sentences and not only words. 
 - add the notion of 'skrivlinje'
 - add more letters and abbreviations
