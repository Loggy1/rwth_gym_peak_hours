from scraper.main_scraper import scrape
from image_reader.main_image_reader import read_image

# This file is used to run the scraper and the image reader
# We will pull the picture with the scraper and then read the number in the picture with the image reader
scrape()
read_image()