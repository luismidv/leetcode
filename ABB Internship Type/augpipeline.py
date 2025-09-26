import cv2
import numpy as np
import torch
from torchvision import transforms
from PIL import Image

def preprocess_cv(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image =cv2.resize(image,(224,224))
    image =image.astype(np.float32)/255.0
    img = image-np.mean(image,keepdims=True)/np.std(image,keepdims=True)
    img = torch.from_numpy(img.transpoe(2,0,1)
    return img

def preprocess_torchv(image):
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std = [0.229, 0.224, 0.225])
    ])
    return transform(image)

def preprocess (image_path):
    image = Image.open(image_path)
    image = preprocess_torchv(image)
    return image
