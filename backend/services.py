# 3. Services (services.py)
def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first()

def create_course(db, title: str, description: str, instructor: str):
    course = Course(title=title, description=description, instructor=instructor)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course
