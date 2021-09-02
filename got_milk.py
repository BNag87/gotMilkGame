import random, time, sys

rollResult = 0
plrChoice = 0

# art variables
art_intro1 = "`                       \033[34m.oo`                      /oo  +o+ .oo.         /oo/.\033[0m\n`                       \033[34m-MM.                      yMN  mMd :MM:       /MMMMMMs\033[0m\n`                       \033[34m-MM.                      /so  mMd :MM:       NMd  sMM:\033[0m\n`                       -MM.                           mMd :MM:      /MMh  /MMs\n`     /so:sy:   .+ss+  -hMMy:      oyo+so: +ss:   /ys  mMd :MM:  :ys +MMh  +MMs\n`    hMMdmMM+  +MMdmMN.-mMMd/      mMMmdMMMmdMMy  yMN  mMd :MM:  mMy .::-  hMM+\n`    \033[34mMM+  NM+  mMs  dMs -MM.       mMd  sMm  oMm  yMN  mMd :MM: yMm       +MMm \033[0m\n`   \033[34m:MM+  NM+  MMo  dMs -MM.       mMd  oMm  +MM. yMN  mMd :MM::MM:      yMMh.\033[0m\n`   \033[34m:MM+  NM+  MMo  dMs -MM.       mMd  oMm  +MM. yMN  mMd :MM/mMs      sMMy\033[0m\n`   :MM+  NM+  MMo  dMs -MM.       mMd  oMm  +MM. yMN  mMd :MMmMm       NMN \n`   :MM+  NM+  MMo  dMs -MM.       mMd  oMm  +MM. yMN  mMd :MMNMh       MMm\n`   :MM+  NM+  MMo  dMs -MM.       mMd  oMm  +MM. yMN  mMd :MM+NM+      MMm\n`   \033[34m:MM+  NM+  MMo  dMs -MM.       mMd  oMm  +MM. yMN  mMd :MM:+MN.     yhs\033[0m\n`    \033[34mMMo  NM+  mMo  dMs -MM.       mMd  oMm  +MM. yMN  mMd :MM: dMd       \033[0m\n`    \033[34msMMNMMM+  oMNyhMM:  mMm:      mMd  oMm  +MM. yMN  mMd :MM:  .NMo    dmh\033[0m\n`     :++-NM+   :shyo.    +y:      sho  /hs  :hh. +hy  sho -hh-  +hy    yhs\n`    yy/ .NM+                                                          \n`    +NMMMMh                                                            \n`      :+/-                                                              "

