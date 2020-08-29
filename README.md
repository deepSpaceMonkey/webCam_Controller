# webCam-Controller

Snippet:

     This project was SOOOO COOl! Basicly you control the computer using your camera. You get an object with a unique color, 
     in this case blue, the program will locate it, put a box around it, and track it. If you move the object up, scroll up. 
     If you move the object down, scroll down.

Psuedocode:

     1. Open the camera
     2. Specify the color the camera should find
     3. Put camera in infinite loop to keep it open (capture more than 1 frame)
     4. Create a mask to remove all color hide all color except for the blue color (black for hidden, white for not hidden)
     5. Create contours to find the size of object
     6. Create condition to ignore noise (random stuff in background that are smaller in size than the object)
     7. Create a rectangle around the object to get actual coordinates
     8. If the object is moving up (y coordinate increasing) scroll up
     9. Same for scrolling down
     
     
Challenges and Solutions:

     1. Isolating out the noise:
         - The program was picking out some wacky colors from the background which made it impossible to effectilvy control 
         anything. Like why is there blue on my white wall and brown closet lol. I created a mask to find where exactly it 
         was picking up those colors and to get their general size. Then I got the size of my object and created a condition 
         to ignore values smaller than a point between the 2 sizes. In this case anything smaller than 40,000.
     
     2. Converting RGB colors to HVC:
         - I didn't know what HVC (Hue, Value, Chroma) was and just put in the RGB values in. This resulted in my object not
         getting recognized. There is an actual formula to convert which is quite tedious, but after converting, it now 
         recognized the obejet.
     

Possible Improvements and How You Can Use This :

     1. There is a limitation to this in that it can't really be used like an infrared remote. However, I can take the size of
     the screen to create boundries. And then if the object is in that part of the graph, then it will close the browser 
     similar to closing the browser by clicking x on the top left corner. 
     
     2. It would be really sick read license plate numbers and outputting to a txt file. Usually they are black letters on 
     white painted metal. If there is a letter, perhaps it can be recognized from the outline just like the object was 
     outlined using contours in this program. 
     
     3. Download the necceasry libraries (pyautogui and numpy and cv2)
     
     4. You can change the blue_upper and blue_lower to have it recognize the color of your choice. Make sure it is different 
     than your surroundings so the program can lock on.
