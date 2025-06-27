import mysql.connector


insert_query = ("INSERT INTO agents (name, codeName, location, status, missionsCompleted)"
                     "VALUES(%s, %s, %s, %s, %s)")
select_all_query = "SELECT * FROM agents"
select_by_name_query = "SELECT * FROM agents WHERE name=%s"
update_agent_query = "UPDATE agents SET {column} = %s WHERE name = %s"
delete_agent_query = "DELETE FROM agents WHERE name = %s"

class Dal:

    __columns = ["id", "name", "codeName", "location", "status", "missionsCompleted"]

    def __init__(self):
        pass

    def add_agent_to_db(self, agent):
        """ add agent into db """

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
        """ select all agents (print)"""
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


    def get_agent_by_name(self, name):
        """ get agent by name """
        try:
            db = mysql.connector.connect(host="localhost",
                                         user="root",
                                         port="3306",
                                         database="agents")

            agent = db.cursor()

            name = [name]

            agent.execute(select_by_name_query, name)

            result = agent.fetchall()
            for n in result:
                print(n)

        except Exception as ex:
            print("error to get agent by name - ", ex)


    def update_agent_missionsCompleted(self, value, name):
        """update agent status and mission competed"""

        column = input("what column you want to update - ")
        if column not in self.__columns:
            raise ValueError
        else:
            update_agent_with_column = update_agent_query.format(column=column)
            print(update_agent_with_column)

        try:
            agents  = mysql.connector.connect(host="localhost",
                                         user="root",
                                         port="3306",
                                         database="agents")

            agent = agents .cursor()

            query = [value,name]

            agent.execute(update_agent_with_column, query)

            agents.commit()

        except Exception as ex:
            print(f"error update {name} - ", ex)


    def delete_agent(self, name):
        """ delete row from agents """
        try:
            db = mysql.connector.connect(host="localhost",
                                         user="root",
                                         port="3306",
                                         database="agents")

            agent = db.cursor()
            name = [name]

            agent.execute(delete_agent_query, name)

            db.commit()

        except Exception as ex:
            print("error to delete agent - ", ex)










