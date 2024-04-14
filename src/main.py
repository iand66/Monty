import uvicorn
import typer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.helper import trace, secure

from src.api import (
    albums_v1,
    artists_v1,
    customers_v1,
    employee_v1,
    genres_v1,
    mediatype_v1,
    playlists_v1,
    tracks_v1,
)

# Define FastAPI parameters
metadata = [
    {"name": "All", "description": "**Common Methods**"},
    {"name": "Albums", "description": "**Album Methods**"},
    {"name": "Artists", "description": "**Artist Methods**"},
    {"name": "Customers", "description": "**Customer Methods**"},
    {"name": "Employees", "description": "**Employee Methods**"},
    {"name": "Genres", "description": "**Genre Methods**"},
    {"name": "Media Types", "description": "**Media Type Methods**"},
    {"name": "Playlists", "description": "**Playlist Methods**"},
    {"name": "Tracks", "description": "**Track Methods**"},
]

app = FastAPI(
    title="Monty API", description="API Methods", openapi_tags=metadata, debug=True
)

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(albums_v1.router, prefix="/albums/v1", tags=["Albums"])
app.include_router(artists_v1.router, prefix="/artists/v1", tags=["Artists"])
app.include_router(customers_v1.router, prefix="/customers/v1", tags=["Customers"])
app.include_router(employee_v1.router, prefix="/employees/v1", tags=["Employees"])
app.include_router(genres_v1.router, prefix="/genres/v1", tags=["Genres"])
app.include_router(mediatype_v1.router, prefix="/mediatypes/v1", tags=["Media Types"])
app.include_router(playlists_v1.router, prefix="/playlists/v1", tags=["Playlists"])
app.include_router(tracks_v1.router, prefix="/tracks/v1", tags=["Tracks"])


# Welcome page - Server is alive?
@app.get("/", summary="Home Page", tags=["All"])
async def index():
    return "Welcome to Monty"


# Run Uvicorn
def main(
    trace: bool = typer.Argument(trace, help="Enable/Disable DB level logging"),
    secure: bool = typer.Argument(secure, help="Enable/Disable OAuth checks"),
) -> None:
    if trace:
        trace = True
    if secure:
        secure = True
    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)


if __name__ == "__main__":
    typer.run(main)
