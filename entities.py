from util import *


class Entity:
    def getProps(self):
        return [sentenceCase(k.split('__')[-1]) for k in vars(self).keys()][::-1]

    def __init__(self, row, header):
        className = self.__class__.__name__
        for i, h in enumerate(header):
            self.__setattr__(f'_{className}__{camelCase(h)}', row[i])

    def __iter__(self):
        return iter(list(vars(self).values())[::-1])

    def __repr__(self):
        s = ''
        for k, v in vars(self).items():
            s += f"{sentenceCase(k.split('__')[-1])}: {v}\n"
        return s + '\n'

class FightCard(Entity):
    def __init__(self, *args):
        if not len(args):
            self.__location = None
            self.__link = None
            self.__date = None
            self.__title = None
        else:
            super().__init__(*args)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        self.__link = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        self.__location = value

class Fight(Entity):
    def __init__(self, *args):
        if not len(args):
            self.__f2Link = None
            self.__f1Link = None
            self.__cardLink = None
            self.__link = None
            self.__titleMatch = False
            self.__koBonus = False
            self.__subBonus = False
            self.__perfBonus = False
            self.__fightBonus = False
            self.__finishTime = None
            self.__finishRound = None
            self.__finishAttack = None
            self.__finishType = None
            self.__weightClass = None
            self.__f2Sub = None
            self.__f1Sub = None
            self.__f2Td = None
            self.__f1Td = None
            self.__f1Str = None
            self.__f2Str = None
            self.__f2Kd = None
            self.__f1Kd = None
            self.__fighter2 = None
            self.__fighter1 = None
        else:
            super().__init__(*args)

    @property
    def fighter1(self):
        return self.__fighter1

    @fighter1.setter
    def fighter1(self, value):
        self.__fighter1 = value

    @property
    def fighter2(self):
        return self.__fighter2

    @fighter2.setter
    def fighter2(self, value):
        self.__fighter2 = value

    @property
    def f1Kd(self):
        return self.__f1Kd

    @f1Kd.setter
    def f1Kd(self, value):
        self.__f1Kd = value

    @property
    def f2Kd(self):
        return self.__f2Kd

    @f2Kd.setter
    def f2Kd(self, value):
        self.__f2Kd = value

    @property
    def f1Str(self):
        return self.__f1Str

    @f1Str.setter
    def f1Str(self, value):
        self.__f1Str = value

    @property
    def f2Str(self):
        return self.__f2Str

    @f2Str.setter
    def f2Str(self, value):
        self.__f2Str = value

    @property
    def f1Td(self):
        return self.__f1Td

    @f1Td.setter
    def f1Td(self, value):
        self.__f1Td = value

    @property
    def f2Td(self):
        return self.__f2Td

    @f2Td.setter
    def f2Td(self, value):
        self.__f2Td = value

    @property
    def f1Sub(self):
        return self.__f1Sub

    @f1Sub.setter
    def f1Sub(self, value):
        self.__f1Sub = value

    @property
    def f2Sub(self):
        return self.__f2Sub

    @f2Sub.setter
    def f2Sub(self, value):
        self.__f2Sub = value

    @property
    def weightClass(self):
        return self.__weightClass

    @weightClass.setter
    def weightClass(self, value):
        self.__weightClass = value

    @property
    def finishType(self):
        return self.__finishType

    @finishType.setter
    def finishType(self, value):
        self.__finishType = value

    @property
    def finishAttack(self):
        return self.__finishAttack

    @finishAttack.setter
    def finishAttack(self, value):
        self.__finishAttack = value

    @property
    def finishRound(self):
        return self.__finishRound

    @finishRound.setter
    def finishRound(self, value):
        self.__finishRound = value

    @property
    def finishTime(self):
        return self.__finishTime

    @finishTime.setter
    def finishTime(self, value):
        self.__finishTime = value

    @property
    def fightBonus(self):
        return self.__fightBonus

    @fightBonus.setter
    def fightBonus(self, value):
        self.__fightBonus = value

    @property
    def perfBonus(self):
        return self.__perfBonus

    @perfBonus.setter
    def perfBonus(self, value):
        self.__perfBonus = value

    @property
    def subBonus(self):
        return self.__subBonus

    @subBonus.setter
    def subBonus(self, value):
        self.__subBonus = value

    @property
    def koBonus(self):
        return self.__koBonus

    @koBonus.setter
    def koBonus(self, value):
        self.__koBonus = value

    @property
    def titleMatch(self):
        return self.__titleMatch

    @titleMatch.setter
    def titleMatch(self, value):
        self.__titleMatch = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        self.__link = value

    @property
    def cardLink(self):
        return self.__cardLink

    @cardLink.setter
    def cardLink(self, value):
        self.__cardLink = value

    @property
    def f1Link(self):
        return self.__f1Link

    @f1Link.setter
    def f1Link(self, value):
        self.__f1Link = value

    @property
    def f2Link(self):
        return self.__f2Link

    @f2Link.setter
    def f2Link(self, value):
        self.__f2Link = value

