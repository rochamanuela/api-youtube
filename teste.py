import requests

API_KEY = 'AIzaSyB2bwXAFvbficNF1riIZD9NP_ugcvgmez4'

# URL da API para busca de playlists
url = 'https://www.googleapis.com/youtube/v3/search'

pesquisa = input('Digite o termo de busca: ')
print('\n\n')

# Parâmetros da solicitação
params = {
    'key': API_KEY,
    'q': pesquisa,
    'type': 'playlist',     # Especificar o tipo de resultado como "playlist"
    'part': 'snippet',      # Partes dos dados que você deseja incluir na resposta (snippet é comum)
    'maxResults': 10        # Número máximo de resultados a serem retornados
}

# Faça a solicitação GET para a API
response = requests.get(url, params=params)

# Analise a resposta JSON
data = response.json()

# Examine os resultados
for item in data['items']:
    playlist_id = item['id']['playlistId']  # Obtenha o ID da playlist
    playlist_title = item['snippet']['title']  # Obtenha o título da playlist
    print(f'Título da Playlist: {playlist_title}')
    print(f'Link da Playlist: https://www.youtube.com/playlist?list={playlist_id}')
    print('---')
