# from argparse import ArgumentParser
import time
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
games_set = set()


def main():
    # Create a Scraper client
    sc = Scraper(headers)

    with open('games.txt', 'w') as f:
        for i in range(100):
            print(f"Processing page {i + 1}")
            # Make a soup for the the site with thw list of games
            soup = sc.make_soup(f"{entry_point}page/{i + 1}")
            # Take a the game links
            games = sc.find_elems(soup, ".blog-content h2 a")

            for game in games:
                # Make soup for game site
                soup = sc.make_soup(game['href'])
                try:
                    # Get the game title
                    game_title = sc.find_elems(
                        soup, ".game-info ul li:nth-child(1)"
                    )[0].text.split(':')[-1].strip()

                    # Check if the game is in the games set and if true
                    # continue to the next game else insert tha game in
                    # games and write it in the file
                    if str(game_title) in games_set:
                        continue
                    else:
                        games_set.add(str(game_title))

                    # Get the game genre
                    game_genre = sc.find_elems(
                        soup, ".game-info ul li:nth-child(4)"
                    )[0].text.split(':')[1].strip()
                    # If the game belongs to many genres join them together
                    game_genre = str(game_genre).replace(',', '')

                    # Write the game infos in a file
                    f.write(
                        f"{game_title},{game_genre},"
                        + f"{game['href']}\n"
                    )
                except Exception as e:
                    print(f"Error: {e}\n")
                    print("Continuing to next game...\n")

            # Wait for seconds to not get blacklisted from the site
            time.sleep(2)


if __name__ == "__main__":
    main()
