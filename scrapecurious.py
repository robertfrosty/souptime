import requests
import urllib.request
from bs4 import BeautifulSoup

import mysql.connector

cnx = mysql.connector.connect(user='dev', password='kP_^zZ99uuSE+}$7', host='localhost', database='soups')

def scrapecurious():
	base = "https://www.epicurious.com"

	for x in range(0,50):
		page = requests.get("https://www.epicurious.com/search/soup?content=recipe&sort=relevance&page=" + str(x)).content
		soup = BeautifulSoup(page, "html.parser")

		for y in soup.find_all("article", {"class":"recipe-content-card"}):
			url = base + y.find("a", {"class":"view-complete-item"})["href"]
			cur = cnx.cursor(buffered=True)
			cur.execute("SELECT * FROM soups WHERE url = %s", [url])
			if cur.rowcount > 0:
				print('Same')
				continue
			cur.close()

			page = requests.get(base + y.find("a", {"class":"view-complete-item"})["href"]).content
			soup = BeautifulSoup(page, "html.parser")

			print(soup)

			ingred = ""
			for z in soup.find("ol", {"class":"ingredient-groups"}).find_all("li", {"class":"ingredient"}):
				ingred += z.text + "&*"

			steps = ""
			for v in soup.find("ol", {"class":"preparation-steps"}).find_all("li", {"class":"preparation-step"}):
				steps += v.text.strip() + "&*"

			spname = soup.find("h1", {"itemprop":"name"}).text

			try:
				image = soup.find("img", {"class":"photo"})
				secid = id_generator() + "." + image["srcset"].split(".")[3]
				urllib.request.urlretrieve(image["srcset"], "static/soupimgs/" + secid)
			except:
				secid = "default.jpg"

			cur = cnx.cursor()
			cur.execute("INSERT INTO soups (SoupName, Ingredients, Directions, image, url) VALUES (%s, %s, %s, %s, %s)", [spname, ingred, steps, secid, url])
			cur.commit()
			cur.close()

	return

scrapecurious()
