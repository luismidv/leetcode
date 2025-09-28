"""
You are building a perception system for an autonomous mobile robot.
You are given a dataset of images (RGB) and their corresponding bounding boxes in a JSON file with the following format:
"""
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import os
import pandas as pd

class Dataset(Dataset):
    def __init__(self, images,bboxes):
        self.images = images
        self.bboxes = bboxes
        self.data_dict = {}

    def __len__(self):
        return len(self.images)

    def __getitem__(self,idx):
        self.transform = transforms.Compose([
            transforms.Resize((224,224)),
            transforms.ToTensor(),
        ])

        image = self.transform(self.images[idx])
        bbox = list(self.bboxes[idx])
        self.data_dict[image] = bbox

        print(f"Image type {type(image)}")
        print(f"Bounding box type {type(bbox)}")
        return image,bbox




def dataset_reader(images_route, label_route):
    image_list = []
    labels_list = []
    for image in os.listdir(images_route):
        image_path = os.path.join(images_route, image)
        image = Image.open(image_path)
        image_list.append(image)

    labels = pd.read_json(label_route)
    labels.loc[2, "bbox"] = [30, 70, 220, 50]
    labels.loc[3, "bbox"] = [30, 70, 220, 50]
    labels.loc[4, "bbox"] = [30, 70, 220, 50]
    for label in labels["bbox"]:
        labels_list.append(labels)

    return image_list, labels_list

image_route = "./dataset/images"
label_route = "./dataset/labels.json"
image_list,labels_list = dataset_reader(image_route, label_route)
dataset = Dataset(image_list,labels_list)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
for (x,y) in dataloader:
    print(x)
    print(y)





