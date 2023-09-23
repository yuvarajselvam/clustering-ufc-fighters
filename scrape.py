import csv
import requests

from entities import *

from tqdm import tqdm
from bs4 import BeautifulSoup


def scrapeFightCards():
    FILE_NAME = 'fight_cards'

    URL = 'http://ufcstats.com/statistics/events/completed?page=all'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.findAll('tr', {'class': 'b-statistics__table-row'})

    with open(f"{FILE_NAME}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(FightCard().getProps())
        for row in tqdm(rows, desc='Fight Cards'):
            cols = row.findAll('td', {'class': 'b-statistics__table-col'})
            if not cols:
                continue

            card = FightCard()
            fightCol, locCol = cols

            card.title = fightCol.find('a').text.strip()
            card.link = fightCol.find('a').get('href')
            card.date = fightCol.find('span').text.strip()
            card.location = locCol.text.strip()

            writer.writerow(card)

def scrapeFights():
    cards, header = [], None
    with open('fight_cards.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if not header:
                header = row
            else:
                cards += [FightCard(row, header)]

    FILE_NAME = 'fights'
    with open(f"{FILE_NAME}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(Fight().getProps())
        for card in tqdm(cards, desc='Fights'):
            page = requests.get(card.link)
            soup = BeautifulSoup(page.text, 'html.parser')

            table = soup.find('tbody')
            rows = table.findAll('tr')
            for row in rows:
                fight = Fight()

                fightersCol = row.findAll('a', href=lambda x: x and 'fighter-details' in x)
                f1, f2 = fightersCol

                imageCols = row.findAll('img')

                remCols = row.select('p:not(:has(a))')
                remCols = [x.text.strip() for x in remCols]

                fight.cardLink = card.link
                fight.link = row.get('data-link')
                fight.fighter1 = f1.text.strip()
                fight.fighter2 = f2.text.strip()
                fight.f1Link = f1.get('href')
                fight.f2Link = f2.get('href')
                fight.f1Kd, \
                    fight.f2Kd, \
                    fight.f1Str, \
                    fight.f2Str, \
                    fight.f1Td, \
                    fight.f2Td, \
                    fight.f1Sub, \
                    fight.f2Sub, \
                    fight.weightClass, \
                    fight.finishType, \
                    fight.finishAttack, \
                    fight.finishRound, \
                    fight.finishTime = remCols

                for image in imageCols:
                    imageType = image.get('src').split('/')[-1].split('.')[0]

                    if imageType == 'perf':
                        fight.perfBonus = True
                    elif imageType == 'belt':
                        fight.titleMatch = True
                    elif imageType == 'ko':
                        fight.koBonus = True
                    elif imageType == 'sub':
                        fight.subBonus = True
                    elif imageType == 'fight':
                        fight.fightBonus = True

                writer.writerow(fight)

def scrapeFightRounds():
    fights, header = [], None
    with open('fights.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if not header:
                header = row
            else:
                fights += [Fight(row, header)]

    FILE_NAME_1 = 'fight_details'
    FILE_NAME_2 = 'fight_rounds'
    with open(f"{FILE_NAME_1}.csv", "w") as f1, \
            open(f"{FILE_NAME_2}.csv", "w") as f2:
        writer1, writer2 = csv.writer(f1), csv.writer(f2)
        writer1.writerow(FightDetail().getProps())
        writer2.writerow(FightRound().getProps())
        for fight in tqdm(fights, desc='Fight Rounds'):
            page = requests.get(fight.link)
            soup = BeautifulSoup(page.text, 'html.parser')

            fightDetailsDiv = soup.find('div', {'class': 'b-fight-details__content'})
            details = [x.strip() for x in fightDetailsDiv.text.split('\n') if x.strip()]
            tables = soup.findAll('table')

            fightDetail = FightDetail()
            fightDetail.fightLink = fight.link
            fightDetail.timeFormat = details[7]
            fightDetail.referee = details[9]
            fightDetail.finishDetails = details[11] if len(details) > 11 else None

            if not tables:
                continue

            totDetails = [x.strip() for x in tables[0].text.split('\n') if x.strip()][10:]
            _, \
                fightDetail.f1Knockdowns, \
                fightDetail.f1SigStrikes, \
                fightDetail.f1SigStrikePerc, \
                fightDetail.f1TotalStrikes, \
                fightDetail.f1Takedowns, \
                fightDetail.f1TakedownPerc, \
                fightDetail.f1SubAttacks, \
                fightDetail.f1Reversals, \
                fightDetail.f1ControlTime = totDetails[(0 if totDetails[0] == fight.fighter1 else 1)::2]

            _, \
                fightDetail.f2Knockdowns, \
                fightDetail.f2SigStrikes, \
                fightDetail.f2SigStrikePerc, \
                fightDetail.f2TotalStrikes, \
                fightDetail.f2Takedowns, \
                fightDetail.f2TakedownPerc, \
                fightDetail.f2SubAttacks, \
                fightDetail.f2Reversals, \
                fightDetail.f2ControlTime = totDetails[(0 if totDetails[0] == fight.fighter2 else 1)::2]

            sigDetails = [x.strip() for x in tables[2].text.split('\n') if x.strip()][9:]
            _, _, _, \
                fightDetail.f1Head, \
                fightDetail.f1Body, \
                fightDetail.f1Leg, \
                fightDetail.f1Distance, \
                fightDetail.f1Clinch, \
                fightDetail.f1Ground = sigDetails[(0 if sigDetails[0] == fight.fighter1 else 1)::2]

            _, _, _, \
                fightDetail.f2Head, \
                fightDetail.f2Body, \
                fightDetail.f2Leg, \
                fightDetail.f2Distance, \
                fightDetail.f2Clinch, \
                fightDetail.f2Ground = sigDetails[(0 if sigDetails[0] == fight.fighter2 else 1)::2]

            roundTotDetails = [x.strip() for x in tables[1].text.split('\n') if x.strip()][10:]
            roundSigDetails = [x.strip() for x in tables[3].text.split('\n') if x.strip()][9:]

            rnd = 1
            while True:
                fightRnd = FightRound()
                fightRnd.fightLink = fight.link
                fightRnd.round = rnd

                currRndTotDetails = roundTotDetails[((rnd - 1) * 21):][1:21]
                currRndSigDetails = roundSigDetails[((rnd - 1) * 19):][1:19]

                if not currRndTotDetails:
                    break

                _, \
                    fightRnd.f1Knockdowns, \
                    fightRnd.f1SigStrikes, \
                    fightRnd.f1SigStrikePerc, \
                    fightRnd.f1TotalStrikes, \
                    fightRnd.f1Takedowns, \
                    fightRnd.f1TakedownPerc, \
                    fightRnd.f1SubAttacks, \
                    fightRnd.f1Reversals, \
                    fightRnd.f1ControlTime = currRndTotDetails[(0 if currRndTotDetails[0] == fight.fighter1 else 1)::2]

                _, \
                    fightRnd.f2Knockdowns, \
                    fightRnd.f2SigStrikes, \
                    fightRnd.f2SigStrikePerc, \
                    fightRnd.f2TotalStrikes, \
                    fightRnd.f2Takedowns, \
                    fightRnd.f2TakedownPerc, \
                    fightRnd.f2SubAttacks, \
                    fightRnd.f2Reversals, \
                    fightRnd.f2ControlTime = currRndTotDetails[(0 if currRndTotDetails[0] == fight.fighter2 else 1)::2]

                _, _, _, \
                    fightRnd.f1Head, \
                    fightRnd.f1Body, \
                    fightRnd.f1Leg, \
                    fightRnd.f1Distance, \
                    fightRnd.f1Clinch, \
                    fightRnd.f1Ground = currRndSigDetails[(0 if currRndSigDetails[0] == fight.fighter1 else 1)::2]

                _, _, _, \
                    fightRnd.f2Head, \
                    fightRnd.f2Body, \
                    fightRnd.f2Leg, \
                    fightRnd.f2Distance, \
                    fightRnd.f2Clinch, \
                    fightRnd.f2Ground = currRndSigDetails[(0 if currRndSigDetails[0] == fight.fighter2 else 1)::2]

                rnd += 1
                writer2.writerow(fightRnd)

            writer1.writerow(fightDetail)

def scrapeFighters():
    FILE_NAME = 'fighters'

    URL = f'http://ufcstats.com/statistics/fighters?char=*&page=all'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.findAll('tr', {'class': 'b-statistics__table-row'})

    links = [row.find('a').get('href') for row in rows if row.find('a')]
    with open(f"{FILE_NAME}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(Fighter().getProps())
        for fighterLink in tqdm(links, desc='Fighters'):
            page = requests.get(fighterLink)
            soup = BeautifulSoup(page.text, 'html.parser')

            fighter = Fighter()
            boxes = soup.findAll('div', {'class': 'b-list__info-box'})

            fighter.name = soup.find('span', {'class': 'b-content__title-highlight'}).text.strip()
            fighter.nickName = soup.find('p', {'class': 'b-content__Nickname'}).text.strip()
            fighter.winLossRecord = soup.find('span', {'class': 'b-content__title-record'}).text.strip()
            fighter.link = fighterLink

            fighter.height, \
                fighter.weight, \
                fighter.reach, \
                fighter.stance, \
                fighter.dob = [i.next_sibling.strip() for i in boxes[0].select('li > i')]

            fighter.slpm, \
                fighter.strikingAcc, \
                fighter.sapm, \
                fighter.strikingDef, \
                _, \
                fighter.takedownAvg, \
                fighter.takedownAcc, \
                fighter.takedownDef, \
                fighter.subAvg = [i.next_sibling.strip() for i in boxes[1].select('li > i')]

            writer.writerow(fighter)


scrapeFightCards()
scrapeFights()
scrapeFightRounds()
scrapeFighters()
