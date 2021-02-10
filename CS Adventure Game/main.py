import time 

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

chocolate = 0
weapon = 0
flashlight = 0
mirror = 0

name = input("What is your name?")
print('Hi, %s.' % name, 'welcome to your very first mystery')

required = ("\nUse only A, B, C, D\n")

print("You're in the center of an urban outlook, when you hear a beeping in the distance. The people nearby run, but you're too stunned to comprehend. Why are people running?")
print("You ask a store vendor, who claims there's an eerie figure that has been spotted in the city's Central Park.")
time.sleep(3)
print("An agent behind you taps your shoulder and gives you a sticky note. You look down, and see coordinates. When you look back up, he's gone.")
time.sleep(3)
print('You notice that the vendor is gone too, and that the store has changed. You see advanced mechanisms, like those in science fiction movies, but something cathes your eye. On the left, you see a board labeled with your name in bold')
time.sleep(3)
print('You have an inventory, type one of the keys to obtain an iten. REMEMBER you can only choose one. You will:')
time.sleep(3)
print(""" A. Grab the flashlight, 
  B. Grab the chocolate, 
  C. Grab the mirror, 
  or D. Grab the weapon""")

choice = input("> ")

if choice in answer_A:
  def option_flashlight():
     
     print("\nYou have vetured into the depths of the park. You hear nothing, not even the strange beeping")
  time.sleep(3)
  print("You hear a stick snap. There's someone in the midst")
  flashlight = input("Do you want to explore, or not. Click keys y or n to answer.")
  if flashlight in no:
    print("You run out of the forest. The board of detectives thanks you for your valiance. However, you have not finished solving the mystery, and the haunted figure is still in the midst")
    exit()
  if flashlight in yes:
    print("You shine your flashlight around, and see a hooded figure tying some ropes. Thankfully he/she doesn't feel the light and continues doing their thing.")
    time.sleep(3)
    choice2 = input("You go back to your inventory, sensing trouble. You get to choose another item. You only find chocolate and take it. Please click c on your keyboard to continue.")
    if choice2 in answer_C:
      print("You go back into the forest, and your flashlight's batteries die out. You are left in the darkness with nothing but your chocolate bar. You feel as though all hope is lost. You chomp on your chocolate depressed, when suddenly you bit on something hard. A battery! Food is always the key to your success!! >:)")
      time.sleep(3)
      batteries = input("You reload your flashlight's batteries. You cling onto your backpack, which is heavy. Would you like to (a)drop the batteries here to avoid put on more weight, or (b) take the batteries with you anyways?")
      
      if batteries in answer_A:
        print("As the batteries fall, you hear a distant screech. Someone has found you. You frantically reach for your chocolate bar, as it is your only weapon. You see it melted and liquidified in your backpack. You're doomed.")
        time.sleep(3)
        print("Now, coming to think of it, why did you have to drop the batteries? They're roughly 25 grams at most. The board of detectives thanks you for your valiance. However,you have failed and are not worthy of becoming a detective due to your irrational decisions. So long, warrior!")
        exit()
      if batteries in answer_B:
        print("You have made the right choice. You don't feel a difference as you put the used batteries in your backpack. It's time for a victory! You reach for your chocolate, but it's melted by now. You are back to square one, with a flashlight and a heavy backpack. What are you going to do?")
        time.sleep(3)
        print("A figure senses your presence, and you hear a rapid beeping. Someone grabs your arm and pulls you. You scream. A rather squeaky voice says you won;t be heard from afar. You finally decide to open your eyes. You spot a metal detector in the man's hands. The batteries! They're made out of metal and alloys. You realize that it's come down to your final minutes, all because you chose chocolate with some batteries.")
        time.sleep(3)
        print("The squeaky man pulls off his hood, and you see an old man. AN OLD MAN HAUNTING THE FOREST?! He gives you a cup of tea, with a strong smell of hazelnut. You can't resist and take a sip. *literal heaven* He tells you his tale.")
        time.sleep(3)
        print("You find out that this old geezer is an inventor and the keeper of this forest. He was trapped here after he swore an oath to people in the nearby village to protect the forest. As the generations went on, the pact was getting broken. The trees were getting cut down for industry. His home was getting destroyed. To scare them off, the inventor created a hologram of himself in a hood. Stories from Grandpas and some hazelnut tea,don't mind if I do, but this tale was not to your taste. A genius inventor trapped in a forest? Something is fishy here, and it throws you off. This mystery was silly, there's something bigger at hand. However, you have successfully fulfilled your duty, and the board of detectives is impressed with your excellency. You tell the people of this man, and they reluctantly agree to let the guy live normally in a village abode.")


