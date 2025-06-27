from DAL import  Dal
import  agent
from agent import Agent

a = Agent("ben", "NY")
d = Dal()

# d.add_agent_to_db(a)
d.delete_agent("avi")