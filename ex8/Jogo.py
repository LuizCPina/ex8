class JogoDatabase:
    def _init_(self, database):
     self.db = database


    def create_player(self, name):
     query = "CREATE (:Player {name: $name})"
     parameters = {"name": name}
     self.db.execute_query(query, parameters)


    def update_player(self, old_name, new_name):
     query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
     parameters = {"old_name": old_name, "new_name": new_name}
     self.db.execute_query(query, parameters)


    def delete_player(self, name):
     query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
     parameters = {"name": name}
     self.db.execute_query(query, parameters)


    def create_match(self, player_names, result):
     query = """
     UNWIND $player_names AS player_name
     MATCH (p:Player {name: player_name})
     WITH collect(p) AS players
     CREATE (m:Match {result: $result})
     FOREACH (player IN players | CREATE (player)-[:PARTICIPATES_IN]->(m))
     """
     parameters = {"player_names": player_names, "result": result}
     self.db.execute_query(query, parameters)


    def update_match_result(self, match_id, new_result):
     query = "MATCH (m:Match {id: $match_id}) SET m.result = $new_result"
     parameters = {"match_id": match_id, "new_result": new_result}
     self.db.execute_query(query, parameters)


    def get_players(self):
     query = "MATCH (p:Player) RETURN p.name AS name"
     results = self.db.execute_query(query)
     return [result["name"] for result in results]


    def get_player_matches(self, player_name):
     query = """
     MATCH (p:Player {name: $player_name})-[:PARTICIPATES_IN]->(m:Match)
     RETURN m.id AS match_id, m.result AS result
     """
     parameters = {"player_name": player_name}
     self.db.execute_query(query, parameters)


    def get_match(self, match_id):
     query = "MATCH (m:Match {id: $match_id}) RETURN m.result AS result"
     parameters = {"match_id": match_id}
     self.db.execute_query(query, parameters)


    def delete_match(self, match_id):
     query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
     parameters = {"match_id": match_id}
     self.db.execute_query(query, parameters)