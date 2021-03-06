import logging

logging.basicConfig(filename='fieldline2ft.log', 
                    
                    level=logging.DEBUG,
                    format='[%(asctime)s](%(module)s %(funcName)s line:%(lineno)d)(thread:%(thread)d) %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