class FightDetail(Entity):
    def __init__(self, *args):
        if not len(args):
            self.__timeFormat = None
            self.__referee = None
            self.__finishDetails = None
            self.__fightLink = None

            self.__f1Knockdowns = None
            self.__f1SigStrikes = None
            self.__f1SigStrikePerc = None
            self.__f1TotalStrikes = None
            self.__f1Takedowns = None
            self.__f1TakedownPerc = None
            self.__f1SubAttacks = None
            self.__f1Reversals = None
            self.__f1ControlTime = None
            self.__f2Knockdowns = None
            self.__f2SigStrikes = None
            self.__f2SigStrikePerc = None
            self.__f2TotalStrikes = None
            self.__f2Takedowns = None
            self.__f2TakedownPerc = None
            self.__f2SubAttacks = None
            self.__f2Reversals = None
            self.__f2ControlTime = None

            self.__f1Head = None
            self.__f1Body = None
            self.__f1Leg = None
            self.__f1Distance = None
            self.__f1Clinch = None
            self.__f1Ground = None
            self.__f2Head = None
            self.__f2Body = None
            self.__f2Leg = None
            self.__f2Distance = None
            self.__f2Clinch = None
            self.__f2Ground = None
        else:
            super().__init__(*args)

    @property
    def timeFormat(self):
        return self.__timeFormat

    @timeFormat.setter
    def timeFormat(self, value):
        self.__timeFormat = value

    @property
    def referee(self):
        return self.__referee

    @referee.setter
    def referee(self, value):
        self.__referee = value

    @property
    def finishDetails(self):
        return self.__finishDetails

    @finishDetails.setter
    def finishDetails(self, value):
        self.__finishDetails = value

    @property
    def fightLink(self):
        return self.__fightLink

    @fightLink.setter
    def fightLink(self, value):
        self.__fightLink = value

    @property
    def f1Knockdowns(self):
        return self.__f1Knockdowns

    @f1Knockdowns.setter
    def f1Knockdowns(self, value):
        self.__f1Knockdowns = value

    @property
    def f1SigStrikes(self):
        return self.__f1SigStrikes

    @f1SigStrikes.setter
    def f1SigStrikes(self, value):
        self.__f1SigStrikes = value

    @property
    def f1SigStrikePerc(self):
        return self.__f1SigStrikePerc

    @f1SigStrikePerc.setter
    def f1SigStrikePerc(self, value):
        self.__f1SigStrikePerc = value

    @property
    def f1TotalStrikes(self):
        return self.__f1TotalStrikes

    @f1TotalStrikes.setter
    def f1TotalStrikes(self, value):
        self.__f1TotalStrikes = value

    @property
    def f1Takedowns(self):
        return self.__f1Takedowns

    @f1Takedowns.setter
    def f1Takedowns(self, value):
        self.__f1Takedowns = value

    @property
    def f1TakedownPerc(self):
        return self.__f1TakedownPerc

    @f1TakedownPerc.setter
    def f1TakedownPerc(self, value):
        self.__f1TakedownPerc = value

    @property
    def f1SubAttacks(self):
        return self.__f1SubAttacks

    @f1SubAttacks.setter
    def f1SubAttacks(self, value):
        self.__f1SubAttacks = value

    @property
    def f1Reversals(self):
        return self.__f1Reversals

    @f1Reversals.setter
    def f1Reversals(self, value):
        self.__f1Reversals = value

    @property
    def f1ControlTime(self):
        return self.__f1ControlTime

    @f1ControlTime.setter
    def f1ControlTime(self, value):
        self.__f1ControlTime = value

    @property
    def f2Knockdowns(self):
        return self.__f2Knockdowns

    @f2Knockdowns.setter
    def f2Knockdowns(self, value):
        self.__f2Knockdowns = value

    @property
    def f2SigStrikes(self):
        return self.__f2SigStrikes

    @f2SigStrikes.setter
    def f2SigStrikes(self, value):
        self.__f2SigStrikes = value

    @property
    def f2SigStrikePerc(self):
        return self.__f2SigStrikePerc

    @f2SigStrikePerc.setter
    def f2SigStrikePerc(self, value):
        self.__f2SigStrikePerc = value

    @property
    def f2TotalStrikes(self):
        return self.__f2TotalStrikes

    @f2TotalStrikes.setter
    def f2TotalStrikes(self, value):
        self.__f2TotalStrikes = value

    @property
    def f2Takedowns(self):
        return self.__f2Takedowns

    @f2Takedowns.setter
    def f2Takedowns(self, value):
        self.__f2Takedowns = value

    @property
    def f2TakedownPerc(self):
        return self.__f2TakedownPerc

    @f2TakedownPerc.setter
    def f2TakedownPerc(self, value):
        self.__f2TakedownPerc = value

    @property
    def f2SubAttacks(self):
        return self.__f2SubAttacks

    @f2SubAttacks.setter
    def f2SubAttacks(self, value):
        self.__f2SubAttacks = value

    @property
    def f2Reversals(self):
        return self.__f2Reversals

    @f2Reversals.setter
    def f2Reversals(self, value):
        self.__f2Reversals = value

    @property
    def f2ControlTime(self):
        return self.__f2ControlTime

    @f2ControlTime.setter
    def f2ControlTime(self, value):
        self.__f2ControlTime = value

    @property
    def f1Head(self):
        return self.__f1Head

    @f1Head.setter
    def f1Head(self, value):
        self.__f1Head = value

    @property
    def f1Body(self):
        return self.__f1Body

    @f1Body.setter
    def f1Body(self, value):
        self.__f1Body = value

    @property
    def f1Leg(self):
        return self.__f1Leg

    @f1Leg.setter
    def f1Leg(self, value):
        self.__f1Leg = value

    @property
    def f1Distance(self):
        return self.__f1Distance

    @f1Distance.setter
    def f1Distance(self, value):
        self.__f1Distance = value

    @property
    def f1Clinch(self):
        return self.__f1Clinch

    @f1Clinch.setter
    def f1Clinch(self, value):
        self.__f1Clinch = value

    @property
    def f1Ground(self):
        return self.__f1Ground

    @f1Ground.setter
    def f1Ground(self, value):
        self.__f1Ground = value

    @property
    def f2Head(self):
        return self.__f2Head

    @f2Head.setter
    def f2Head(self, value):
        self.__f2Head = value

    @property
    def f2Body(self):
        return self.__f2Body

    @f2Body.setter
    def f2Body(self, value):
        self.__f2Body = value

    @property
    def f2Leg(self):
        return self.__f2Leg

    @f2Leg.setter
    def f2Leg(self, value):
        self.__f2Leg = value

    @property
    def f2Distance(self):
        return self.__f2Distance

    @f2Distance.setter
    def f2Distance(self, value):
        self.__f2Distance = value

    @property
    def f2Clinch(self):
        return self.__f2Clinch

    @f2Clinch.setter
    def f2Clinch(self, value):
        self.__f2Clinch = value

    @property
    def f2Ground(self):
        return self.__f2Ground

    @f2Ground.setter
    def f2Ground(self, value):
        self.__f2Ground = value