elif choice in answer_B:
  print("Really?! Food?")
  def option_chocolate():
    print("\nWell, food is always the remedy, but seriously?! You then pick up your golden bar and set afoot in the depths of the park.")
  time.sleep(3)
  print("Just then, you freeze. You hear the beep. You are grabbed by a metal arm and are swung out of the park. You land with an umph, and have no stamina. With your last breaths, what would you like to do? Will you:")
  death = input(""" A. Take a bite out of your chocolate,
  B. die in silence, or C. Call for help """)
  if death in answer_A:
    print("You take a bite out of your chocolate and are immediately energized. Still stunned, you head back into the forest. This chocolate is magical.")
    time.sleep(3)
    print("You come back into the park, expecting the wacko metal arm to swing back, but it doesn't. In fact, it's broken and hung on a tree. You feel a hand on your shoulder.")
    time.sleep(3)
    print("Would you like to:")
    run = input("""A. run
    B. turn around""")
    if run in answer_A:
      print("You run out of the park, not knowing the solution to this strange mystery.")
      exit()
    if run in answer_B:
      print("You see an old man behind you with a kind face.He tells you his tale.")
      print("You find out that this old geezer is an inventor and the keeper of this forest. He was trapped here after he swore an oath to people in the nearby village to protect the forest. As the generations went on, the pact was getting broken. The trees were getting cut down for industry. His home was getting destroyed. To scare them off,the inventor created a hologram of himself in a hood. A genius inventor trapped in a forest? Something is fishy here, and it throws you off. This mystery was silly, there's something bigger at hand. However, you have successfully fulfilled your duty, and the board of detectives is impressed with your excellency. You tell the people of this man, and they reluctantly agree to let the guy live normally in a village abode.")
  
  if death in answer_B:
    print("RIP. You have not died in vain")
    exit()
  
  if death in answer_C:
    print("You are rushed to the hospital, but no means of remedy can cure you. You will inevitably die. So long, warrior!")

    
elif choice in answer_C:
  def option_mirror():
    print("A mirror seems like the wisest decision. When broken, you can use it as a weapon, and when pieced together, you can look at your surroundings.")
    time.sleep(3)
    print("You venture off into the depths of the park, clutching onto your mirror.")
    time.sleep(3)
    print("You hear the screeching of metal. *horror movie vibes*")
    time.sleep(1.5)
    print("Will you: ")
    mirror = input("""A. Use your mirror
    B. Run away """)
    if mirror in answer_B:
        print("Your were seconds away from solving the mystery. You have not deemed worthy.")
        exit()
    if mirror in answer_A:
        print("You see an old man. Wait hold up. AN OLD MAN IN A HOODIE HAUNTING CENTRAL PARK?! You must be seeing things. He tells you to sit down and have some tea")
        time.sleep(3)
        print("You think that this guy is one of those strange grandpas, and take a sip of what seems to be hazelnut tea. Grandpa Scary tells his tale.")
        time.sleep(3)
        print("You find out that this old geezer is an inventor and the keeper of this forest. He was trapped here after he swore an oath to people in the nearby village to protect the forest. As the generations went on, the pact was getting broken. The trees were getting cut down for industry. His home was getting destroyed. To scare them off, the inventor created a hologram of himself in a hood. Stories from Grandpas and some hazelnut tea,don't mind if I do, but this tale was not to your taste. A genius inventor trapped in a forest? Something is fishy here, and it throws you off. This mystery was silly, there's something bigger at hand. However, you have successfully fulfilled your duty, and the board of detectives is impressed with your excellency. You tell the people of this man, and they reluctantly agree to let the guy live normally in a village abode.")
        exit()
elif choice in answer_D:
  def option_weapon():
    print("You have chosen a weapon.")
    time.sleep(0.3)
    print("You head into the depths of the park, and hear the screeching of metal. Will you: ")
    weapon = input("""A. Hold you weapon,
    B. Run away""")
    if weapon in answer_A:
        print("You clutch your weapon close to your chest. Panting, you try to stand your ground. You feel a hand on your shoulder. Would you like to: ")
        hand = input("""A. Run away
        B. Turn around""")
        if hand in answer_A:
            print("You run out of the park")
            time.sleep(0.3)
            print("You have not deemed worthy, even with a weapon.")
            exit()
        if hand in answer_B:
            print("You turn around, and are relieved. It's just an old man. Wait! AN OLD MAN?!!")
            time.sleep(0.3)
            print("You listen to his tale. Here's what he says:You find out that this old geezer is an inventor and the keeper of this forest. He was trapped here after he swore an oath to people in the nearby village to protect the forest. As the generations went on, the pact was getting broken. The trees were getting cut down for industry. His home was getting destroyed. To scare them off, the inventor created a hologram of himself in a hood. Stories from Grandpas and some hazelnut tea,don't mind if I do, but this tale was not to your taste. A genius inventor trapped in a forest? Something is fishy here, and it throws you off. This mystery was silly, there's something bigger at hand. However, you have successfully fulfilled your duty, and the board of detectives is impressed with your excellency. You tell the people of this man, and they reluctantly agree to let the guy live normally in a village abode.")
            time.sleep(6)
            print("You have solved the mystery, and have deemed worthy. Good job.")
            exit()

  


  