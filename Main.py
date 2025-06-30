from DAL import Dal, update_agent_query
import  agent
from agent import Agent, Status
import  manager




class Main:

    def __init__(self):
        self.manager = manager.Manager()

    def run(self):
        self.manager.run_all()


run = Main()
run.run()