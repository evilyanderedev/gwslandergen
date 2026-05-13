import random
choice = random.randint(1,5)
minute = random.randint(1,60)
hour = random.randint(1,12)
day = random.randint(1,31)
month = random.randint(1,12)
views = random.randint(-100, 1000000)
comments = random.randint(1,10)
retweets = random.randint(1,100)
likes = random.randint(1,5000)
bookmarks = random.randint(0,12)

chars = ["giorno", "narancia", "abbachio", "doppio", "diavolo", "bruno", "bucciarati", "fugo", "trish", "mista", "coco jumbo", "polnareff", "nero", "formaggio", "illuso", "prosuctio", "pesci", "melone", "ghiacco", "sorbet", "gelato", "luca", "polpo"]

def func_run_tweet():
    if choice == 1:
        print(random.choice(chars), " fans are so fucking annoying bro")
        return
    elif choice == 2:
        print(random.choice(chars), " fans solo a not reading GW competiton")
        
    elif choice == 3:
        print("no but why did araki write ", random.choice(chars), " they add NOTHING to GW")
        
    elif choice == 4:
        print("im convinced araki just didnt want to write ", random.choice(chars), "'s stand, like its in genuinely only one fight'")
        
    elif choice == 5:
        print(random.choice(chars), " makes me lowkey forgive araki for writing rohan. like it could be worse")
        

def func_start_tweet():
    print("🔘 Oody")
    print("@waterplankton")
    print("")
    func_run_tweet()
    print("")
    print(hour, ":", minute, "AM,", day, "/", month, "/ 2026.   ]", views, "views")
    print("💬", comments, "  🔁", retweets, "  ❤️", likes, "  📄", bookmarks)
    return

func_start_tweet()
