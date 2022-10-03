# Coffee Flavors Analyzer
#### Video Demo:  https://youtu.be/WYgWJc4UbIY

### **Description**:
The main idea representing this software, arises in the desire from obtain insight from La Celia farm coffee data since 2019.

Coffee samples for every harvest in Colombia are analyzed, and the results are presented in pdf documents. But the majority of coffee growers does not know how to do with this results beyond identify the flavors presented in their coffee farm.

Nevertheless, this information can be useful to obtain correlation between variables, or track defects which are produced in the transformation process of the seed since is manually picked until it is dehydrated.

As a first stept in the development of this Software is to extract and organize the information in order to be statistically analized in the second part of the development.

Specific information of the software design are showed below:

```bash
project.py
```
This file takes as input (*using sys*), the folder path containing the pdf documents to extract the information and outputs a data.json file compatible to be readed as pandas dataframe.

The information is separated into different rectangles, represented by coordinates:

top left: ($x_0$, $y_0$)

top right: ($x_1$, $y_0$)

bottom left: ($x_0$, $y_1$)

bottom right: ($x_1$, $y_1$)

Every rectangle contains specific data that is being organized as a list of dictionaries.

```python
information_extraction_from_pdf()
```
This function takes the path validated from other two functions and using *PyMuPDF* module reads every pdf document and extract the information.

#### **Installation**
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules.

```bash
pip install -r requirements.txt
```

#### **Usage**

```python
#Instructions
python project.py --help
```
```python
#Instructions
python project.py --path [name path of the folder]
```

### **Additional Modules**
```bash
extraction_coordinates.py [file_path]
```
This module is used to obtain the coordinates and assure the data that is going to be extracted.

```bash
data_analizer .py
```
This module is used to check if the data.json output is suitable to be visualized.