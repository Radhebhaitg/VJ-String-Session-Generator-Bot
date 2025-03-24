from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "14012535"))
API_HASH = environ.get("API_HASH", "19b6b514b108611a6a0b51325fe53999")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "5985814740")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "2634611798")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://rlmeena2024:YY9ts6HIiiUWg0sV@cluster0.agcfr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
