from database import Base, engine
from models import Item
print("Creating santosh database......")
Base.metadata.create_all(engine)
