# img-data - PyPi package to make image datasets
img-data is a small python package which will help you gather images from popular stock images sites and process them into image datasets. It can be incredibly easy to make a new image dataset for your deep learning project using img-data.

## Overview
img-data provides 2 major functions :-
- Gather images from some of the most popular stock image websites using the API - No need to write the whole Python code to extract all the images yourself!
- It also conveniently divides those image into train, test and validation directories, so you have a dataset ready to use

## Installation
You can PyPi repositiory to install img-data
```
$ pip install imgdata
```
## Usage
I am working on simplifying it further but as of now, using imgdata involves 3 steps
1. importing the library
2. creating the object
3. calling requisite function

## Functions
Following functions are available for use in the library:
1. **pexels()** -> Download data from pexels API
2. **unsplash()** -> Download data from unsplash API
3. **transform_data()** -> Divide data at a provided path into train/test/validation

### Downloading Images and Making Dataset
```
$ import imgdata
$ obj = imgdata.Api()
$ obj.pexels(query = query,
            api_key = api_key,
            count = count,
            ratio = ratio,
            divide = True/False,
            validation = True/False)
```

#### Arguments for Data Download functions
- **query**: You need to specify topic of image dataset. It can be a one word or multi word query. This will be the search query for API to work on.
- **api_key**: You need to provide API key through which to access website's data. Keep in mind, some sites limit use of API. Program may generate an error if limits exceed. I'll try to generate a warning beforehand for such sites when they are used.
- **count**: Total number of images needed. Again please check with site regarding the limit.
- **ratio**: Ratio in which you needed images divided into train and test. Default ratio is 0.2.
- **divide**: Setting this argument to `True` will automatically divide the downloaded images in train and test category
- **validation**: Only applicable if `divide` is set to `True`. Separates data into train/test/validation instead of train/test.

#### File Structure for Data Download Functions
```bash
- if `divide` is set to `True`:
└── dataset
    ├── train
    │   └── *.jpg
    ├── test
    │   └── *.jpg
    └── val (if validation set to `True`)
        └── *.jpg

- if `divide` is set to `False`

└── dataset
    └── *.jpg


```

### Transforming Available Dataset into Train, Test, Validation
Shuffles the data converts them into train/test/val modules.

```
$ import imgdata
$ obj = imgdata.Api()
$ obj.transform_data(path = data path
                    ratio = ratio,
                    validation = True/False)
```

#### Arguments:
- **path**: The path to the dataset.
- **ratio**: Ratio of data for test and validation sets. (Default: 0.2)
- **validation**: If set to true, files will be divided into train/test/val instead of train/test

#### File Structure for Transforming data
```bash
- Initial File Structure

└── dataset
    ├── Class A
    └──  Class B




- Structure after transforming:
└── dataset
    ├── train
    │   ├── Class A
    │   └── Class B
    ├── test
    │   ├── Class A
    │   └── Class B
    └── validation (if set to True)
        ├── Class A
        └── Class B

```

## Keypoints
- The ratio is mentioned is total count of files for test and validation individually. Eg. Assuming a ratio of 0.2 and a total of 10 files, test will have 2, validation will have 2 and train will have 6 files.
- The path for transforming data should be to folder containing the classes


## License
MIT License

Copyright (c) 2020 Arohan Ajit

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
