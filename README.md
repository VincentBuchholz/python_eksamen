# python eksamen

To run project, use: python3 price_predictor.py --image path (path = path to any of the images in the images folder, these have corresponding bilbasen data in the data folder)

more car data can be scraped with bilbasen.py

numberplate_detector.py can be used to get the text from the numberplate of a car.

motorregister.py scrapes data from motorregisteret and findsynsrapport.


# Requirements:
- selenium
- webdriver-manager
- opencv-python
- easyOCR

## Installation:
- conda install -c conda-forge selenium -y
- conda install -c conda-forge webdriver-manager -y
- pip install opencv-python

## For X86 computers use:
- conda install -c conda-forge easyocr

## For ARM computers use:
- pip install easyocr
    
## Other requirements (These come pre packaged with anaconda):
- bs4
- json
- requests
- re
- pandas
- csv
- numpy