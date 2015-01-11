import pandas as pd
from time import gmtime, strftime
import datetime as dt
class Interview_question:
    def __init__(self,filename,company,link,type):
        self.filename = filename
        self.company = company
        self.link = link
        self.type = type
        self.starttime = None
        self.endtime = None
        self.spendtime = None
        
    def setTime(self):
        FMT = "%Y-%m-%d %H:%M:%S"
        if self.starttime is None:
            self.starttime = strftime(FMT, gmtime())
        elif self.endtime is None:
            self.endtime = strftime(FMT, gmtime())
            spend = dt.datetime.strptime(self.endtime, FMT) - dt.datetime.strptime(self.starttime, FMT)
            self.spend = spend.seconds/60
            
    def to_csv(self):
        f = pd.read_csv("Interview_questions.csv")
        
    


x = Interview_question("insert_in_ordered_circular_linkedlist.py","Walmartlab", "http://www.careercup.com/question?id=13273690","Linkedlist")