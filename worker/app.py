import datetime
import logging
import random
import time

import check_aba


def sleep():
    ts = datetime.datetime.now()
    if ts.hour == 17:
        sleepTime = random.randint(0,5)
    else:
        sleepTime = random.randint(30, 60)
        # sleepTime = random.randint(0,5)
    logging.debug(f'Sleep: {sleepTime}')
    time.sleep(sleepTime)

def main():
    logging.basicConfig(
        filename='tmp/aba.log',
        format='%(asctime)s (%(module)s %(funcName)s %(lineno)d) %(levelname)s: %(message)s', 
        level=logging.INFO
        )

    result = None
    while result is None:
        # try:
        result = check_aba.process()
        if result is not None:
            logging.debug(f'Result: {result}')
        # except Exception as e:
        #     logging.error(e)

        if result == 'No requests':
            time.sleep(10*60)
            result = None

        if result == 'No more dates':
            time.sleep(1*60*60)
            result = None

        if result is None:
            sleep()
        
if __name__ == '__main__':
    main()