from hyperliquid import getTwap
import time

tokens = [
    'PURR', 'HFUN', 'JEFF', 'WAGMI', 'POINTS', 'GMEOW', 'XULIAN', 'RUG', 'ILIENS',
    'CZ', 'BIGBEN', 'KOBE', 'VEGAS', 'PUMP', 'SCHIZO', 'CATNIP', 'HAPPY', 'FARMED',
    'GUP', 'PANDA', 'RAGE'
]

while True:
    for token in tokens:
        getTwap(token)
        time.sleep(5)
    time.sleep(600)




