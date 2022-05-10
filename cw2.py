from cgi import test
import imghdr
import imp
from pyexpat import native_encoding
import numpy as np
import cv2






#sets the question count to 1 (to start from the beginning)
currentQuestion = 1
 
#main function
def cam():
        
    #SETS CASCADES
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
    hand_cascade = cv2.CascadeClassifier('D:\\University\\Interface\\Code\\cv2\\data\\haarcascades\\fist.xml')

    #SETS COLOURS to be used by different elements of the UI
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    WHITE = (255, 255, 255)

    #text position values for placing on the GUI

    question1Pos = (20, 200)
    question2Pos = (40, 200)

    ans1Pos = (100, 450)
    ans2Pos = (300, 450)

    ans1Prompt = (110, 350)
    ans2Prompt = (310, 350)
    font = cv2.FONT_HERSHEY_TRIPLEX

    #POLYGON VALUES (POSITIONS OF POINTS)
    pts = [(300, 360), (350, 460), (250, 460)]

    #ELLIPSE VALUES
    center = 110, 415
    axes = 50, 50
    angle = 0

    #SQUARE VALUES (BOTTOM LEFT AND TOP RIGHT POINTS)
    sp0 = 460, 460
    sp1 = 560, 360

    def detect(gray, frame):

        guess = 0

        #Sets the colour of the box
        boxCol = WHITE
        
        #Detects fists
        fist = hand_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in fist:
            #set the colour for feedback
            boxCol = GREEN
            #sets the user's guess to the value of 1
            guess = 1

            
            

        #detects faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
                
                    

            #detects smiles
            for (sx, sy, sw, sh) in smiles:
                #set the colour for feedback
                boxCol = RED
                #sets the user's guess to the value of 2
                guess = 2
                    
                    
                    
        #draws each of the shapes
        cv2.fillPoly(frame, np.array([pts]), boxCol)

        global currentQuestion
        if currentQuestion == 1:

            #sets the correct guess to the value of 2
            correctGuess = 2

            #place the text on the UI
            cv2.putText(uiWindow, "Which snippet of code would\n make the code output \"Hello World!\"?", question1Pos, font, 0.4, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Smile", ans1Prompt, font, 1, RED, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Fist", ans2Prompt, font, 1, GREEN, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "(\"Hello World!\")", ans1Pos, font, 0.5, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "(Hello World!)", ans2Pos, font, 0.5, WHITE, 1, cv2.LINE_AA)

            #Displays the code for the question
            questionImg = cv2.imread('question1.png',0)
            cv2.imshow('Question', questionImg)


            if guess == correctGuess:
                
                #Shows the output of the code and progresses the questions by one
                answerImg = cv2.imread('answer1.png',0)
                cv2.imshow('Output', answerImg)
                currentQuestion = currentQuestion + 1

                
                
            

        if currentQuestion == 2:

            #place the text on the UI
            cv2.putText(uiWindow, "Which snippet of code would\n make the code output \"hello\"?", question2Pos, font, 0.4, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Smile", ans1Prompt, font, 1, RED, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Fist", ans2Prompt, font, 1, GREEN, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "(x = 3)", ans1Pos, font, 0.5, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "(x == 3)", ans2Pos, font, 0.5, WHITE, 1, cv2.LINE_AA)

            #Displays the code for the question
            questionImg = cv2.imread('question2.png',0)
            cv2.imshow('Question', questionImg)

            #Sets the correct guess value to 1
            correctGuess = 1
            if guess == correctGuess:
                #Shows the output of the code and progresses the questions by one
                answerImg = cv2.imread('answer2.png',0)
                cv2.imshow('Output', answerImg)
                currentQuestion = currentQuestion + 1

        if currentQuestion == 3:

            #place the text on the UI
            cv2.putText(uiWindow, "Which snippet of code would\n make the code output the numbers 1-10?", question2Pos, font, 0.35, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Smile", ans1Prompt, font, 1, RED, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Fist", ans2Prompt, font, 1, GREEN, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "(x <= 10)", ans1Pos, font, 0.5, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "(x >= 10)", ans2Pos, font, 0.5, WHITE, 1, cv2.LINE_AA)

            #Displays the code for the question
            questionImg = cv2.imread('question3.png',0)
            cv2.imshow('Question', questionImg)

            #Sets the correct guess value to 2
            correctGuess = 2
            if guess == correctGuess:
                #Shows the output of the code and progresses the questions by one
                answerImg = cv2.imread('answer3.png',0)
                cv2.imshow('Output', answerImg)
                currentQuestion = currentQuestion + 1

        if currentQuestion == 4:

            #place the text on the UI
            cv2.putText(uiWindow, "Which snippet of code would\n make the code output \"John Smith\"?", question1Pos, font, 0.4, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Smile", ans1Prompt, font, 1, RED, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Fist", ans2Prompt, font, 1, GREEN, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "Nothing goes there", ans1Pos, font, 0.5, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "getName()", ans2Pos, font, 0.5, WHITE, 1, cv2.LINE_AA)

            #Displays the code for the question
            questionImg = cv2.imread('question4.png',0)
            cv2.imshow('Question', questionImg)


            #Sets the correct guess value to 1
            correctGuess = 1
            if guess == correctGuess:
                #Shows the output of the code and progresses the questions by one
                answerImg = cv2.imread('answer4.png',0)
                cv2.imshow('Output', answerImg)
                currentQuestion = currentQuestion + 1

        
        #if all the questions are completed:
        if currentQuestion == 5:
            
            text1 = (45, 200)
            text2 = (40, 260)

            #Display completion text
            cv2.putText(uiWindow, "All Questions Complete", text1, font, 1, WHITE, 1, cv2.LINE_AA)
            cv2.putText(uiWindow, "SMILE GESTURE to Exit", text2, font, 1, RED, 1, cv2.LINE_AA)

            #Guess is 3 so that the user can't continue
            correctGuess = 2

            if guess == correctGuess:
                
                video_capture.release()                                 
                cv2.destroyAllWindows()
            
        #update frame    
        return frame
            


    video_capture = cv2.VideoCapture(0)
    while video_capture.isOpened():

        uiWindow = np.zeros((512,512,3), np.uint8)
        
            
    # Captures video_capture frame by frame
        _, frame = video_capture.read()
        
        # To capture image in monochrome                   
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 


        # calls the detect() function   
        canvas = detect(gray, frame)  
        
        # Displays the result on camera feed                    
        cv2.imshow('Video', canvas)
        cv2.imshow('Main', uiWindow)

        # The control breaks once q key is pressed
        a = cv2.waitKey(1)                       
        if(a==ord('q')):
            break
        
    # Release the capture once all the processing is done.
    video_capture.release()                                
    cv2.destroyAllWindows()
#run the function
cam()