import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import albums_v1, artists_v1

# Define FastAPI parameters
metadata = [{'name':'All','description':'**Common Methods**'},
            {'name':'Albums','description':'**Album Methods**'},
            {'name':'Artists','description':'**Artist Methods**'}]

app = FastAPI(title='Monty API', description='API Methods', openapi_tags=metadata, debug=True)

origins = ['http://localhost:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])

app.include_router(albums_v1.router, prefix='/albums/v1', tags=['Albums'])
app.include_router(artists_v1.router, prefix='/artists/v1', tags=['Artists'])

# Welcome page - Server is alive?
@app.get('/', summary='Home Page', tags=['All'])
async def index():
  return 'Welcome to Monty'

# Run Uvicorn
def main() -> None:
  uvicorn.run('main:app', port=8000, log_level='debug', reload=True)
  
if __name__ == '__main__':
  main()


