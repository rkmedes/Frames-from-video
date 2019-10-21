import cv2

def getFrame(videoObject,sec,count,imagePath):
    videoObject.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image=videoObject.read()
    if hasFrames:
      image_name="image"+str(count)+".jpg"
      cv2.imwrite(imagePath+'/'+image_name,image)
    return hasFrames

def captureFrame(videoPath,framerate,imagePath,model,x_single_embedding):
    videoObject=cv2.VideoCapture(videoPath)
    sec=0.0
    count=1
    success=getFrame(videoObject=videoObject,sec=sec,count=count,imagePath=imagePath)
    while success==1:
        sec+=framerate
        sec=round(sec,2)
        count+=1
        success=getFrame(videoObject=videoObject,sec=sec,count=count,imagePath=imagePath)
    videoObject.release()
