from sqlalchemy import create_engine, Column, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./vehicles.db"

# Create engine and session local
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class VehicleDB(Base):
    __tablename__ = "vehicles"

    vehicleId = Column(String, primary_key=True, index=True)
    model = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    speed = Column(Float)
    engineTemp = Column(Float)
    isFaulty = Column(Boolean)

def init_db():
    Base.metadata.create_all(bind=engine)

# Dependency to get DB session for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