art_bodybuilder1 = ".......``.......``......++.......``......``.......\n........`......```...-+mMMd+-....``......``.......\n........`......```..+dMMMMNNd/...``......``.......\n``.....`````````````/dMMMMMMh/`````````````....```\n......`````````````://+dMMh/://:````````.....`````\n.......``.......`:yNMy.-//..yMMNh:`...............\n.......```.....-sNMMNs..``..yNMMMN-......``.......\n.....``````..-omMMMdyo/.```.-+dMMMmo-```.``.`````.\n````````````-sMMMd/.sMNh```yds:+dMMMmo-```````````\n..oyyo.```-odMMm+...yMMNy`yNMMy..+mmNMmo.``syy/...\n..hMMh.``+dNMmo-``..yMMMM`NMMMh..`--odNm+``NMMs...\n..hMMh../Ndds-..``..yMMMM`NNNMy..``..-omN:`NMMs...\n``hMMmssmmysssssssssdMMMMsNMNMmssssssssymmsNMNs```\n..hMMh..`.......``..yMMMM.NMMMh..``......`.NMMs.`.\n..hMMh.```.....```..yMMMM`NMMMh..``........NMMs...\n..hMMh.``.......``..omMNm`/mMNs..``........NMMs...\n.`/oo/```````````````:o+```+o:`````````````+oo:```"
art_bodybuilder2 = "     `+++`                      :hhh.\n     -MMM:                   `` oMMMo`\n `++sdMMMh:hh-------:::-----:dm:yMMMdo//`\n    ``NMMo `sms-   /NNd   /hmo` +MMM:\n      /++-   `/hms/+MMm/smm:     ...\n                /hMMMMMMN+`\n                 `mMMMMMy\n                  sMMMMN.\n                  /MMMMm\n                  yMMMMm\n                `yMMMMMMy`\n                sMMm/-mMMd`\n                hN+    +NM:\n               .Mh      -Nh\n               `N+       dh\n               `m/       sd.\n               +h+       :os`"
art_bodybuilder3 = "````.-.```````/mNm+```` ````````````````\n ```+dNN+````-NMMMh`````````````-odm+````\n ..+hMMNd-`.-:dNNdN+:.````-.```.yNMMM/```\n .-yhMNmd/:yhhmmNmmNmMNy/yhds::shMMhhs:/-\n ``/hMMMy``/NNMMNMMMMMMN/.mm+``/hMMMM/```\n ```:oy+```+NNMMNMMMMNNMNhMM:```sdNNs````\n ``````````:NMNNhhhhmNNNNMMd`````--.`````\n ```````````:o+.+hdddymdmms-`````````` ``\n ````````````+oydydyyhydy-```````````` ``\n ``````````+mNdmddddMNdNd/```````````````\n `````````:NhNhy/hMdmdhyo```` ```` ``````\n ``````````.ymNN:.sdNNs.`````````````````\n ````````````+ymd``ohNMs`````````````` ``\n `````````````.dMs```+NN-````````````` ``\n ````````````/hdMh+``+mMh.``` ```````````\n ``````````.+hhs-``.yMhN+````````````````\n ``````````````````oydho` ``````` ```` ``"
art_thief1 = ".......``......``////``........``......\n........`..../hmmddmmmdy-......``......\n........`....`hmdmdhhhddm......``......\n``......`````-Ndmhshyohsd:```````......\n.....````````.ddmy/-:/::h````````....``\n```````````` -+dmdm/--:oy.`````....````\n``-.```````.Nmmmmmdhhmmmh:``````````:h`\n``oo/`````:hyyyddddhhdhhhss:```````+/s`\n``-o:o````/hyyyddhhyhhddNhhyys+---:o//-\n````./ohshyshdmdhyydhhhmmo.ohyysymmds``\n`````mddmymdmdmdmhhhhmmdm```::ooss/````\n``...`---.mdmmMNmhohNmddo```.......````\n```....``sdmdNhyhhyysymh`....``````....\n```....`.hmddmyysyyyyshh``....``````...\n`````...sdddmysyymmdyyyhs````..````..``\n``````..dddNdhyymmddmhyydo.``````......\n`````````-/dhhhm+/oo/ddhhhh```..```````\n```....```.hddm+`````-yddd:`````....```\n````.-::/sdhhds//////:+dhhhy`...```````\n```````.......------..``````..........."
art_thief2 = "`..............................`\n`        `sNMms--odMNs         `\n`        yMMMMMMMMMMMMy        `\n`       .MMMMMMMMMMMMMM.       `\n`  oyyyydMMMMMMMMMMMMMMdyyyyo  `\n`  -//////++++////++++//////:  `\n`       .mMMMMm..mMMMMm-       `\n`       :MMMMMM-.MMMMMM:       `\n`     `- +ooo+.  .+ooo+`-`     `\n`     oMNy/`        `:yNMo     `\n`     oMMMMMh+.  .+hMMMMMs     `\n`     oMMMMMMMM  NMMMMMMMs     `\n`  -ohNMMMMMMMM  NMMMMMMMNho-  `\n`-mMMMMMMMMMMMM  NMMMMMMMMMMMm-`\n`mMMMMMMMMMMMMM  NMMMMMMMMMMMMN`\n`MMMMMMMMMMMMMM  NMMMMMMMMMMMMM`\n`NMMMMMMMMMMMMM  NMMMMMMMMMMMMN`\n`+mMMMMMMMMMMMM  NMMMMMMMMMMMm+`\n````````````````````````````````"
art_thief3 = "`                             :+ossyyy+\n`                            -ddddddddd:\n`                            oddddddddd+\n`                           -oydddddddds`\n`                             .yddddddy.       .-:/+ossyyyyyyso+:-.\n`                              .:+oso+///-.-oyhhddddddddddddddddddy/.\n`                                  -sdddddho/+hdddddddddddddddddddddy-\n`                             .:oo+hddddddddds:/yddddddddddddddddddddy\n`                             /ddddddddddddddddo./dddddddddddddddddddm-\n`                         -::/odddddddddddddddddy--hdddddddddddddddddd:\n`                          :sddsyddddddddddddddddh.-hddddddddddddddddm-\n`                            -s+./yddddhdddddddddds`/ddddddddddddddddh\n`                                 ..---.sdddddddddd--dddddddddddddddd:\n`                                 .---:/dddddddddd/+ddddddddddddddd/\n`                               ..+yhdddddddddddddd/sdddddddddddddh/\n`                               -+dddddddddddddddddo/dddddddddddds:\n`                               -hdddddyyyyyhhdddddh:/ydddddddhs/\n`                               -hddddh:----::+dddddy::/+osso/:\n`                               :oddddds:------odddddy:\n`                                :sdddddy/::::::sdddddh\n`                                 /sdddddd+::::::sddddddo\n`                                   ohdddds       ohdddddh+\n`                                     osso         +yddddds\n`                                                    +yhhy+"
art_professor1 = "`    .-:-:--o///              \n`  .-:/+//-.-/o::::            \n` -/-:/+oo::s-o/--:/-    `     \n`:/:::/so/o/++os:/://   `      \n` :+//+o+++-/+/s+/-`     `     \n`     o+-+/:/o-/+       .``.   \n`     //.:ysh/../      `.-`    \n`      /-+yoso:-:      ....    \n`       :-///:./       /.:-    \n`        :::///.       :./     \n`        :s:::++.     //-/--   \n`       +:s-o:/+//`   /:+s+o.  \n`     .:+o++sy/oo/::: o:ooo/::.\n`    /:::o/+ohs+++::o:s/s//    \n`    /:::/+/yys://:/+s/+y+-    \n`    ++::::+sy:/+::oo+::/.     \n`   /:+/::::+y/+::::o/:+       \n`  -/:++::::/o+:::::/+:.       \n`   .:+:::::+o/::::::+         \n`     /:::::o//::::::/:        \n`     +:::::+++:::::::+        \n`     +::::::o::::::::::       \n`     -://:::o::::::::/:       \n`        .+hyyhysssss-         \n`    ./+shddhyhssyhddh+/-      \n`   +sooss+/++++oo/yyyhhdds-   "
art_professor2 = "```````````````-/sdNmyo:.```````````````\n``````````./sdNMMMMMMMMMMmho:.``````````\n`````./ohNMMMMMMMMMMMMMMMMMMMMmho/.`````\n`````h/sdNMMMMMMMMMMMMMMMMMMMMNhs/.`````\n`````y````-+sdMMMMMMMMMMMNhs/.``````````\n`````y````.yo/.-+ydMNhs/--/sh.``````````\n`````y````yMMMMmho:.-+sdNMMMMh``````````\n````-h.```NMMMMMMMMMMMMMMMMMMM.`````````\n```oMMM:``mMMMMMMMMMMMMMMMMMMN``````````\n```.sho```/MMMMMMMMMMMMMMMMMM+``````````\n```````````/NMMMMMMMMMMMMMMN+```````````\n````````````.ymMMMMMMMMMMNh:.```````````\n```````:oydNMMo-+syhhys+-+MMMNdy+-``````\n````-yNMMMMMMMM/````````:MMMMMMMMMm+````\n```oMMMMMMMMMMMN:``````-NMMMMMMMMMMMy```\n```NMMMMMMMMMMMMN.````.mMMMMMMMMMMMMN```\n```NMMMMMMMMMMMMMm````dMMMMMMMMMMMMMN```\n```NMMMMMMMMMMMMMMh``yMMMMMMMMMMMMMMN```\n```NMMMMMMMMMMMMMMMsoMMMMMMMMMMMMMMMN```\n```NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN```\n```yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy```"
art_professor3 = "`                       `..-:::.`\n`                    `-::---...-::`\n`               `.//::..-:-....../-\n`            `-:+:::--//:--.....-/.\n`         -++o+oo/+/o++oo/......-/\n`         h+/+yooh:+::/s++s:..../-\n`         -os:-.:o++/o+o/+o/++/oo`\n`          /:-:::/--+yo++--.--:/-/-\n`          //:---....::-.....-/-:/.\n`       `:/::----/////::/...-:-/``\n`        `.......``/hhmh//..-/:`\n`    .`          `-oNhsy::..-/``\n`  ./:-:.`       `:://::-.---:+:-.\n``:////::/`        `.:-.-.-//+ss`-:\n`:/--+::+-           `+/:///s/:s` `:..``\n`:/://::/.         `.:h+++//::+y`  -``---`\n`./-/-/+-`      ``--.`-/++++o+/o  `.    `--`\n` ./-:-:/+:`   ---`  : ++//:::o-  -` :.   `--\n`  -o//::` .--//`    o o/:::::o. `.  /-    `:-\n` :shs:`    ``. `   :: o/:::::o. .`  ./     `/.\n` :yo.              +`.o/::::/+``.    :-      o`\n`  `.-:.          `-s`:o:::::+/`.-.`   o.`:   ./`\n`      .--``    `--`o`:o:::::+/:::::..:://:-   ./`\n`        `.-::::-`  +`/so::::+/:::.-////        +.\n`                   +/o::::::+::::.::/+//       +.\n`                   /+:::::::+:-----:::++     `./.\n`                  .o::::::::/+::...:hhs- `.:--.`\n`                  /+::::::::/+-    `/+-.--.\n`                  /+:::::::::s.      `..+`\n`                 .o/:::::::::+.         +.\n`                  /+ooo////os/    `....`o.\n`                  /-ydddddddh/   -`     +.\n`                  /-yddmmdddo    -`     +.\n`                  :-syyyyhhyo::::/::::::o."

