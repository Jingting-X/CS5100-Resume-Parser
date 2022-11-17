# CS5100-Resume-Parser

<!-- ABOUT THE PROJECT -->
## About The Project
This app can parse a free-format resume into a structured format with the information needed. 
It will significantly improve the user's efficiency in processing resumes.

![](https://i.ibb.co/0yDZrT0/picture-1.png)
![](https://i.ibb.co/rMz4WNV/picture-2.png)

## Targeted Environment

|                  | Version |                                                                                                         Introduction                                                                                                          |
|:----------------:|:-------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|      Python      | 3.9.13  |                                 Python programming language is being used in web development, Machine Learning applications, along with all cutting edge technology in the Software Industry.                                 |                                                                                                                                                                                             |
|      Flask       |  1.1.2  |                                                                                    Flask is a web application framework written in Python.                                                                                    |
|  spaCy(Package)  |  2.3.8  | spaCy is an open-source software library for advanced natural language processing. It features state-of-the-art speed and neural network models for tagging, parsing, named entity recognition, text classification and more. |
| pymupdf(Package) | 1.21.0  |                               PyMuPDF adds Python bindings and abstractions to MuPDF, a lightweight PDF, XPS, and eBook viewer, renderer, and toolkit. It can be used to decrypt the document.                                |

## PEAS Environment

|  Agent Type   |                      Performance Measure                      |    Environment     |   Actuators    |                   Sensors                   |
|:-------------:|:-------------------------------------------------------------:|:------------------:|:--------------:|:-------------------------------------------:|
| Resume Parser | Parse resume’s contents into different categories accurately. | Internet, Computer | Screen display | Web pages, Resumes uploaded by users, Mouse |

## Run In Terminal
```
  export FLASK_ENV=development
  export FLASK_APP=app
  flask run
```

