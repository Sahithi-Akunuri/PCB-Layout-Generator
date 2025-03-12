from flask import Flask, request, jsonify
import torch
import torch.nn as nn
import pandas as pd

app = Flask(__name__)

class PCBModel(nn.Module):
    def __init__(self):
        super(PCBModel, self).__init__()
        self.fc1 = nn.Linear(5, 64) 
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 2)  

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)  
        return x

model = PCBModel()
model.load_state_dict(torch.load("pcb_layout_model.pth", map_location=torch.device('cpu')))
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  
        df = pd.DataFrame(data)  
        input_tensor = torch.tensor(df.values, dtype=torch.float32)

        with torch.no_grad():
            predictions = model(input_tensor).tolist()  

        return jsonify({"predictions": predictions})  

    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/', methods=['GET'])
def home():
    return "Flask is running!"

if __name__ == '__main__':
    app.run(debug=True)
