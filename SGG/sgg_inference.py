from SceneGraph import SceneGraph
import torch

class SGGInference:
    def __init__(self, model_path):
        self.model = SceneGraph(16, 2318)
        checkpoint = torch.load(model_path)
        self.model.load_state_dict(checkpoint['model_state_dict'])

    def infer(self, X):
        print(self.model(X).shape)
        return torch.argmax(self.model(X), dim=1).item()
