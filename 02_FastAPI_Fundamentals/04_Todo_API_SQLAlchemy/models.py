from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__ = 'todos'

# primary_key = True because it basically 
# means that id is our unique identifier 
# index=true so that we can use it directly, as it is unique
# Enhances perfomance.

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default = False)

# Every column has default = Null
# Complete has default = False