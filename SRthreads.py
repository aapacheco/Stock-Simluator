"""
 Developer: Anthony Pacheco
"""
import os
import csv
import queue
import threading
import StockRecord as SR

###############################################################

# Global Variables
stocks_rows = queue.Queue()
stocks_records = queue.Queue()

class Runnable:

    # Defining the function performed by each thread
    def __call__(self):

        print("{worker_id} working hard!! \n".format(worker_id=id(self)))
        while True:

            try:
                row = stocks_rows.get(timeout=1)


                if row["net_income"] == None:
                    raise SR.BadDataError
                else:
                    stocks_records.put(SR.StockRecord(row["ticker"],row["exchange_country"], row["company_name"],float(row["price"]),
                                                      float(row["exchange_rate"]),float(row["shares_outstanding"]), float(row["net_income"])))
            except queue.Empty:
                break
            except (ValueError,SR.BadDataError):
                pass

###############################################################

class FastStocksCSVReader():

    def __init__(self,filepath):
        self.filepath = filepath


    def load(self):

        # Creating Local Variables
        threads = []
        new_list = []

        with open(self.filepath, "r") as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                stocks_rows.put(row)


        # Creating the 4 threads
        for index in range(4):
            new_thread = threading.Thread(target=Runnable())
            new_thread.start()
            threads.append(new_thread)

        for thread in threads:
            thread.join()

        # Populating the new_list to be returned
        while not stocks_records.empty():
            item = stocks_records.get()
            new_list.append(item)

        return new_list

###############################################################

if __name__ == '__main__':
    fastcsv  = FastStocksCSVReader("StockValuations.csv")
    _list = fastcsv.load()
    for i in _list:
        print(i)

# Never Stop Learning
