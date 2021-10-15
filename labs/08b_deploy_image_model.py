import torch
import torchvision.models as models

# Create a model that wraps a pretrained MobileNetV3
# and outputs top 5 predicted classes in ImageNet
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.model = models.mobilenet_v3_small(pretrained=True)
        # Normalization parameters
        self.mean = torch.tensor([0.485, 0.456, 0.406]).view(1, 3, 1, 1)
        self.std = torch.tensor([0.229, 0.224, 0.225]).view(1, 3, 1, 1)

    def forward(self, x):
        # Preprocess
        x = x / 255.0
        x = x - self.mean
        x = x / self.std
        # Do inference and get top 5 classes
        return torch.topk(self.model(x), 5, 1)[1]

model = Model()

# Put model in eval mode
model.eval()

# Use a dummy input for JIT trace
x = torch.ones(1, 3, 224, 224)
trace = torch.jit.trace(model, x)

# Save model
torch.jit.save(trace, 'model.zip')
