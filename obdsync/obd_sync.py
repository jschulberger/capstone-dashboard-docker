# Standard import
from time import sleep
from datetime import datetime
import configparser

# Service wrappers
from wrappers import redis_manager
from wrappers import obd_manager

# Command queue
#from commqueue import commqueue

# Constants
# TODO: Explicitly set rfcomm port/path (config)
CONFIG_FILE = "sync_config.ini"


def main():
    # Sync loop enabler
    sync = False

    # Use config file for connections attributess
    try:
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        # Get config values
        redis_sock_addr = config['DEFAULT']['socket_addr']
        update_key = config['DEFAULT']['update_key']
        update_interval = float(config['DEFAULT']['update_interval'])

        # Everything went well, make sure we allow sync
        sync = True
        print("[obdsync] config read successfully")
    except:
        print("[obdsync] could not read config")

    # Set all values from config
    db_manager = redis_manager(db_addr=redis_sock_addr, update_key=update_key)
    obdii_manager = obd_manager()

    while not db_manager.is_alive():
        db_manager = redis_manager(
            db_addr=redis_sock_addr, update_key=update_key)

    while not obdii_manager.is_alive():
        obdii_manager = obd_manager()

    # Let's update all of the requested values
    while sync:
        update_start = datetime.now()
        db_manager.update_key_list()

        # Iterate through all keys and record reponse in db
        if obdii_manager.is_alive() and db_manager.key_list is not None:
            for key in db_manager.key_list:
                obd_response = obdii_manager.query_value(key)
                if obd_response is not None:
                    db_manager.set_value(key, obd_response)
                else:
                    db_manager.set_value(key, "-1")

        # Wait if for some reason the queries came back quickly
        wait_time = update_interval - \
            (datetime.now() - update_start).total_seconds()
        if wait_time > 0:
            #print("[main] sleeping for {} seconds".format(str(wait_time)))
            sleep(wait_time)


if __name__ == "__main__":
    main()