class FightRound(Entity):
    def __init__(self, *args):
        if not len(args):
            self.__fightLink = None
            self.__round = None

            self.__f1Knockdowns = None
            self.__f1SigStrikes = None
            self.__f1SigStrikePerc = None
            self.__f1TotalStrikes = None
            self.__f1Takedowns = None
            self.__f1TakedownPerc = None
            self.__f1SubAttacks = None
            self.__f1Reversals = None
            self.__f1ControlTime = None
            self.__f2Knockdowns = None
            self.__f2SigStrikes = None
            self.__f2SigStrikePerc = None
            self.__f2TotalStrikes = None
            self.__f2Takedowns = None
            self.__f2TakedownPerc = None
            self.__f2SubAttacks = None
            self.__f2Reversals = None
            self.__f2ControlTime = None

            self.__f1Head = None
            self.__f1Body = None
            self.__f1Leg = None
            self.__f1Distance = None
            self.__f1Clinch = None
            self.__f1Ground = None
            self.__f2Head = None
            self.__f2Body = None
            self.__f2Leg = None
            self.__f2Distance = None
            self.__f2Clinch = None
            self.__f2Ground = None
        else:
            super().__init__(*args)

    @property
    def fightLink(self):
        return self.__fightLink

    @fightLink.setter
    def fightLink(self, value):
        self.__fightLink = value

    @property
    def round(self):
        return self.__round

    @round.setter
    def round(self, value):
        self.__round = value

    @property
    def f1Knockdowns(self):
        return self.__f1Knockdowns

    @f1Knockdowns.setter
    def f1Knockdowns(self, value):
        self.__f1Knockdowns = value

    @property
    def f1SigStrikes(self):
        return self.__f1SigStrikes

    @f1SigStrikes.setter
    def f1SigStrikes(self, value):
        self.__f1SigStrikes = value

    @property
    def f1SigStrikePerc(self):
        return self.__f1SigStrikePerc

    @f1SigStrikePerc.setter
    def f1SigStrikePerc(self, value):
        self.__f1SigStrikePerc = value

    @property
    def f1TotalStrikes(self):
        return self.__f1TotalStrikes

    @f1TotalStrikes.setter
    def f1TotalStrikes(self, value):
        self.__f1TotalStrikes = value

    @property
    def f1Takedowns(self):
        return self.__f1Takedowns

    @f1Takedowns.setter
    def f1Takedowns(self, value):
        self.__f1Takedowns = value

    @property
    def f1TakedownPerc(self):
        return self.__f1TakedownPerc

    @f1TakedownPerc.setter
    def f1TakedownPerc(self, value):
        self.__f1TakedownPerc = value

    @property
    def f1SubAttacks(self):
        return self.__f1SubAttacks

    @f1SubAttacks.setter
    def f1SubAttacks(self, value):
        self.__f1SubAttacks = value

    @property
    def f1Reversals(self):
        return self.__f1Reversals

    @f1Reversals.setter
    def f1Reversals(self, value):
        self.__f1Reversals = value

    @property
    def f1ControlTime(self):
        return self.__f1ControlTime

    @f1ControlTime.setter
    def f1ControlTime(self, value):
        self.__f1ControlTime = value

    @property
    def f2Knockdowns(self):
        return self.__f2Knockdowns

    @f2Knockdowns.setter
    def f2Knockdowns(self, value):
        self.__f2Knockdowns = value

    @property
    def f2SigStrikes(self):
        return self.__f2SigStrikes

    @f2SigStrikes.setter
    def f2SigStrikes(self, value):
        self.__f2SigStrikes = value

    @property
    def f2SigStrikePerc(self):
        return self.__f2SigStrikePerc

    @f2SigStrikePerc.setter
    def f2SigStrikePerc(self, value):
        self.__f2SigStrikePerc = value

    @property
    def f2TotalStrikes(self):
        return self.__f2TotalStrikes

    @f2TotalStrikes.setter
    def f2TotalStrikes(self, value):
        self.__f2TotalStrikes = value

    @property
    def f2Takedowns(self):
        return self.__f2Takedowns

    @f2Takedowns.setter
    def f2Takedowns(self, value):
        self.__f2Takedowns = value

    @property
    def f2TakedownPerc(self):
        return self.__f2TakedownPerc

    @f2TakedownPerc.setter
    def f2TakedownPerc(self, value):
        self.__f2TakedownPerc = value

    @property
    def f2SubAttacks(self):
        return self.__f2SubAttacks

    @f2SubAttacks.setter
    def f2SubAttacks(self, value):
        self.__f2SubAttacks = value

    @property
    def f2Reversals(self):
        return self.__f2Reversals

    @f2Reversals.setter
    def f2Reversals(self, value):
        self.__f2Reversals = value

    @property
    def f2ControlTime(self):
        return self.__f2ControlTime

    @f2ControlTime.setter
    def f2ControlTime(self, value):
        self.__f2ControlTime = value

    @property
    def f1Head(self):
        return self.__f1Head

    @f1Head.setter
    def f1Head(self, value):
        self.__f1Head = value

    @property
    def f1Body(self):
        return self.__f1Body

    @f1Body.setter
    def f1Body(self, value):
        self.__f1Body = value

    @property
    def f1Leg(self):
        return self.__f1Leg

    @f1Leg.setter
    def f1Leg(self, value):
        self.__f1Leg = value

    @property
    def f1Distance(self):
        return self.__f1Distance

    @f1Distance.setter
    def f1Distance(self, value):
        self.__f1Distance = value

    @property
    def f1Clinch(self):
        return self.__f1Clinch

    @f1Clinch.setter
    def f1Clinch(self, value):
        self.__f1Clinch = value

    @property
    def f1Ground(self):
        return self.__f1Ground

    @f1Ground.setter
    def f1Ground(self, value):
        self.__f1Ground = value

    @property
    def f2Head(self):
        return self.__f2Head

    @f2Head.setter
    def f2Head(self, value):
        self.__f2Head = value

    @property
    def f2Body(self):
        return self.__f2Body

    @f2Body.setter
    def f2Body(self, value):
        self.__f2Body = value

    @property
    def f2Leg(self):
        return self.__f2Leg

    @f2Leg.setter
    def f2Leg(self, value):
        self.__f2Leg = value

    @property
    def f2Distance(self):
        return self.__f2Distance

    @f2Distance.setter
    def f2Distance(self, value):
        self.__f2Distance = value

    @property
    def f2Clinch(self):
        return self.__f2Clinch

    @f2Clinch.setter
    def f2Clinch(self, value):
        self.__f2Clinch = value

    @property
    def f2Ground(self):
        return self.__f2Ground

    @f2Ground.setter
    def f2Ground(self, value):
        self.__f2Ground = value

