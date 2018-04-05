import obd
import redis


class redis_manager(object):
  def __init__(self, db_addr='127.0.0.1', db_port=None, db_num=0, update_key='UPDATE_KEY'):
    self.db_addr = db_addr
    self.db_num = db_num
    self.update_key = update_key
    self.key_list = None

    if db_port is None:
      print("[redis] connecting via unix socket")
      self.db_conn = redis.Redis(unix_socket_path=self.db_addr)
    else:
      self.db_port = db_port
      self.db_conn = redis.RedisStrict(host=self.db_conn, port=self.db_port, db_num=db_num)

  def is_alive(self):
    try:
      self.db_conn.ping()
      return True
    except:
      print("[redis] not reachable at \'{}\'".format(self.db_addr))
    return False

  def update_key_list(self):
    # Verify connectability
    if not self.is_alive():
      return False

    # Retrieve the key list by querying the db
    raw_keys = self.db_conn.get(self.update_key).decode("utf-8")
    if raw_keys is not None:
      self.key_list = raw_keys.split(':')
    else:
      print("[redis] \'{}\' does not exist".format(self.update_key))
      return False

    # Yay!
    return True

  def set_value(self, key, value):
    # Verify connectability
    if not self.is_alive():
      return False
    # Set value in redis
    try:
      self.db_conn.set(key, value)
      return True
    except:
      print("[redis] could not set \'{}\' to \'{}\'".format(key, value))
    return False


class obd_manager(object):
  def __init__(self, port=None):
    self.obd_conn = obd.OBD(portstr=port, fast=True)

  def is_alive(self):
    # We really only care if car is reachable or not
    if self.obd_conn.status() is not obd.OBDStatus.CAR_CONNECTED:
      print("[obdii] status: \'{}\'".format(self.obd_conn.status()))
      return False
    # Car is reachable
    return True

  def query_value(self, request):
    # Make sure we can reach the vehicle
    if self.is_alive():
      try:
        response = self.obd_conn.query(OBD.commands[request])
        if not response.is_null():
          return response
      except:
        print("[obdii] \'{}\' command could not be sent".format(request))

    # RIP
    return None
