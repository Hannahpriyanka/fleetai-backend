from sqlalchemy import create_engine, Column, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./fleetai.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class VehicleDB(Base):
    __tablename__ = "vehicles"

    vehicleId = Column(String, primary_key=True, index=True)
    model = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    speed = Column(Float)
    engineTemp = Column(Float)
    isFaulty = Column(Boolean, default=False)

def init_db():
    Base.metadata.create_all(bind=engine)
