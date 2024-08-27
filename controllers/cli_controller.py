from app import db
# import cli? for controllers


# CONTROLLER? AREA
...


@cli.command("create")
def create_tables():
    db.create_all()

@cli.command("seed")
def seed_tables():
    users = [
        {
            name = "admin"

        }
    ]

@cli.command("drop")
def drop_tables():
    db.drop_all()