art_gameover2 = "\033[0m   `-ysssssso     `+yssy-`    :yys`  `-yys   oyyssssssss:\n\033[31m `.ydd+-----.   ./hdh-odds.`  +NNmh+.ydNNm   hNNo-------`\n\033[0m +mNd`` ----.   dmN/` `.dmm/  +NNNNmmNNNNm   hNNo------\n\033[31m oNNh  `ohNNh   mNNs///+mNN+  +NNmshNyyNNm   hNNhssssso\n\033[0m -+mdo-  +NNh   mNNs++++mNN+  +NNd`-+`:NNm   hNN+\n\033[31m   -+mhyyhmmh   dmm:   `hmm+  /mmh`   :mmm   hmmhyyyyyyy/\n\033[0m    `........   ...`    ...`  `...    `...   ...........`\n \n  `.......     `..     `..`  `..........`   `........`\n\033[31m .:dmyyyydm+-   mmm:   `dmN+  +Nmmyyyyyyys   hmmdyyyymd:.\n\033[0m oNNh    +NNh   mNN:   `dNN+  +NNd`          hNN+    hNNo\n\033[31m oNNh    /NNh   mNNhs`:ymNN+  +NNmyssssy-    hNN/  -smNNo\n\033[0m oNNh    /NNh   .+mmmddNmh-`  +NNd-.....`    hNNdhhdN+:.`\n\033[31m /hmd----oNds    ``ohNdh-`    +NNd--------   hNN+.ydNmd-.\n\033[0m  `ssssssss-`      `.s/`      :yysssssssso   oyy: `:yyss:\n"
art_milk = "\033[34m          ````````````````\n        .-ddddddddddddddNh\n        hN++++++++++++++Md\n      -/mMssssssssssssssMm/-\033[0m\n     .+shhhhhhhhhhhhhhhNMssso+.\n    :Mo.............+ho+   +Mhs`\n  `hys/:::::::::::::yM: yyyo/dM`\n  `MNddddddddddddddhdMdh:::::dM`\033[34m\n  `Md///\033[0m::\033[34m/////\033[0m::\033[34m///yMo//////dM`\n  `Md///\033[0m`/: \033[34m//\033[0m:`/\033[34m///yMs//////dM`\n  `Md///\033[0m`/-.-..`/\033[34m///yMs//////dM`\n  `Md///\033[0m` /\033[34m/-:\033[0m/`/\033[34m///yMs//////dM`\n  `Md///\033[0m` /\033[34m///\033[0m/`/\033[34m///yMs////:.hM`\n  `Md///:-/////:-///yMo/...` hM`\n\033[0m  `Mh...............sM/. `:-`yN`\n  `Md///////////////yMo//+mdd/.\n    `mmddddddddddddddddmdddy"

#art tuples
art_bodybuilders = (
    art_bodybuilder1, art_bodybuilder2, art_bodybuilder3
)
art_thieves = (
    art_thief1, art_thief2, art_thief3
)
art_professors = (
    art_professor1, art_professor2, art_professor3
)
# functions to call single art pieces and print
def display_art_milk():
    print(art_milk)

def display_art_intro():
    print(art_intro1)

def display_art_bodybuilder1():
    print(art_bodybuilder1)

def display_art_bodybuilder2():
    print(art_bodybuilder2)

def display_art_bodybuilder3():
    print(art_bodybuilder3)

def display_art_thief1():
    print(art_thief1)

def display_art_thief2():
    print(art_thief2)

def display_art_thief3():
    print(art_thief3)

def display_art_professor1():
    print(art_professor1)

def display_art_professor2():
    print(art_professor2)

def display_art_professor3():
    print(art_professor3)

def display_art_gameover2():
    print(art_gameover2)

# function for random art in list
def rand_art_bodybuilders():
    print(art_bodybuilders[random.randint(0,2)])

def rand_art_thieves():
    print(art_thieves[random.randint(0,2)])

def rand_art_professors():
    print(art_professors[random.randint(0,2)])

# set color variables
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
purple = "\033[35m"
teal = "\033[36m"
blue = "\033[34m"
no_color = "\033[0m"

# colorful functions
def print_red(string_in):
    convertstring = str(string_in)
    return(red + convertstring + no_color)

def print_green(string_in):
    convertstring = str(string_in)
    return(green + convertstring + no_color)

def print_yellow(string_in):
    convertstring = str(string_in)
    return(yellow + convertstring + no_color)

def print_purple(string_in):
    convertstring = str(string_in)
    return(purple + convertstring + no_color)

def print_teal(string_in):
    convertstring = str(string_in)
    return(teal + convertstring + no_color)

def print_blue(string_in):
    convertstring = str(string_in)
    return(blue + convertstring + no_color)

# This creates a loop in which it iterates over the message, and sleeps for a short duration before typing the next character, providing a typewriter aesthetic
def typewrite(message, delay_between_char = 0.01, new_line = True):
    # This will take a provided message
    # and a supplied time (in seconds) which it will wait for between typing letters
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay_between_char)
    # Print an empty line to reduce the need for \n after every typewrite()
    if new_line == True:
        print()

# dialogue nested tuple
# access individual elements with 'dialogue_list[0][1]' 
# (this would access the first list in the list and return the second element "You wake up form a deep sleep...")
intro_dialogue_list = (
    ("INTRODUCTION",
    "You wake from a deep sleep. Yawning deeply, you feel there is something important you need to do.",
    "Through the brain fog of waking up, the memory slowly becomes clearer. As you plant your feet in to your slippers, you are nearly heartbroken as you remember something terrible...",
    "You have NO milk in your fridge...",
    "As full blown panic sets in, you forget who you are.",
    "Through the mind numbing fear, you realise this is a chance to remake yourself.",    
    "Ruffling through your pockets you find a couple of ",
    "pound coins ",
    "and make plans to head to the ",
    "grocery store",
    "You leave home, walk through the estate, it looks like the heavens are about to open up.",
    "The environment looks miserable and you have the feeling that things won't go your way today.",
    "A mile into your journey, drenched in rain with holes on your shoes, birds flocking in the sky and you happen to see some of the most bizare characters on the way.",
    "You ask yourself what else can potentionally happen today...?"
    ),
    
     ("Chapter 1","Something"),
     ("Chapter 2", "Something"),
     ("Chapter 3", "Something"),
)

