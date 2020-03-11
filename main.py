from bs4 import BeautifulSoup
import random
import requests
import argparse

def getAll():
    perlisisms = []

    with open("perlisisms.html") as fp:
        soup = BeautifulSoup(fp, features="html.parser")
        ps = soup.find_all("p")
        for p in ps:
            for s in p.stripped_strings:
                # print(s)
                perlisisms.append(s)

    return perlisisms

def getRandom(perlisisms):
    random_perlisism = perlisisms[random.randint(0,len(perlisisms))]

    print(random_perlisism)
    return random_perlisism

def send(url, data):
    # send to mattermost
    requests.post(url, data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a random perlisism to given webhook (e.g. mattermost)')
    parser.add_argument('--webhook', type=str, help="webhook url to send a perlisism to")
    args = parser.parse_args()

    webhook_url = args.webhook

    all_perlisisms = getAll()
    perlisism_of_the_day = getRandom(all_perlisisms)

    send(webhook_url, perlisism_of_the_day)