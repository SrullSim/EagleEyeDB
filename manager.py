import agent
import DAL
from agent import Agent

class Manager:

    def __init__(self):
        self.agent = None
        self.dal = DAL.Dal()
        self.run = True

    def run_all(self):

        while self.run:

            choice = self.entry_print()

            if choice == "1":
                # get agent details
                self.agent = Agent(self.set_name(),self.set_location())
                # add agent to DB
                self.dal.add_agent_to_db(self.agent)

            if choice == "2":
                self.dal.get_all_agents()

            if choice == "3":
                self.dal.get_agent_by_name(self.set_name())

            if choice == "4":
                name = input("enter name of agent")
                column= input("what column you want to update - ")
                val = input("enter value to insert")
                self.dal.update_agent(column, val, name)

            if choice == "5":

                name = input("enter name of agent")
                self.dal.delete_agent(self.set_name())

            if choice == "6":
                self.run = not (self.run)






    def set_name(self):
        name = input("enter name")
        return name

    def set_location(self):
        loc = input("enter location")
        return loc

    def entry_print(self):
        print("======= agent manager =======")
        print("1. add agent ")
        print("2. display all agents")
        print("3. get agent by name")
        print("4. update agent")
        print("5. delete agent by name ")
        print("6. exit")
        choice = input("your choice - ")
        return choice