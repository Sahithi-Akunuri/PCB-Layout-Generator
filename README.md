# PCB-Layout-Generator

A deep-learning-based structured 2D layout generation model for PCB component placement. The application can be used via:

* REST API (Flask)
* Google Colab Notebook

#Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Visualization](#visualization)
* [Example API Requests](#example_api_requests)
* [License](#license)


#Features

✅ Predicts optimal PCB component placements using deep learning.
✅ Flask API to integrate with other applications.
✅ Google Colab support for easy execution in the cloud.
✅ Visualizations using Matplotlib/OpenCV.

#Installation

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

#Usage

## Option 1: Run the Flask REST API
1️⃣ Start the Flask Server

```
python app.py
```
* The API will start on http://127.0.0.1:5000/.

2️⃣ Test with Postman or Curl
To test the API, send a POST request to /predict with a JSON payload:

```
{
  "components": [[1, 0.5, 0.5, 2, 3], [2, 0.3, 0.3, 1, 2]],
  "connections": [[0, 1]],
  "obstacles": [[0.2, 0.2, 0.1, 0.1]]
}
```

Use curl:

```
curl -X POST "http://127.0.0.1:5000/predict" -H "Content-Type: application/json" -d @input.json
```

##Option 2: Run in Google Colab

1️⃣ Open Google Colab.
* Open [Google Colab](https://colab.google/)
* Upload colab_notebook.ipynb from this repository.

2️⃣ Run All Cells
* The notebook will prompt you to upload a CSV file.
* The model will process the data and visualize the PCB layout.

#Visualization

1️⃣ Matplotlib
* If using Flask, the layout will be plotted using Matplotlib.

2️⃣ OpenCV
* For better visualization


#Example API Requests

1️⃣ Using Python Requests

```
import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "components": [[1, 0.5, 0.5, 2, 3], [2, 0.3, 0.3, 1, 2]],
    "connections": [[0, 1]],
    "obstacles": [[0.2, 0.2, 0.1, 0.1]]
}

response = requests.post(url, json=data)
print(response.json())
```

#License

This project is licensed under the MIT License.
