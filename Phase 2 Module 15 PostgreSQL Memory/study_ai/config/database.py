import os
from dotenv import load_dotenv
from langgraph.checkpoint.postgres import PostgresSaver
load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")

checkpointer=PostgresSaver.from_conn_string(DATABASE_URL)