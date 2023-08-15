import torch
import cv2
import numpy as np

from models.LPRNet import build_lprnet, CHARS



def transform(img, device):
    img = cv2.resize(img, (94, 24))
    img = img.astype('float32')
    img -= 127.5
    img *= 0.0078125
    img = np.transpose(img, (2, 0, 1))
    img = np.expand_dims(img, axis=0)
    img = torch.from_numpy(img)
    img = img.to(device)
    return img


def check_license_plate(plate_number):
    if len(plate_number) != 7 and len(plate_number) != 8:
        return False
    if plate_number[0] not in CHARS[:31]:
        return False
    if plate_number[1] not in CHARS[41:67]:
        return False
    for char in plate_number[2:]:
        if char not in CHARS[31:67]:
            return False
    return True


def detect_lprnet(images, model, device):
    # model = build_lprnet(lpr_max_len=8, phase=False, class_num=len(CHARS), dropout_rate=0.0)
    # device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # model.to(device)
    # model.load_state_dict(torch.load("weights/Final_LPRNet_model.pth"))

    resultlist=[]
    for img in images:
        img = transform(img, device)
        
        prebs = model(img)
        prebs = prebs.cpu().detach().numpy()
        
        result=''
        for i in range(prebs.shape[0]):
            preb = prebs[i, :, :]
            preb_label = list()
            for j in range(preb.shape[1]):
                preb_label.append(np.argmax(preb[:, j], axis=0))
            no_repeat_blank_label = list()
            pre_c = preb_label[0]
            if pre_c != len(CHARS) - 1:
                no_repeat_blank_label.append(pre_c)
            for c in preb_label: # dropout repeate label and blank label
                if (pre_c == c) or (c == len(CHARS) - 1):
                    if c == len(CHARS) - 1:
                        pre_c = c
                    continue
                result += CHARS[c]
                pre_c = c
        resultlist.append(result)
    return resultlist



if __name__ == '__main__':
    images = []
    img1 = cv2.imdecode(np.fromfile("C:/Users/hamlet/Desktop/123/沪AD58333.jpg", dtype=np.uint8), 1)
    img2 = cv2.imdecode(np.fromfile("C:/Users/hamlet/Desktop/123/沪ADE6010.jpg", dtype=np.uint8), 1)
    img3 = cv2.imdecode(np.fromfile("C:/Users/hamlet/Desktop/123/苏CD05935.jpg", dtype=np.uint8), 1)
    img4 = cv2.imdecode(np.fromfile("C:/Users/hamlet/Desktop/123/皖AD10222.jpg", dtype=np.uint8), 1)
    images.append(img1)
    images.append(img2)
    images.append(img3)
    images.append(img4)
    resultlist = detect_lprnet(images)

    for result in resultlist:
        print(result)