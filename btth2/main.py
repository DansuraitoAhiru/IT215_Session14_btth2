from fastapi import FastAPI, Depends, HTTPException, status
from app.routers.student_router import router
from app.database import engine, get_db
from app.models.models import Base
from sqlalchemy.orm import Session
from sqlalchemy import text

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

@app.get("/test-connection")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "Success",
            "message": "Kết nối thành công"
        }
    except Exception as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(error))