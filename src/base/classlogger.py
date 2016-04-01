import logging

def send_to_stdout(level = logging.DEBUG):
  logging.basicConfig(
    level = level,
    format = '%(asctime)s.%(msecs)03d %(name)-30s %(levelname)-8s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
  )

class ClassLogger(object):
  __log = None

  def __init__(self, log_instance_id = False):
    name = self.__module__ + "." + type(self).__name__
    if log_instance_id:
      name = name + "(%s)" % id(self)

    self.__log = logging.getLogger(name)

  def log(self):
    return self.__log