html_doc = open("/Users/miabonanno/Desktop/project2/opinion.html", "r")
def grab_html():
    chicken_soup = BeautifulSoup(html_doc, "html.parser")
        cs_as = chicken_soup.find_all("a")
    print(cs_as)

grab_html()



>>> import requests
>>> r = requests.get("http://www.michigandaily.com/section/opinion")
>>> r
<Response [200]>
>>> r.text
'<!DOCTYPE ht

r = requests.get("http://www.michigandaily.com/section/opinion")
soup = BeautifulSoup(r.text, "html.parser")
soup.find("div", {"class": "view-most-read"})

div_containing_answer = soup.find("div", {"class": "view-most-read"}).findChildren("a")

[<a href="/section/government/students-attempt-shut-down-speech-controversial-social-scientist-charles-murray">Students attempt to shut down speech by controversial social scientist Charles Murray </a>, <a href="/section/football/michigan-football-john-okorn-jim-harbaugh-brandon-peters">Orion Sang: Michigan should see what it has with Peters</a>, <a href="/section/campus-life/protestors-grapple-charles-murrays-appearance-campus">Protesters grapple with Charles Murray's appearance on campus</a>, <a href="/section/arts/lil-pump-delivers-hype-despite-substantive-lack">'Lil Pump' delivers hype despite a lack of substance</a>, <a href="/section/tvnew-media/jane-virgin-season-four-review-0">'Jane the Virgin' becomes Adam the Virgo in season 4 shift</a>]
