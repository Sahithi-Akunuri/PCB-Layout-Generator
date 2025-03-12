# PCB-Layout-Generator

A deep-learning-based structured 2D layout generation model for PCB component placement. The application can be used via:

* REST API (Flask)

# Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Troubleshooting](#troubleshooting)
* [License](#license)


# Features

✅ Predicts optimal PCB component placements using deep learning.
✅ Flask API to integrate with other applications.
✅ Visualizations using Matplotlib/OpenCV.

# Installation

1️⃣ Clone the Repository
```
git clone https://github.com/your-username/pcb-layout-generator.git
cd pcb-layout-generator
```

2️⃣ Install Dependencies
Make sure you have Python 3.8+ installed. Then, install the required libraries:

```
pip install -r requirements.txt
```

3️⃣ Download or Train the Model
Place the pre-trained model in the project directory as:
```
pcb-layout-model.pth
```

# Usage

## Option 1: Run the Flask REST API
1️⃣ Start the Flask Server

```
python app.py
```
* The API will start on http://127.0.0.1:5000/.
* After running, you should see output like:
```
Running on http://127.0.0.1:5000/
```

2️⃣ Test the API with Postman
To test the API, send a POST request to /predict with a JSON payload:

➤ POST Request to /predict

* Open Postman.

* Select POST method.

* Enter the URL: http://127.0.0.1:5000/predict

* Go to the Body tab and select raw → JSON.

* Input the following sample JSON data:

```
[
    {"Component_Type": 1, "Width": 2.5, "Height": 3.1, "Power": 10, "Connections": 2},
    {"Component_Type": 2, "Width": 1.8, "Height": 2.2, "Power": 5, "Connections": 3}
]
```
* Click Send.
  
* You should receive a response like:

```
{
    "predictions": [
        [
            -0.12908372282981873,
            -0.19454966485500336
        ],
        [
            0.030656568706035614,
            -0.12306378781795502
        ]
    ]
}
```

* In flask server url: http://127.0.0.1:5000/, you should receive a response like this:
```
Flask is running!
```

# Troubleshooting

* 404 Not Found: Ensure you are hitting the correct endpoint (/predict).

* 405 Method Not Allowed: Use POST instead of GET.

* CUDA Error: Load the model using torch.load('pcb_layout_model.pth', map_location=torch.device('cpu')) if running on a CPU-only system.

* Ensure that pcb_layout_model.pth is in the same directory as app.py.

# License

This project is licensed under the MIT License.
