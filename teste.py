import requests

API_KEY = 'AIzaSyB2bwXAFvbficNF1riIZD9NP_ugcvgmez4'

# URL da API para busca de vídeos
url = 'https://www.googleapis.com/youtube/v3/search'

pesquisa = input('Digite o termo de busca: ')
print('\n\n')

# Parâmetros da solicitação
params = {
    'key': API_KEY,
    'q': pesquisa,
    'type': 'video',        # Você pode especificar o tipo de resultado (vídeo, canal, playlist, etc.)
    'part': 'snippet',      # Partes dos dados que você deseja incluir na resposta (snippet é comum)
    'maxResults': 10        # Número máximo de resultados a serem retornados
}

# Faça a solicitação GET para a API
response = requests.get(url, params=params)

# Analise a resposta JSON
data = response.json()

# Examine os resultados
for item in data['items']:
    video_id = item['id']['videoId']
    video_title = item['snippet']['title']
    # print(f'Video ID: {video_id}')
    print(f'Título do Vídeo: {video_title}')
    print(f'Link do Vídeo: https://www.youtube.com/watch?v={video_id}')
    print('---')