charList = [["The Player", 33, 30, "Protagonist", 1, 2, False, 5, 3, 3],
            ["The Strongman", 40, 30, "Strongman", 1, 2, False, 5, 1, 3]]

events_list = (
    ("ID", "Event Name", "Dialogue 1", "Dialogue 2","Dialogue 3", "PLAYER CHOOSES AN OPTION"),
    (1,"Strongman", 
        "You see a well built man. He sees you and moves to block your path. When you try to step around him, he blocks your movement.", 
        "You ask him: '\033[36mLet me pass. I need to buy milk, urgently!\033[0m.", 
        "He responds: '\033[33mYou shall not pass. I move... for no man. Unless you can beat me in an arm wrestle!'\033[0m. What will you do?",        
        "")
)

event_body_builder_choices_list = (
    ("Event ID", "Choice 1", "Choice 2", "Choice 3"),
    ("1", "Try to knock him out", "Try to baffle him", "Try to somersault over him"),
    ("2", "something", "sOmEtHiNg", "SOMETHING ELSE")
    )

event_character_choices_list = (
    ("Event ID", "Choice 1", "Choice 2", "Choice 3"),
    ("1", "Strongman", "Thief", "Professor")
    )

event_riddles_list = (
    ('"What gets wetter as it dries?"', 
    '"Jim\'s parents have three sons called "Snap" and "Crackle". What is the name of their third son?"', 
    '"Why did the girl fall off the swing?"',
    '"What runs all around a garden, but never moves?"', 
    '"Which weighs more? A tonne of bricks or a tonne of feathers?"' ),

    ('"A towel!"', 
    '"Jim!"', 
    '"She had no arms!"',
    '"A fence!', 
    '"They\'re the same!"' ),

    ("They look thoughtful for a moment, but then start crying. They run away in shame.", 
    "They look slack-jawed. All mental activity has ceased. They are now a vegetable",
    "Standing open mouthed, he stares vacantly in to the distance",
    "They start sweating and looking more and more nervous. They start hyperventilating.", 
    "They think REALLY hard, but end up with a migraine and have to go home to lay down.",
    "He stutters and stammers. Eventually from the stress of talking and thinking, he falls asleep.", 
    "When he finally thinks he has the answer, he instead starts screaming like an ape. He climbs a lamp post and swings from one to the other, until you no longer see him.", 
    "You hear a loud, wet pop. Then you see grey mush leaking from his ear. His brain exploded.", 
    "They start pacing around, desperately trying to figure out the answer. They then walk right in to a lamp post and knock themselves out."),
    (-1, 0, 1,2,2)
    )

speed_choices_list = (
        ("#ID", "Choice1","Choice2","Choice3"),
        ("1", "Dodge", "Dash", "Backflip")
    )

# tuples as we don't need to change any data
chocolate_surname = (    
    "Wonka",
    "Loompa",
    "Bucket",
    "Teavea",
    "Slugworth",
    "Gloop",
    "Salt",
    "Beauregarde",
    "Pondicherry",
    "Turkentine"
)   

fool_surname = (
    "Buffoon",
    "Clown",
    "Bozo",
    "Jester",
    "Joker",
    "Harlequin",
    "Funster",
    "Picador",
    "Gagster",
    "Wisecracker"
)

def weather_event():
    w = random.randint(1,3)
    if w == 1:
        typewrite("The sun in the sky beams down making you optamistic about the milk you'll soon buy",0.03)
    elif w == 2:
        typewrite("It starts to rain but that doesn't distract you from knowing you'll soon be buying milk",0.03)
    else:
        typewrite("A gust of wind chills you. Althings considered getting this milk will be worth it",0.03)
    
def generate_player_name():    
    # generate random surname from 2 tuples
    rand_first_surname = random.choice(chocolate_surname)
    rand_second_surname = random.choice(fool_surname)
    double_barrel_surname = f"{rand_first_surname}-{rand_second_surname}"

    first_name = input("What is your first name?\n")
    # capitalize and truncate the first name
    first_name = first_name.capitalize()[0:20]
    
    full_name = f"{first_name} {double_barrel_surname}"
    
    print(f"Welcome... " + str(print_purple(full_name)) + "\n")
    
    # store players name in our list
    charList[0][0] = full_name    

def randomize_player_age():
    # randomize age    
    age = random.randint(10, 110)
    # store players age in our list    
    charList[0][1] = age
    
    if age >= 101:
        typewrite(f"You're " + str(print_yellow(age)) + f" years old! You don't look a day over {age - 10}\n", 0.03)
    elif age >= 50:
        typewrite(f"You're " + str(print_yellow(age)) + " years old, bet you wish you were still 40!\n", 0.03)
    else:
        typewrite(f"You're " + str(print_yellow(age)) + " years old, young whippersnapper!\n", 0.03)

def choose_character():
    # choice of 3 pre-determind charcters
    # store players "Strength", "Smarts", "Speed" in our list
    # x is the amount of times to loop
    # length_of_list is the length of the  #event_character_choices_list[1]
    
    length_of_list = len(event_character_choices_list[1])
    
    # for loop to print out all available choices... 
    # this will ignore the first element in the list (for x in range (1....))
    x = 0
    print("Choose your profession, it will affect your " + str(print_blue("Strength")) + ", " + str(print_blue("Smarts")) + " & " + str(print_blue("Speed")) + " attributes:")
    for x in range(1,(length_of_list)):
        print("\t" + str(x) + ": " + str(event_character_choices_list[1][x]))
        x += 1 

    # now allow the player to choose an option (1 to x from the loop above)     
    player_choice = input_number("\nEnter your choice (1-" + str(x-1) + "):")
    
    print("You chose: " + str(print_blue(event_character_choices_list[1][int(player_choice)])))
    
    if int(player_choice) == 1:        
        rand_art_bodybuilders()

        charList[0][7] = 5
        charList[0][8] = 1
        charList[0][9] = 3
    elif int(player_choice) == 2:
        rand_art_thieves()
        
        charList[0][7] = 1
        charList[0][8] = 3
        charList[0][9] = 5
    elif int(player_choice) == 3:
        rand_art_professors()
                
        charList[0][7] = 1
        charList[0][8] = 5
        charList[0][9] = 3
    else:
        print("Should not get here!")

