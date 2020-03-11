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
                perlisisms.append(s)

    return perlisisms

def getRandom(perlisisms):
    random_perlisism = perlisisms[random.randint(0,len(perlisisms))]
    return random_perlisism

def send(url, data):
    data = "Here is your daily programming wisdom:\n\'" + data + "\' _- Alan Perlis_"

    # wrap neatly in json
    json_payload ="{ \"text\": \"" + data + "\" }"

    # send to mattermost
    response = requests.post(url, json_payload)
    
    if not response.status_code == 200:
        print("could not post to", url)
        print("Error code", response.status_code)
    else:
        print("Successfully posted to ", url, response.status_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send a random perlisism to given webhook (e.g. mattermost)')
    parser.add_argument('webhook', type=str, help="webhook url to send a perlisism to")
    args = parser.parse_args()

    webhook_url = args.webhook

    all_perlisisms = getAll()
    perlisism_of_the_day = getRandom(all_perlisisms)

    send(webhook_url, perlisism_of_the_day)