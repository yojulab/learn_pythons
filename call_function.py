import function1

function1.sum()
function1.print_info(name='SangHun Oh', age = 35 )

import time
# while True:
#     function1.sum()
#     function1.print_info(name='SangHun Oh', age = 35 )
#     time.sleep(1)

import schedule
def job():
    print("I'm working...")

schedule.every(5).seconds.do(
    
)
while True:
    schedule.run_pending()
    time.sleep(1)
