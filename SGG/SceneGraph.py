import torch
import torch.nn as nn
import torch.nn.functional as F

class SceneGraph(nn.Module):
    def __init__(self, num_classes, num_features):
        super(SceneGraph, self).__init__()
        self.num_classes = num_classes
        self.num_features = num_features

        self.fc1 = nn.Linear(num_features, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x