def output_intro_dialogue():
    # output intro dialog list
    typewrite(intro_dialogue_list[0][1], 0.03)
    typewrite(intro_dialogue_list[0][2], 0.03)
    typewrite(intro_dialogue_list[0][3], 0.03)
    time.sleep(0.5)
    print()
    typewrite(intro_dialogue_list[0][4], 0.03)
    typewrite(intro_dialogue_list[0][5], 0.03)    

def output_intro_dialogue_after_name():
    # output intro dialog list
    
    pound_coins = print_teal(intro_dialogue_list[0][7])    
    grocery_store = print_green(intro_dialogue_list[0][9])
    
    typewrite(intro_dialogue_list[0][6] + pound_coins + intro_dialogue_list[0][8] + grocery_store + ".", 0.03)

    print("")
    typewrite(intro_dialogue_list[0][10], 0.03)
    typewrite(intro_dialogue_list[0][11], 0.03)
    time.sleep(0.5)
    print("")
    typewrite(intro_dialogue_list[0][12], 0.03)
    typewrite(intro_dialogue_list[0][13], 0.03)

def input_number(message):
   while True:
      try:
         user_input = int(input(message))
         if user_input == 1 or user_input == 2 or user_input ==3:
            return user_input 
            break            
         else:
            print("You need to enter 1,2 or 3\n")
            continue
      except ValueError:
         print("You need to enter 1,2 or 3\n")
         continue      

def output_choices(): 
    # x is the amount of times to loop
    # length_of_lList is the length of the  #event_body_builder_choiceslist[1]
    x = 0
    length_of_list = len(event_body_builder_choices_list[1])

    # print out the event dialogue
    print()
    for x in range(1,(length_of_list)):
        typewrite("\t"+str(events_list[1][x+1]), 0.03)        
        x += 1
    
    # for loop to print out all available choices... 
    # this will ignore the first element in the list (for x in range (1....))
    x = 0
    print()
    for x in range(1,(length_of_list)):
        print("\t" + str(x) + ": " + str(event_body_builder_choices_list[1][x]))
        x += 1 

    # now allow the player to choose an option (1 to x from the loop above)     
    player_choice = input_number("\nEnter your choice (1-" +str(x-1)+"):")
    plrChoice = player_choice

    print("You chose: " + str(event_body_builder_choices_list[1][int(player_choice)]))

    if int(player_choice) == 1:        
        attack_target()
        if charList[0][6] == False:
            output_dialogue_after_strong_event()
        else:
            game_over(True, False)
    elif int(player_choice) == 2:        
        outsmart_target()
        if charList[0][6] == False: 
            output_dialogue_after_smart_event()
        else:
            game_over(True, False)
    elif int(player_choice) == 3:        
        speed_target()
        if charList[0][6] == True: 
        #    output_dialogue_after_speed_event()
        #else:
            game_over(True, False)
    #elif int(player_choice) == 4:
        #print(f"do something! for choice {player_choice}")
        #checkStats()
    else:
        print("Should not get here!")

def fight_over(actor_ref, player_dead, rounds, player_misses, actor_misses, player_crits, actor_crits):
    print("\n=|AFTER ACTION REPORT|===============================================================")
    if player_dead == True:
        print("|\tOh no! Your vision went black as your spine was punched out of your back! You died!!!")
    else: 
        print("|\tYou managed to punch the "+ str(print_blue(actor_ref)) +" to death! You won!")
    print("|\tYou dealt "+ str(print_yellow(rounds)) +" blows between you.")
    if player_misses == 0:
        print("|\tAmazingly, you didn't miss a single of those punches!.")    
    elif player_misses == 1:
        print("|\tYou only missed a single one of those punches!.")    
    else:
        print("|\tUnfortunately, you also punched the air "+ str(print_yellow(player_misses)) +" of those times.")

    if actor_misses == 0:
        print("|\tTo your great shame, they didn't miss a single one of their punches!")    
    elif actor_misses == 1:
        print("|\tUnfortunately, they missed only one of their punches.")    
    else:
        print("|\tYou almost laughed each time they missed "+ str(print_yellow(actor_misses)) +" of their punches.")

    if player_crits == 0:
        print("|\tYou didn't do any major damage with any punches.")
    elif player_crits == 1:
        print("|\tYou made him scream once with a lucky hit!")
    else:
        print("|\tYou made him scream "+ str(print_yellow(player_crits)) +" times with BRUTAL attacks.")
        print("|\tHe no longer looks human...Ew...")
    if actor_crits == 0:
        print("|\tYou thank the heavens that they didn't land a single devastating punch.")
    elif actor_crits == 1:
        print("|\tYou coughed blood when they punched you in the throat.")
    else:
        print("|\tYour cried like a baby, "+ str(print_yellow(actor_crits)) +" times, from their BRUTAL strikes.")
        print("|\tYou're going to need plastic surgery before your open casket funeral...Ew...")
    print("====================================================================================\n")

def generate_actor_strength_bonus():
    # this function will set a bonus to strength rolls depending on the strength attribute
    actor_strength_bonus = 0
    if charList[1][7] == 1:
        actor_strength_bonus = -5
        return actor_strength_bonus
    elif charList[1][7] == 3:
        actor_strength_bonus = 0
        return actor_strength_bonus
    elif charList[1][7] == 5:
        actor_strength_bonus = 5
        return actor_strength_bonus
    else:
        print("Something went wrong when setting the actor_strength_bonus. Setting it to 0")
        return actor_strength_bonus
        
def generate_actor_smarts_bonus():
    # this function will set a bonus to smarts rolls depending on the SMA attribute
    actor_smarts_bonus = 0

    if charList[1][8] == 1:
        actor_smarts_bonus = -5
        return actor_smarts_bonus
    elif charList[1][8] == 3:
        actor_smarts_bonus = 0
        return actor_smarts_bonus
    elif charList[1][8] == 5:
        actor_smarts_bonus = 5
        return actor_smarts_bonus
    else:
        print("Something went wrong when setting the actor_smarts_bonus. Setting it to 0")
        return actor_smarts_bonus

def generate_player_smarts_bonus():
    # this function will set a bonus to smarts rolls depending on the smarts attribute
    player_smarts_bonus = 0

    if charList[0][8] == 1:
        player_smarts_bonus = -5
        return player_smarts_bonus
    elif charList[0][8] == 3:
        player_smarts_bonus = 0
        return player_smarts_bonus
    elif charList[0][8] == 5:
        player_smarts_bonus = 5
        return player_smarts_bonus
    else:
        print("Something went wrong when setting the player_smarts_bonus. Setting it to 0")
        return player_smarts_bonus

