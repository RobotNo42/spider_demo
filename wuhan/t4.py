import logging

def test():
    log = logging.getLogger()
    log.setLevel(logging.CRITICAL)
    file = logging.FileHandler('test.log')
    file.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file.setFormatter(formatter)
    log.addHandler(file)
    return log


l = test()
l.debug("debug")
l.info("info")
l.warning("warning")
l.error("error")
l.critical("critical")