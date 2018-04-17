# Standard import
from time import sleep
from datetime import datetime
import configparser

# Service wrappers
from wrappers import redis_manager
from wrappers import obd_manager

# Command queue
from commqueue import commqueue

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

    # Initialize obd reader, quit if not available
    obdii_manager = obd_manager()
    if not obdii_manager.is_alive():
        print('[obdsync] obdii device is not available')
        quit()

    # Initialize redis manager, quit if not available
    db_manager = redis_manager(db_addr=redis_sock_addr, update_key=update_key)
    if not db_manager.is_alive():
        print('[obdsync] redis is not available')
        quit()

    pri_queue = commqueue()
    commands = db_manager.get_key_list()
    if commands is None:
        print('[obdsync] OBD key list is empty')
        quit()
    else:
        for comm in commands:
            if comm == "RPM" or comm == "SPEED":
                pri_queue.register(comm, 70)
            else:
                pri_queue.register(comm, 5000)

    # Let's update all of the requested values
    while sync:
        if obdii_manager.is_alive() and db_manager.is_alive():
            query = pri_queue.getnext()
            if query is not None:
                print("Getting" + query)
                obd_response = obdii_manager.query_value(query)
                if obd_response is not None:
                    db_manager.set_value(query, obd_response)
                else:
                    db_manager.set_value(query, "-1")
        '''
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
            sleep(wait_time)
        '''


if __name__ == "__main__":
    main()