def generate_actor_speed_bonus():
    #this function will set a bonus to speed rolls depending on the spe attribute
    actor_speed_bonus = 0
    if charList[1][9] == 1:
        actor_speed_bonus = -1
        return actor_speed_bonus
    elif charList[1][9] == 3:
        actor_speed_bonus = 0
        return actor_speed_bonus
    elif charList[1][9] == 5:
        actor_speed_bonus = 1
        return actor_speed_bonus
    else:
        print("Something went wrong when setting the actor_speed_bonus. Setting it to 0")
        return actor_speed_bonus    

def generate_player_speed_bonus():
    # this function will set a bonus to speed rolls depending on the speed attribute
    player_speed_bonus = 0
    if charList[0][9] == 1:
        player_speed_bonus = -1
        return player_speed_bonus
    elif charList[0][9] == 3:
        player_speed_bonus = 0
        return player_speed_bonus
    elif charList[0][9] == 5:
        player_speed_bonus = 1
        return player_speed_bonus
    else:
        print("Something went wrong when setting the player_speed_bonus. Setting it to 0")
        return player_speed_bonus

def dice_roller(count, sides, bonus):
    # convert inputs to variables
    count_to_roll = count
    number_of_sides = sides
    bonus_to_add = bonus
    # create variables for use inside the function
    loop_index = count_to_roll
    x = 0
    roll_total = 0

    # as long as x is less than the number of times you roll the dice...
    while x < count_to_roll:
        # increase the x index...
        x += 1
        # create a variable to store a random dice roll between 1 and the number of sides the dice has...
        result = (random.randint(1, number_of_sides) + bonus)
        #print out the result...
        #print("Roll "+str(x)+": [1d"+str(number_of_sides)+"] = " +str(result))
        # set a variable to store the result of the roll (including multiple rolls)...
        roll_total = roll_total + result

    # ...then if there are any bonuses to the roll, add them here whilst printing them out
    #print("Bonus: +"+str(bonus_to_add)+".")   
    #print("Total (with bonus): "+str(rollTotal+bonus_to_add)+".\n")   

    # beware. this only returns the result of the last roll done in the while loop, not the first or any others in between.
    return result

def attack_target():
    # make vars to track a combat run...
    number_of_rounds = 0
    number_of_player_crits = 0
    number_of_player_misses = 0

    number_of_actor_crits = 0
    number_of_actor_misses = 0

    # make vars to control a loop that checks if the player or actor is dead...
    player_is_dead = charList[0][6]
    actor_is_dead = charList[1][6]
    # generate the strength bonus of the player...
    strength_bonus = generate_actor_strength_bonus()    
    # this will change whose turn it is and apply rolls to the other target
    turnIndex = 0

    # create the loop to attack and deal damage
    while player_is_dead == False or actor_is_dead == False:
    # as nobody is dead, take turns attacking until someone dies.
    # player always goes first

        # FIRST, check if the player or the actor are already dead  (have less than or equal to 0 hit points)
        if player_is_dead == True:
            charList[0][6] = True            
            fight_over(charList[0][3], player_is_dead, number_of_rounds, number_of_player_misses, number_of_actor_misses, number_of_player_crits, number_of_actor_crits)
            break
        elif actor_is_dead == True:
            charList[1][6] = True            
            fight_over(charList[1][3], player_is_dead, number_of_rounds, number_of_player_misses, number_of_actor_misses, number_of_player_crits, number_of_actor_crits)
            break


        # NOW, generate an attack roll as neither character would be dead at this point
        attack_roll = dice_roller(1, 20, strength_bonus)        
        number_of_rounds += 1

        # SECOND, check if the attack roll was a critical hit, then apply that damage to whoever's turn it isn't
        if int(attack_roll) == 20:
            damage_done = int((dice_roller(1,4, strength_bonus))*2)

            if turnIndex == 0:
                number_of_player_crits +=1
                charList[1][2] -= ((damage_done) + strength_bonus)
                turnIndex = 1

            else:
                number_of_actor_crits +=1
                charList[0][2] -= ((damage_done) + strength_bonus)
                turnIndex = 0

        elif int(attack_roll) >= 13 and int(attack_roll) < 20:

            damage_done = int(dice_roller(1,4, strength_bonus))
            if turnIndex == 0:
                charList[1][2] -= ((damage_done) + strength_bonus)
                turnIndex = 1
                
            else:
                charList[0][2] -= ((damage_done) + strength_bonus)
                turnIndex = 0
                
        # after applying damage, check if the actor is dead    
        if charList[turnIndex][2] <= 0:
            if turnIndex == 0:
                player_is_dead = True
                charList[0][6] = True
                continue

            else:
                actor_is_dead = True
                charList[1][6] = True
                continue

        elif int(attack_roll) < 13:
            if turnIndex == 0:
                number_of_player_misses += 1
                turnIndex = 1
                
            else:
                number_of_actor_misses += 1
                turnIndex = 0

def outsmart_target():
    # make a variable to store results of dice rolls
    roll_result = 0

    # need the player to tell a random riddle, but not repeat themselves
    # get a random index
    actor_smarts_bonus = generate_actor_smarts_bonus()
    player_smarts_bonus = generate_player_smarts_bonus()
    
    riddle_index = random.randint(0,int(len(event_riddles_list[0])-1))
    
    difficulty_mod = event_riddles_list[3][riddle_index]
    # depending on how smart the player is will make it harder for the riddle to be solved
    difficulty_class = (12 + difficulty_mod + player_smarts_bonus)
    
    # #dice roll for the smarts check!
    roll_result = dice_roller(1, 20, actor_smarts_bonus)
    
    typewrite("\nYou feel you can outsmart this strongman. You decide to tell him one of your many favourite riddles.",0.01)
    typewrite("\n\t" +str(event_riddles_list[0][riddle_index]) + " you ask him.\n",0.065)

    # now the actor needs to check if they understand the riddle
    # a dice roll is already available to check at this point so use it

    if roll_result < difficulty_class:
        randResponse = random.randint(0,int(len(event_riddles_list[2])-1))
        typewrite("\t...", 0.3)
        typewrite("\t...", 0.2)
        typewrite("\t...\n", 0.1)
        typewrite("\t" +str(event_riddles_list[2][randResponse]),0.04)
        typewrite("\nWith him out of the way, you are free to move on!")
        
    elif roll_result >= difficulty_class:
        typewrite("\t...", 0.3)
        typewrite("\t...", 0.2)
        typewrite("\t...\n", 0.1)
        typewrite("\t" +str(event_riddles_list[1][riddle_index]+ " he says excitedly. He's very proud of himself!\n"),0.04)
        typewrite("Damn...now he's still blocking your way...\n")
        typewrite("But he's happy with himself and leaves!\n")
        
