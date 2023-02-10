from sqlmodel import create_engine, Session

from app.outer.settings.datastore_settings import datastore_setting

engine = create_engine(
    url=datastore_setting.URL
)


def create_session():
    with Session(engine) as session:
        return session
