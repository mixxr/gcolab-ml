import torch
import torch.nn as nn

class DNA_CNN(nn.Module):
    def __init__(self, sequence_length):
        super(DNA_CNN, self).__init__()
        # 1D Convolution looks for small motif patterns (like "filters") in the sequence
        self.conv1 = nn.Conv1d(in_channels=4, out_channels=32, kernel_size=9, padding=4)
        self.pool = nn.MaxPool1d(kernel_size=4)
        
        # Fully connected layers to output a binding probability
        self.fc1 = nn.Linear(32 * (sequence_length // 4), 64)
        self.fc2 = nn.Linear(64, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # x shape: [batch_size, 4, sequence_length]
        x = torch.relu(self.conv1(x))
        x = self.pool(x)
        x = x.view(x.size(0), -1) # Flatten
        x = torch.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

# Example initialization for a 100-base-pair DNA sequence
model = DNA_CNN(sequence_length=100)
print(model)
