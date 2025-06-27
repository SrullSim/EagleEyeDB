from DAL import  Dal
import  agent
from agent import Agent

a = Agent("avi", "NY")
d = Dal()

d.add_agent_to_db(a)
d.get_all_agents()