def speed_target():
    # make vars to track a speed combat run...
    number_of_rounds = 0
    number_of_player_crits = 0
    number_of_player_misses = 0

    number_of_actor_crits = 0
    number_of_actor_misses = 0
    # make vars to control a loop that checks if the player or actor is dead...
    player_is_dead = charList[0][6]
    actor_is_dead = charList[1][6]
    # generate the speed bonus of the player...    
    player_speeed_bonus = generate_player_speed_bonus()
    # generate the speed bonus of the actor...    
    actor_speed_bonus = generate_actor_speed_bonus()
    # make SpeedPoints counter for player
    player_speed_points = 3 + player_speeed_bonus
    if player_speed_points <= 0:
        player_speed_points = 1
    else:
        player_speed_points = player_speed_points
    # make SpeedPoints counter for actor
    actor_speed_points = 3 + actor_speed_bonus
    if actor_speed_points <= 0:
        actor_speed_points = 1
    else:
        actor_speed_points = actor_speed_points        
    # combat using player choices
    # list choices in speedCombat
    
    typewrite("After artfully acrobatting out of his peripheral vision,\n you have the initiative to plan your means of escape.", 0.03)
    x = 0
    length_of_list = len(speed_choices_list[1])
    for x in range(1,(length_of_list)):
        print("\t" +str(x)+": " + str(speed_choices_list[1][x]) +"")
        x += 1
    print("\nEnter your choice (1-" +str(x-1)+"):")
    player_choice = input()
    print("You chose: " +str(speed_choices_list[1][int(player_choice)]))
    # roll dice
    speed_roll = dice_roller(1, 20, player_speeed_bonus)
    success_roll = bool
    if speed_roll <= 7:
        success_roll = False
    else:
        success_roll = True
    if success_roll == False and int(player_choice) == 1:
        print("\033[31mfailed\033[0m")
        typewrite("Apparently you forgot to be the ball and the strongman\n judges your movements and lands a killing hit to your face.", 0.03)
        
        game_over(True, False)
    elif success_roll == False and int(player_choice) == 2:
        print("\033[31mfailed\033[0m")
        typewrite("You turn yourself into a sonic pin ball and roll right into\n his foot, which kicks you backs home\n although with the force of the kick you wish it were the hospital.", 0.03)
        
        game_over(True, False)
    elif success_roll == False and int(player_choice) == 3:
        print("\033[31mfailed\033[0m")
        typewrite("You perform a backflip and land on your back.\n Which shatters your spine and any hope of getting milk.", 0.03)
        
        game_over(True, False)  
    # Dodge
    elif success_roll == True and int(player_choice) == 1:
        print("\033[32msuccess\033[0m")
        typewrite("Feeling brave, you start jumping around the Strongman.\nHe tries to grab you, but misses every time.\nOn his last grab, you dodge so hard, that you jump over your own house.\nYou carry on jumping all the way down the street, then eventually reach the shop.", 0.03)
        
        game_won()
    # Dash
    elif success_roll == True and int(player_choice) == 2:
        print("\033[32msuccess\033[0m")
        typewrite("Defying physics, you compress yourself into a ball and begin spinning.\nConfused, the Strongman backs away.\nNow you unlesh your momentum and you speed past him at a worrying speed.\nYou pump your legs with minimal effort and arrive at the shop within seconds, this normally would have taken an hour if you had walked.", 0.03)
        
        game_won()
    # Backflip
    elif success_roll == True and int(player_choice) == 3:
        print("\033[32msuccess\033[0m")
        typewrite("The Strongman throws a deadly punch at you.\nBut you are faster than him!.\nYou backflip onto the top of a lamp post, you swing to the next and out of harms way.\nThe lamposts are your jungle, you swing from one to the next all through the neighbourhood.\nSoon after, you land in front of the shop.", 0.03)
                
        game_won()
    else:
        print("Something went wrong in the 'speed_target' event")

def game_won():
        print("===============================================================================================")
        typewrite(f"\tCongratulations! " + str(print_yellow(charList[0][0])) + " has successfully got milk!")
        print("-----------------------------------------------------------------------------------------------")
        # print out a game over screen here!
        typewrite("As you leave the shop, with milk in hand, the scent of success is in the air.", 0.05)
        typewrite("You walk past crowds on the high street, you can hear chants and echos of your name in your head...\n", 0.07)
        time.sleep(0.5)
        typewrite("The feeling of a newly crowned heavyweight champion, ", 0.04)
        typewrite("Sweet sensation of victory...\n", 0.07)
        time.sleep(0.5)
        typewrite("Feels like a dream.", 0.04)
        typewrite("Ain't no feeling topping this.", 0.05)
        typewrite("You sink to your knees, heart full of joy...", 0.04)
        typewrite("Success is all you know now...", 0.07)
        typewrite("Never knew buying milk could be this satisfying...\n", 0.04)
        time.sleep(0.5)
        print("===============================================================================================")
        
