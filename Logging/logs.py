import logging as log

log.basicConfig(level=log.WARNING,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('Data_layer.log'),
                    log.StreamHandler()
                ])

# log.basicConfig(level=log.DEBUG)

if __name__ == '__main__':
    log.debug('Debug message')
    log.info('Info message')
    log.warning('Warning Message')
    log.error('Error message')
    log.critical('Critical message')