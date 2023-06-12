from bs4 import BeautifulSoup
import requests
article_tags = []
article_links = []
points = []
response = requests.get("https://news.ycombinator.com/")
hacker_news_html = response.text
soup = BeautifulSoup(hacker_news_html, "html.parser")

span_tags_titles = soup.find_all(name="span", class_="titleline")
for each_span in span_tags_titles:
    article_tags.append(each_span.find('a').text)
    article_links.append(each_span.find('a').get('href'))

span_tags_points = soup.find_all(name="span", class_="score")
for each_span in span_tags_points:
    points.append(int(each_span.text.split()[0]))

article_details = {}
for i, v in enumerate(points):
    article_details[i] = [v, article_tags[i], article_links[i]]

points.sort(reverse=True)
points = points[0:10]
for key, value in article_details.items():
    if article_details[key][0] in points:
        print(f"News: {article_details[key][1]}.\nLink: {article_details[key][2]}.\nVotes: {article_details[key][0]}\n\n")
