import os
from dotenv import load_dotenv

# Load existing environment variables from .env file
load_dotenv()

# Set the cache interval time in seconds (adjust as needed)
cache_interval_seconds = 3600  # 1 hour

# Update or add the CACHE_INTERVAL variable in the .env file
with open('.env', 'a') as env_file:
    env_file.write(f'\nCACHE_INTERVAL={cache_interval_seconds}\n')

# Print a message indicating the update
print(f'Cache interval time set to {cache_interval_seconds}.')
