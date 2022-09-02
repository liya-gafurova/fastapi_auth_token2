from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID

from app.db.base_class import Base
from sqlalchemy import String, Column


# table_name will be 'user' anyway - defined in  SQLAlchemyBaseUserTable
class User(SQLAlchemyBaseUserTableUUID, Base):
    username = Column(String(length=320), unique=True, index=True, nullable=False)


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):
    pass
