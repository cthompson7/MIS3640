import csv
import urllib.request
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'http://www.imdb.com/chart/top'


def download_page(url):

    return urllib.request.urlopen(url)

# print(download_page(DOWNLOAD_URL).read())


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    movie_table = soup.find('tbody', attrs={'class': 'lister-list'})
    movie_list = []
    for movie_row in movie_table.find_all('tr'):
        movie_detail = movie_row.find('td', attrs={'class': 'titleColumn'})
        movie_name = movie_detail.find('a').string
        movie_rating = movie_row.find('td', attrs={'class': 'ratingColumn imdbRating'})
        ratings = movie_rating.find('strong').string
        # print(movie_name)
        year = movie_detail.find(
            'span', attrs={'class': 'secondaryInfo'}).string.strip('()')
        # print(year)
        movie_list.append((movie_name,' ' + year,' ' + ratings))
    return movie_list


def main():
    url = DOWNLOAD_URL

    with open('imdb_top250.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        fields = ('name', 'year')
        writer.writerow(fields)

        html = download_page(url)
        movies = parse_html(html)
        writer.writerows(movies)


if __name__ == '__main__':
    main()
