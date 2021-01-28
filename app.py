# from argparse import ArgumentParser
from scraper import Scraper

# # Create the required arguments to running the program
# arg_parser = ArgumentParser()
# arg_parser.add_argument("--page", "-p", type=str, required=True)
# args = arg_parser.parse_args()


# Initiliaze variables
entry_point = "https://www.skidrowcodex.net/"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 84.0)'
    + ' Gecko/20100101 Firefox/84.0'
}


def main():
    sc = Scraper(headers)
    soup = sc.make_soup(entry_point)
    games = sc.find_elems(soup, ".blog-content h2 a")

    with open('games.txt', 'w') as f:
        for game in games:
            soup = sc.make_soup(game['href'])
            game_title = sc.find_elems(
                soup, ".game-info ul li:nth-child(1)"
            )[0].text.split(':')[1].strip()
            game_genre = sc.find_elems(
                soup, ".game-info ul li:nth-child(4)"
            )[0].text.split(':')[1].strip()

            f.write(
                f"Title:{game_title},Genre:{game_genre},"
                + f"Adress: {game['href']}\n"
            )


if __name__ == "__main__":
    main()
