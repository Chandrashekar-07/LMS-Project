# 4. API Routes (routers.py)
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import services

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(name: str, email: str, password: str, role: str, db: Session = Depends(get_db)):
    user = models.User(name=name, email=email, password=password, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/courses/")
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()