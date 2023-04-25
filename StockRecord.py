"""
 Developer: Anthony Pacheco
"""
import csv
import os

###############################################################


class AbstractClass:
    def __init__(self,name):
        self.name = name


###############################################################


class StockRecord(AbstractClass):
    def __init__(self,ticker,exchange_country,company_name,price,exchange_rate,shares_outstanding,net_income):
        super().__init__(ticker)
        self.exchange_country = exchange_country
        self.company_name = company_name
        self.price = price
        self.exchange_rate = exchange_rate
        self.shares_outstanding = shares_outstanding
        self.net_income = net_income
        self.peratio = (price / net_income)
        self.marketval = (price * exchange_rate * shares_outstanding)

    def __str__(self):
        newstr = "StockStatRecord({}, {}, {}, $Price={:.2f}, $Cap={:.2f}, P/E={:.2f})"

        return newstr.format(self.name,self.exchange_country,self.company_name,self.price, self.marketval, self.peratio)


###############################################################


class BaseballRecord(AbstractClass):
    def __init__(self,name,salary,G,AVG):
        super().__init__(name)
        self.salary = salary
        self.G = G
        self.AVG = AVG

    def __str__(self):
        newstr = "BaseballStatRecord({}, {:.2f}, {}, {:.3f})"

        return newstr.format(str(self.name), self.salary, self.G, self.AVG)


###############################################################


class Error(Exception):
    pass


###############################################################


class BadDataError(Error):
    def __init__(self):
        self.message = "There was a problem creating the record."

    def error(self):
        return self.message


###############################################################


class AbstractCSVReader:

    def __init__(self,filename):
        self.filename = filename

    def row_to_record(self,row):
        raise NotImplementedError

    def load(self):
        Approved_Data = []
        with open(self.filename, "r") as csvfile:
            csvreader = csv.DictReader(csvfile)

            for currentrow in csvreader:
                try:
                    new_record = self.row_to_record(currentrow)
                    Approved_Data.append(new_record)
                except BadDataError as bde:
                    #print(bde)
                    continue
            return Approved_Data


###############################################################


class StockCSVReader(AbstractCSVReader):
    stock_columns = (
        "ticker",
        "exchange_country",
        "company_name",
        "price",
        "exchange_rate",
        "shares_outstanding",
        "net_income")

    def __init__(self,filename):
        super().__init__(filename)

    def row_to_record(self,datarow):
        new_record = {}

        # validation fails if any piece of information is missing
        try:
            for col in self.stock_columns:
                new_record[col] = datarow[col]
                if new_record[col] == None:
                    raise BadDataError

                if ((col == "price") or (col == "net_income") or (col == "exchange_rate") or (col == "shares_outstanding")):
                    new_record[col] = float(new_record[col])

            return StockRecord(new_record["ticker"],new_record["exchange_country"], new_record["company_name"],
                               new_record["price"], new_record["exchange_rate"],
                               new_record["shares_outstanding"], new_record["net_income"])
        except (KeyError,BadDataError,ValueError) as e:
            raise BadDataError

        pass


###############################################################


class BaseballCSVReader(AbstractCSVReader):
    baseball_columns = (
        "PLAYER",
        "SALARY",
        "G",
        "AVG")

    def __init__(self,filename):
        super().__init__(filename)

    def row_to_record(self,datarow):
        new_record = {}

        # validation fails if any piece of information is missing
        try:
            for col in self.baseball_columns:
                new_record[col] = datarow[col]
                if new_record[col] == None:
                    raise BadDataError

                if ((col == "SALARY") or (col == "AVG")):
                    new_record[col] = float(new_record[col])
                elif(col == "G"):
                    new_record[col] = int(new_record[col])

            return BaseballRecord(new_record["PLAYER"], new_record["SALARY"],
                           new_record["G"], new_record["AVG"])

        except (KeyError,BadDataError,ValueError) as e:
            raise BadDataError

        pass


###############################################################


### Run the code
if __name__ == '__main__':

    stockcsv = StockCSVReader("StockValuations.csv").load()
    for datarow in stockcsv:
        print(type(datarow.exchange_country))


    baseballcsv = BaseballCSVReader("MLB2008.csv")
    PlayerRecord = baseballcsv.load()
    for player in PlayerRecord:
        print(player)

# Never Stop Learning
