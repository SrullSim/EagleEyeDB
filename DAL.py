import mysql.connector

insert_query = ("INSERT INTO agents (name, codeName, location, status, missionsCompleted)"
                     "VALUES(%s, %s, %s, %s, %s)")

select_all_query = "SELECT * FROM agents"


class Dal:

    def __init__(self):
        pass


    def add_agent_to_db(self, agent):

        agent_tup = agent.get_tup_agent()

        try:
            db = mysql.connector.connect(host="localhost",
                                         user="root",
                                         port="3306",
                                         database="agents")
            agents = db.cursor()
            agents.execute(insert_query,agent_tup)
            db.commit()

        except Exception as ex:
            print("failed to connect -", ex)


    def get_all_agents(self):

        try:
            db = mysql.connector.connect(host="localhost",
                                         user="root",
                                         port="3306",
                                         database="agents")
            all = db.cursor()

            all.execute(select_all_query)

            result = all.fetchall()

            for row in result:
                print(row)

        except Exception as ex:
            print("error to get all. error: ", ex)








