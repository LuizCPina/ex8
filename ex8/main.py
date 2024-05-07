from database import Database
from Jogo import JogoDatabase


db = Database('bolt://52.90.253.106:7687', 'neo4j', 'generations-experiences-experience')
db.drop_all()


jogo_db = JogoDatabase(db)

# Criando alguns jogadores
jogo_db.create_player("João")
jogo_db.create_player("Gabriel")
jogo_db.create_player("Luiz")

# Criando algumas partidas
jogo_db.create_match("João,Luiz","Vitória vermelha")


# Atualizando o nome de um Jogador
jogo_db.update_player("Gabriel", "Pedro")

# Encontrando partidas de jogadores
jogo_db.get_player_matches("Luiz")

# Deletando um jogador
jogo_db.delete_player("Pedro")

# Imprimindo todas as informações do banco de dados
print("Jogadores:")
print(jogo_db.get_players())
print("Partidas:")
print(jogo_db.get_match())


# Fechando a conexão com o banco de dados
db.close()