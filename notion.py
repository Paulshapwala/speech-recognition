import json
import requests
import main
from notion_client import Client

class notionClient:
    def __init__(self, token, database_name):
        self.token = token
        self.database_id = database_name
        self.notion = Client(auth=token)
        self.res = self.notion.databases.query(
            **{
                "database_id": self.database_id,
            }
        )
    data = self.res.get('results')
        
    