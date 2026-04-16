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
     <li><a href="#Model Architecture">Model Info</a></li>
     <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project

[![Confusion Screen Shot][cover-screenshot]](https://example.com)


PotatoGuard is a computer vision project centered on a custom-architected Convolutional Neural Network (CNN) designed for the automated classification of Solanum tuberosum (potato) foliar pathologies. The core engine utilizes a deep learning pipeline to distinguish between Early Blight, Late Blight, and Healthy tissue with high precision.

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

## Model Architecture
* Architecture: A multi-layered CNN optimized with Global Average Pooling and Dropout layers to prevent overfitting on specific field backgrounds.
* Inference Strategy: Employs a Base-Model Inference protocol, bypassing training-time data augmentation to ensure deterministic and stable predictions in production environments.
* Dataset: Trained on the PlantVillage dataset, involving rigorous preprocessing including color space normalization and target-size rescaling to 224 x 224 pixels.
* Deployment: Integrated into a Flask-based REST API to demonstrate real-world model serving and edge-case handling.


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

[contributors-shield]: https://img.shields.io/github/contributors/skidd104/nScript.svg?style=for-the-badge
[contributors-url]: https://github.com/skidd104/nScript/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/skidd104/nScript.svg?style=for-the-badge
[forks-url]: https://github.com/skidd104/nScript/network/members
[stars-shield]: https://img.shields.io/github/stars/skidd104/nScript.svg?style=for-the-badge
[stars-url]: https://github.com/skidd104/nScript/stargazers
[issues-shield]: https://img.shields.io/github/issues/skidd104/nScript.svg?style=for-the-badge
[issues-url]: https://github.com/skidd104/nScript/issues
[license-shield]: https://img.shields.io/github/license/skidd104/nScript.svg?style=for-the-badge
[license-url]: https://github.com/skidd104/nScript/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/michael-ian-leguira-a5b9793aa/
[product-screenshot]: images/cover.png

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
