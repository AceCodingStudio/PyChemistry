import json

f = open("data/elements.json")
data = json.load(f)


class Chem:
    def __init__(self, element):
        self.element = element

    def getAtomicNumber(self):
        for i in data:
            if self.element in i["name"]:
                an = i["atomicNumber"]
                return an

    def getAtomicMass(self):
        for i in data:
            if self.element in i["name"]:
                an = i["atomicMass"]
                return an

    def getAtomicRadius(self):
        for i in data:
            if self.element in i["name"]:
                an = i["atomicRadius"]
                return an

    def getStandardState(self):
        for i in data:
            if self.element in i["name"]:
                an = i["standardState"]
                return an

    def getBondingType(self):
        for i in data:
            if self.element in i["name"]:
                an = i["bondingType"]
                return an

    def getMeltingPoint(self):
        for i in data:
            if self.element in i["name"]:
                an = i["meltingPoint"]
                return an

    def getBoilingPoint(self):
        for i in data:
            if self.element in i["name"]:
                an = i["boilingPoint"]
                return an

    def getYearDiscovered(self):
        for i in data:
            if self.element in i["name"]:
                an = i["yearDiscovered"]
                return an



