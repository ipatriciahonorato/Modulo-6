#Import the libraries
import cv2

video=True #if true start the video

#Funtion to detect the object
def detect(path):

    #Classificator
    face_cascade = cv2.CascadeClassifier(
    filename=f"{cv2.data.haarcascades}/haarcascade_frontalface_default.xml"
    )

    #Condition to start the function
    if video:
        video_cap = cv2.VideoCapture('arsene.mp4') 
    else:
        ('No video')

    while True:
        # Capture frame-by-frame
        ret, img = video_cap.read()

        #converting to gray image for faster video processing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Parameters of CascadeClassifier
        faces = face_cascade.detectMultiScale(gray, 
        scaleFactor=1.5, # Mudança de escala a cada passada
        minNeighbors=5 # Verifier the neighbors before promote the point 
        )

        # if at least 1 face detected
        if len(faces) >= 0:
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, pt1= (x, y), pt2= (x + w, y + h), color=(0, 255, 0), thickness=2)
                
            # Display the resulting frame
            cv2.imshow('Face Detection on Video', img)

            #wait for 'c' to close the application
            if cv2.waitKey(1) & 0xFF == ord('c'):
                break
    #Defining size for the output video
    width  = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
    height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    #Local and parameters for the output video
    output_video = cv2.VideoWriter( './saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))
    output_video.release()
    video_cap.release()


#Main Function to start the program
def main():
    cascadeFilePath="haarcascade_frontalface_alt.xml"
    detect(cascadeFilePath)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()