# Lane line detection in autonomous vehicles
If you are wondering how smart cars automatically follow the driverless lane line and go to the desired route, I have prepared an article for you using an applied image processing algorithm.
Essentially, the Hough Line Transform structure, which has similar logic in all image processing algorithms, is used.I will create an example scenario using the Python programming language.

In fact, what is important here is the functionality of the cameras on the front bumpers of autonomous vehicles. While the vehicle is in motion, the cameras continuously process the image. The most important thing is to be able to detect the lane.

## Original Picture
![orijin](https://github.com/user-attachments/assets/71281e19-beef-4afb-9987-6e1548a2faaa)

## Masked Picture
![masked](https://github.com/user-attachments/assets/37985a87-160a-45e1-9f98-4e02c03e2a1b)

## Detected Picture
![painted](https://github.com/user-attachments/assets/dccab1ac-174d-408f-862e-ca6047fa0c83)

You can find my article in which I explain the codes in detail [here](https://mustafaulas.net/Article/ArticleDetail/3009/how-do-autonomous-vehicles-detect-lane-lines).

