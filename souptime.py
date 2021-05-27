import requests
import string
import random
import urllib.request
from bs4 import BeautifulSoup
from flask import Flask, Blueprint, render_template, url_for, redirect, request

from dbinit import mysql

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))

souptime = Blueprint('souptime', __name__)

@souptime.route("/")
def homepage():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM soups ORDER BY RAND() LIMIT 1")
	tmpval = cur.fetchone()
	cur.close()

	soupname = tmpval[1]
	soupingred = tmpval[2].split("&*")[:-1]
	soupdir = tmpval[3].split("&*")[:-1]
	soupimg = tmpval[4]
	soupurl = tmpval[5]
	soupid = tmpval[0]

	return render_template("main.html", sn = soupname, si = soupingred, sd = soupdir, simg = soupimg, surl = soupurl, sid = soupid)

@souptime.route("/soups/<soupid>")
def soupshare(soupid):
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM soups WHERE id = %s", [soupid])
	if cur.rowcount > 0:
		tmpval = cur.fetchone()
		cur.close()

		soupname = tmpval[1]
		soupingred = tmpval[2].split("&*")[:-1]
		soupdir = tmpval[3].split("&*")[:-1]
		soupimg = tmpval[4]
		soupurl = tmpval[5]
		soupid = tmpval[0]

		return render_template("main.html", sn = soupname, si = soupingred, sd = soupdir, simg = soupimg, surl=soupurl, sid=soupid)

	cur.close()
	return "ERROR 404"

@souptime.route("/searchsoup", methods=["GET", "POST"])
def searchsoup():
	if request.method == 'POST':
		tmpvar = request.form["searchinfo"]

		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM soups WHERE INSTR(SoupName, %s)", [tmpvar]) > 0
		tmpval = cur.fetchall()
		cur.close()

		if cur.rowcount > 0:
			return render_template("sr.html", soups=tmpval)

		return render_template("sre.html")
		#return redirect(url_for('homepage'))
	else:
		return render_template("sr.html", soups=[])

@souptime.route("/scrapecurious")
def scrapecurious():
	base = "https://www.epicurious.com"

	for x in range(31,50):
		page = requests.get("https://www.epicurious.com/search/soup?content=recipe&sort=relevance&page=" + str(x)).content
		soup = BeautifulSoup(page, "html.parser")

		for y in soup.find_all("article", {"class":"recipe-content-card"}):
			url = base + y.find("a", {"class":"view-complete-item"})["href"]
			cur = mysql.connection.cursor()
			cur.execute("SELECT * FROM soups WHERE url = %s", [url])
			if cur.rowcount > 0:
				continue
			cur.close()

			page = requests.get(base + y.find("a", {"class":"view-complete-item"})["href"]).content
			soup = BeautifulSoup(page, "html.parser")

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

			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO soups (SoupName, Ingredients, Directions, image, url) VALUES (%s, %s, %s, %s, %s)", [spname, ingred, steps, secid, url])
			mysql.connection.commit()
			cur.close()

	return redirect(url_for('homepage'))