class Fighter(Entity):
    def __init__(self, *args):
        if not len(args):
            self.__name = None
            self.__nickName = None
            self.__link = None
            self.__winLossRecord = None
            self.__height = None
            self.__weight = None
            self.__reach = None
            self.__stance = None
            self.__dob = None
            self.__slpm = None
            self.__strikingAcc = None
            self.__sapm = None
            self.__strikingDef = None
            self.__takedownAvg = None
            self.__takedownAcc = None
            self.__takedownDef = None
            self.__subAvg = None
        else:
            super().__init__(*args)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def nickName(self):
        return self.__nickName

    @nickName.setter
    def nickName(self, value):
        self.__nickName = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        self.__link = value

    @property
    def winLossRecord(self):
        return self.__winLossRecord

    @winLossRecord.setter
    def winLossRecord(self, value):
        self.__winLossRecord = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

    @property
    def reach(self):
        return self.__reach

    @reach.setter
    def reach(self, value):
        self.__reach = value

    @property
    def stance(self):
        return self.__stance

    @stance.setter
    def stance(self, value):
        self.__stance = value

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, value):
        self.__dob = value

    @property
    def slpm(self):
        return self.__slpm

    @slpm.setter
    def slpm(self, value):
        self.__slpm = value

    @property
    def strikingAcc(self):
        return self.__strikingAcc

    @strikingAcc.setter
    def strikingAcc(self, value):
        self.__strikingAcc = value

    @property
    def sapm(self):
        return self.__sapm

    @sapm.setter
    def sapm(self, value):
        self.__sapm = value

    @property
    def strikingDef(self):
        return self.__strikingDef

    @strikingDef.setter
    def strikingDef(self, value):
        self.__strikingDef = value

    @property
    def takedownAvg(self):
        return self.__takedownAvg

    @takedownAvg.setter
    def takedownAvg(self, value):
        self.__takedownAvg = value

    @property
    def takedownAcc(self):
        return self.__takedownAcc

    @takedownAcc.setter
    def takedownAcc(self, value):
        self.__takedownAcc = value

    @property
    def takedownDef(self):
        return self.__takedownDef

    @takedownDef.setter
    def takedownDef(self, value):
        self.__takedownDef = value

    @property
    def subAvg(self):
        return self.__subAvg

    @subAvg.setter
    def subAvg(self, value):
        self.__subAvg = value
