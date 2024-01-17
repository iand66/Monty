import logging

myStr = "Stanisław,Wójcik,,Ordynacka 10,Warsaw,,Poland,00-358,+48 22 828 37 39,,stanisław.wójcik@wp.pl,4"

logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
logging.info(myStr)
