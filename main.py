from scraper.main_scraper import scrape
from image_reader.main_image_reader import read_image

scrape()
read_image()

# add path to this folder to globals
# pip install all the packages
# run main.py for scraping data (for example by providing it in crontab)
# plot your data by using analyze_files and plot_files
