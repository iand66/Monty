# TODO DocStrings
from src.main import app

@app.get('/')
async def index():
  return 'Welcome to Monty'