from back.api import db


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def delete_row(data):
    db.session.delete(data)
    db.session.commit()