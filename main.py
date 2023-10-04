"""
From this point on, the api is being integrated with an external api,
in this case, a YouTube data API. The aim is to return the album link.


import requests

API_KEY = 'AIzaSyB2bwXAFvbficNF1riIZD9NP_ugcvgmez4'
url = 'https://www.googleapis.com/youtube/v3/search' # Default URL for playlist search

search = input('Digite o termo de busca: ')
print('\n\n')

params = {
    'key': API_KEY,
    'q': search,
    'type': 'playlist',
    'part': 'snippet',
    'maxResults': 1
}

response = requests.get(url, params=params)
data = response.json()

playlist_id = ['id']['playlistId']
playlist_title = ['snippet']['title']
print(f'Playlist Title: {playlist_title}')
print(f'Playlist Link: https://www.youtube.com/playlist?list={playlist_id}')
print('_'*40)

"""

from fastapi import FastAPI, HTTPException, status, Response
from models import Music

app = FastAPI()

songs = {
    1 : {
        "id": 1,
        "name": "Memories",
        "artist": "Conan Gray",
        "year": 2022,
        "album": "Superache",
        "genre": "Pop"
    },
    2 : {
        "id": 2,
        "name": "People Watching",
        "artist": "Conan Gray",
        "year": 2022,
        "album": "Superache",
        "genre": "Pop"
    },
    3 : {
        "id": 3,
        "name": "Astronomy",
        "artist": "Conan Gray",
        "year": 2022,
        "album": "Superache",
        "genre": "Pop"
    },
    4 : {
        "id": 4,
        "name": "Family Line",
        "artist": "Conan Gray",
        "year": 2022,
        "album": "Superache",
        "genre": "Pop"
    }
}


@app.get ('/musics')
async def get_musics():
    return songs

@app.get ('/musics/{music_id}')
async def get_music(music_id : int):
    try:
        music = songs[music_id]
        return music
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='music not found :(')
    
##@app.get('/musics/{genre}')
##async def get_music_by_genre(genre: str):
##    try:
##       music = songs(genre)
##        return music
##   except KeyError:
##        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid genre')
  
   
@app.post('/musics')
async def post_music(music: Music):
    last_key = sorted(songs.keys())[-1]
    next_key = last_key + 1
    music.id = next_key
    songs[next_key] = music
    return music


@app.put('/musics/{music_id}')
async def put_music(music_id: int, music: Music):
    if music_id in songs:
        music.id = music_id
        songs[music_id] = music
        return music
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="this music not exists (;-;)")
    

@app.delete('/musics/{music_id}')
async def delete_musics(music_id: int):
    if music_id in songs:
        del songs[music_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="this music not exists (;-;)")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload=True)