def game_over(player_is_dead, player_is_broke):
    if player_is_dead == True:
        print("===============================================================================================")
        display_art_gameover2()
        typewrite("\tOH NO! The player died!!!")
        print("-----------------------------------------------------------------------------------------------")
        # print out a game over screen here!
        typewrite("Your lifeless body falls to the floor.", 0.04)
        typewrite("Several onlookers scream in horror at the gruesome sight.\n", 0.05)
        time.sleep(0.5)
        typewrite("Meanwhile, the owner of the shop has no need to restock his milk.", 0.05)
        typewrite("Nobody came in to buy any today...", 0.04)
        typewrite("The fresh milk in the back of the shop starts to heat up as it's not in the shop fridges.\n", 0.05)
        time.sleep(0.5)
        typewrite("They keep on heating up...expanding the bottles.", 0.04)
        typewrite("Soon, all of the milk explodes at once, their flimsy plastic unable to expand any more.", 0.05)
        typewrite("The milk explosion blows out the wall it was next to.\n", 0.06)
        time.sleep(0.5)
        typewrite("A chunk of the rubble is hurtled in to an oncoming car.", 0.04)
        typewrite("The car swerves...it crashes in to a retirement home.", 0.08)
        typewrite("It hits and kills a man called Mikhail Dimitrescu...\n", 0.05)
        time.sleep(0.5)
        typewrite("Mikhail is...was...the father of a Russian diplomat.", 0.05)
        typewrite("Enraged by his fathers sudden and brutal death, Vadim Dimitrescu persuades Moscow to go to war.", 0.07)
        typewrite("Within weeks, the Earth is consumed by fire, the oceans boil and the mountains crumble.\n", 0.07)
        time.sleep(0.5)
        typewrite("This is the end of all things...", 0.08)
        print("===============================================================================================")

    elif player_is_broke == True:
        print("===============================================================================================")
        typewrite("\tOH NO! The player had no money to buy milk!")
        print("-----------------------------------------------------------------------------------------------")
        # print out a game over screen here!
        typewrite("As you leave the shop, with no milk in hand, the crushing weight of your failure burdens your heart.",0.05)
        typewrite("It actually hurts...\n",0.07)
        time.sleep(0.5)
        typewrite("The shame washes over you and permeates your entire being",0.04)
        typewrite("With each passing second, the feeling of emptiness only grows stronger",0.04)
        typewrite("It hurts even more now...\n",0.07)
        time.sleep(0.5)
        typewrite("Your vision flickers as you feel yourself giving up",0.04)
        typewrite("Colour drains from your sight, there is no good in the world.",0.05)
        typewrite("Why won't your chest stop hurting?\n",0.07)
        time.sleep(0.5)
        typewrite("You sink to your knees, your heart feels like it's in a jagged vice...",0.04)
        typewrite("Despair is all you know now...",0.07)
        typewrite("The pain in your chest is all you can feel...\n",0.04)
        time.sleep(0.5)
        typewrite("As you gaze up to the sky, you know it will be the last time you see it...",0.05)
        typewrite("If only you could have bought the milk...",0.07)
        typewrite("Finally, you feel no more pain. You feel nothing else...\n",0.07)
        time.sleep(0.5)
        typewrite("Your vision finally fades as you feel yourself slump over. Your last sensation before oblivion.",0.08)
        print("===============================================================================================")

        #maybe print out some game statistics here?
        
def output_dialogue_after_strong_event():
    # output dialog list for after the player chooses something
    if charList[0][6] == False:
        print("")
        typewrite("\nHey, you just beat the strongman to death! Well done!")
        typewrite("You feel pretty good. That guy looked really buff. You didn't think you'd be able to take him.")
    if charList[0][7] >= 5:
        typewrite("\nLooking down at your own hulking biceps, you wonder why you thought you couldn't.")
        time.sleep(0.2)
        typewrite("You think you could fight a building and win, based on the sheer amount of muscle on you.")
        print("")
    elif charList[0][7] == 3:
        typewrite("\nLooking down at your own normal sized arms, you thank whatever forces control your luck that you won.")
        time.sleep(0.2)
        typewrite("You think you may not be so lucky next time however...")
        print("")
    else:
        typewrite("\nLooking down at your own toothpick sized arms, you tremble at the idea of taking a light slap.")
        time.sleep(0.2)
        typewrite("You think you'll buy a lottery ticket as well as milk. It's clearly your lucky day!")

    time.sleep(0.5)
    typewrite("\nPutting those thoughts aside, you carry on to the shop.", 0.025)
    typewrite("Feeling pleased with yourself, you feel like taking a shortcut.", 0.025)
    typewrite("So instead of taking the winding path to the shop, you decide to walk in a straight line.", 0.04)
    typewrite("Walking through a field first, a hedge blocks your path.", 0.025)
    time.sleep(0.5)
    typewrite("\nYou laugh at the hedge and it's audacity. How dare it block your path...", 0.04)
    typewrite("With a heavy swing, you punch the ground where the hedges roots are.", 0.025)
    typewrite("The ground explodes from the force of your arms and the hedge is obliterated.", 0.025)
    time.sleep(0.5)
    typewrite("\nYou can almost taste that milk. It calls to you from afar...", 0.025)
    time.sleep(0.5)
    typewrite("\nAfter walking through a fence, a house now blocks your path. You COULD walk around it...", 0.04)
    typewrite("But no. You will not be stopped by mere bricks and mortar.", 0.025)
    typewrite("You punch the first wall you come to and the house disintegrates as every chunk is blasted over the horizon.", 0.04)
    time.sleep(0.5)
    typewrite("\nFinally, you see it!", 0.025)
    typewrite("The shop is before you and you still have the money in your pocket.", 0.04)
    typewrite("You buy a pint of second hand UHT semi skimmed milk (and a lottery ticket). There is no alternative.", 0.025)
    
def output_dialogue_after_smart_event():
    # output dialog list for after the player chooses something
    if charList[0][6] == False:
        print("")
        typewrite("Hey, you just outsmart the strongman! Well done!")
        typewrite("The BRAIN has outdone the MUSCLE!")
        time.sleep(0.5)
        print("")
        typewrite("Adrenaline levels are through the roof and the confidence is sky high after outsmarting the steroid junkie.", 0.03)
        typewrite("The final destination is in sight, you tread on towards to grocery store for the WHITE STUFF.", 0.03)
        typewrite(str(print_green("Green")) + " , " + str(print_blue("Blue")) + " or " + str(print_red("Red")) + " top... I think its going to be a full fat " + str(print_blue("Blue")), 0.03)
        print("")
        game_won()

def output_dialogue_after_speed_event():
    # output dialog list for after the player chooses something
    if charList[0][6] == False:
        print("")
        typewrite("Hey, you just beat the strongman using Speed to escape! Well done!", 0.03)
        time.sleep(0.5)
        typewrite("You hastally continue. ", 0.02)
        time.sleep(1.5)
        typewrite("In a blink of an eye, you parkour over walls and fences.", 0.02)
        time.sleep(0.4)
        typewrite("Moving as quick as a car, you race over a field leaping over hedges.", 0.015)
        time.sleep(0.5)
        typewrite("You move fast. So Fast. Too Fast. You Are A Blur!", 0.01)
        time.sleep(1.5)
        typewrite("Arriving at the shop...", 0.03)
        typewrite("You buy a pint of second hand UHT semi skimmed milk (and a lottery ticket). There is no alternative.",0.025)
        time.sleep(0.5)        
        print("")
        game_won()

def display_credits():
    print("\nThanks for playing!")
    print("'got milk?' By [MILKteam]")
    print("\tAnthony")
    print("\tBasil")
    print("\tDave")
    print("\tMohammad\n")
    
def intro():
    display_art_intro()
    print()
    time.sleep(1.5)
    output_intro_dialogue()
    print()
    generate_player_name()
    time.sleep(0.5)
    randomize_player_age()
    choose_character()
    print()
    output_intro_dialogue_after_name()

def start_game():    
    intro()
    output_choices()
    display_art_milk()
    display_credits()
    print("To quit, press Enter. Or type anything, then press enter to play again!")
    restartInput = input()
    if restartInput == "":
        print("Bye!")
    else:
        start_game()

start_game()