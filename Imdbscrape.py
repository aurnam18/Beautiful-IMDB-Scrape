import csv
import requests
from bs4 import BeautifulSoup
URL = 'https://www.imdb.com/search/title/?genres=comedy&sort=user_rating,desc&title_type=tv_series,mini_series&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f85d9bf4-1542-48d1-a7f9-48ac82dd85e7&pf_rd_r=YYK4F4117WVGRHNF0M0Z&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_gnr_5'
csvfile = open("top50comedy.csv", 'w')
csv_writer = csv.writer(csvfile)
csv_writer.writerow(["rank", "name", "length", "genre", "rating"])
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("div", class_="lister-list")
movies = results.find_all("div", class_="lister-item")
for movie in movies:
  rank_elem = movie.find("span", class_="lister-item-index")
  namestuff = movie.find("h3", class_="lister-item-header")
  name_elem = namestuff.find("a")
  length_elem = movie.find("span", class_="runtime")
  genre_elem = movie.find("span", class_="genre")
  ratingbar = movie.find("div", class_="ratings-bar")
  rating_elem = ratingbar.find("strong")
  if None in (rank_elem, name_elem, length_elem, genre_elem, rating_elem):
    continue
  rank = rank_elem.text.strip()
  name = name_elem.text.strip()
  length = length_elem.text.strip()
  genre = genre_elem.text.strip()
  rating = rating_elem.text.strip()
  csv_writer.writerow([rank, name, length, genre, rating])
csvfile.close()
