import pandas as pd
from time import gmtime, strftime
import datetime as dt
import pdb
class Question:
    def __init__(self,desc,company=None,link=None,type=None):
        self.desc = desc
        self.company = company
        self.link = link
        self.type = type
        self.id = hash(self.link)
        
    def upload(self):
        pass


class User:
    
    def __init__(self,username):
        self.username = username


class ProblemSolve:
    
    def __init__(self,username,problem):
        self.username = username
        self.problem = problem
                        
    def start_solve(self):
        FMT = "%Y-%m-%d %H:%M:%S"
        self.starttime = strftime(FMT, gmtime())
        
    def done_solve(self):
        FMT = "%Y-%m-%d %H:%M:%S"
        self.endtime = strftime(FMT, gmtime())
        spend = dt.datetime.strptime(self.endtime, FMT) - dt.datetime.strptime(self.starttime, FMT)
        self.spendtime = "{} mins".format(spend.seconds/60)
        self.upload()
            
    def upload(self):
        pass 
            
                            
                            
            
        
  