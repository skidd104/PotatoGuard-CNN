<a id="readme-top"></a>

<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
     <li><a href="#Model Confusion Matrix">Model Info</a></li>
     <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project

[![Confusion Screen Shot][cover-screenshot]](https://example.com)


PotatoGuard is a full-stack AI-powered web application designed to help farmers and agronomists identify potato leaf diseases in real-time. By leveraging a Convolutional Neural Network (CNN) trained on thousands of plant pathology images, PotatoGuard provides instant diagnosis and actionable treatment recommendations.

## Features
* eal-time Image Analysis: Upload leaf photos and get results in seconds.
* Deep Learning Backend: Powered by a customized CNN (TensorFlow/Keras) optimized for high accuracy.
* Actionable Insights: Provides specific treatment protocols (fungicides, irrigation, pruning) for Early and Late Blight.
* Mobile-First Design.
* Scan History: Track field health trends locally using browser storage.


## Built With
* [![Flask][Flask-badge]][Flask-url]
* [![Python][Python-badge]][Python-url]
* [![TensorFlow][TensorFlow-badge]][TensorFlow-url]
* [![TailwindCSS][Tailwind-badge]][Tailwind-url]
* [![JavaScript][JS-badge]][JS-url]

## Model & Inference
1. The core of PotatoGuard is a CNN model trained to identify three distinct states:

2. Early Blight (Alternaria solani)

3. Late Blight (Phytophthora infestans)

4. Healthy


## Model Confusion Matrix Result

[![Confusion Screen Shot][confusion-matrix-screenshot]](https://example.com)

## Note
While Training the model i notice if you save the model while using data augmentation you will run into false result even if your model is almost 100% accuracy. Solution is to transfer the weights of model and save it into the base model.


## Installation
1. Clone Repository
```git
git clone https://github.com/skidd104/PotatoLeafDiseaseDetection
cd Potato
```

2. Create Virtual Environment
```python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Run
```
cd WebApp
python app.py
```

## Train Machine Learning CNN
The model is trained on this https://www.kaggle.com/datasets/muhammadardiputra/potato-leaf-disease-dataset

1. Go to ModelMaking Folder

2. Use the potatoe_leaf_training.ipynb the other is outdated

## License

Distributed under the project license. See `LICENSE` for more information

<p align="right">(<a href="#readme-top">back to top</a>)</p>


[confusion-matrix-screenshot]: /img/matrix.png
[cover-screenshot]: /img/cover.png

[Flask-badge]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/
[Python-badge]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[TensorFlow-badge]: https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/
[Tailwind-badge]: https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white
[Tailwind-url]: https://tailwindcss.com/
[JS-badge]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JS-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
