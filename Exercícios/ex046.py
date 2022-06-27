import emoji
from time import sleep
for c in range(10 , 0 , -1):
    print(c)
    sleep(1)
print(emoji.emojize('BOOM :boom:', use_aliases=True))