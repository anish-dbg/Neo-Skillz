from Atm.atm_main import AtmMachine
from Atm.db import Database


db = Database()
atm = AtmMachine()


if __name__ == '__main__':
    db.connection()
    atm.create_pin()
    atm.check_balance()