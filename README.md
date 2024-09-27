# SeeFood Hotdog Classification Web Application
Determine if there is hotdog in the picture.

## To run the app

1. Download necessary library listed in app.py (I forgot to create python virtual environment and that will never happen again). 
2. Change your directory to current project folder.
3. run `python3 app.py` or `python app.py`

## How SeeFood created / How SeeFood run

1. Create tensorflow model
    - Find training and testing data. I use [this](https://www.kaggle.com/datasets/yashvrdnjain/hotdognothotdog).
    - Categorize the image into different folders (hotdog and not hotdog) for tensorflow to understand.
    - [Optional] Perform image augmentation. 
    - Check labels and adjust if necessary. (IMPORTANT!)
    - [Optional] Create prefetch buffer and callbacks function for run time optimziation.
    - Come up with tensorflow models and metrics to determine model performance (I use model accuracy and binary cross entropy).
    - Train model with training and validation data.
    - Test model with testing data.
    - Determine how to improve model (overfitting or underfitting, dropout layers, adjust learning rate, try new activation functions, image augmentation, more data...)
    - Save weights (not the model, ONLY WEIGHTS, I have to set model structure again in app.py)

2. Design front end 
    - Use HTML, CSS, and JavaScript to design web application 

3. Do back end
    - Use flask to handle image processing, decision machine and output result 


## Conclusion
Harder than I expected but it was fun. 
