from fastapi import FastAPI, HTTPException, status
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
    
from fastapi import Response


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