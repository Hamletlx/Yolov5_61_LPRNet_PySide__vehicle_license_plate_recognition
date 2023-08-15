import torch
import cv2
import numpy as np
from models.experimental import attempt_load
from utils.general import non_max_suppression

def transform(img, device):
    # Convert
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to(device)
    img=img.float()
    img/=255.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)
    return img

def detect_yolov5(image, model, device):
    # device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # model = attempt_load('weights/yolov5_best.pt', map_location=device)

    image = cv2.resize(image, (640, 640))
    new_image = transform(image, device)
    pred = model(new_image)[0]
    pred = non_max_suppression(pred, 0.8, 0.5)[0]
    pred = pred.cpu().tolist()

    result1 = image.copy() 
    result2 = []
    result3 = []
    for i in pred:
        x1,y1,x2,y2 =map(int,i[:4])
        p, c=i[4], i[5]
        classs='Other'
        if -0.01<c<0.01:
            classs='Green'
        elif 0.99<c<1.01:
            classs='Blue'

        cv2.rectangle(result1,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.putText(result1, classs + ' ' + str(round(p,2)), (x1,y1-3), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2)

        img=image[y1:y2,x1:x2]
        result2.append(img)
        result3.append(classs)

    return result1,result2,result3
    
        
if __name__ == '__main__':
    image = cv2.imread("C:/Users/hamlet/Desktop/b1.jpg")
    result1,result2=detect_yolov5(image)
    cv2.imshow('result1',result1)
    cv2.waitKey(0)