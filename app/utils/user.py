from app.crud import user


def create_any_user(db, obj_in):
    new_user = user.create(db, obj_in=obj_in)

    return new_user
