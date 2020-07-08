import numpy as np
import random
from IPython.display import clear_output

# Constants
starting_money = 15000
board_size = 39
go_amount = 2000
dice_num = 2
chance_deck_size = 4
chest_deck_size = 15

emp_str = '      '
com_str = ' com  '
# Cards class
class card_action:
    def __init__(self, serial, text, money_add_amount, location_move_size, location_set_idc, location_set_dest, jail_idc, get_out_of_jail_idc, house_idc):
        self.serial = serial
        self.text = text
        self.money_add_amount = money_add_amount
        self.location_move_size = location_move_size
        self.location_set_idc = location_set_idc
        self.location_set_dest = location_set_dest
        self.jail_idc = jail_idc
        self.get_out_of_jail_idc = get_out_of_jail_idc
        self.house_idc = house_idc


# Chance_card_db
chance_card_deck = []
#                    serial                         text                                     money_add_amount, location_move_size, location_set_idc, location_set_dest, jail_idc, get_out_of_jail_idc, house_idc):
chance_0 = card_action (0,                    "Advance to Go",                                      0,                  0,               True,                0,          False,       False,            False)
chance_1 = card_action (1,    "Advance to Illinois Ave. If you pass Go, collect $200",              0,                  0,               True,               24,          False,       False,            False)
chance_2 = card_action (2, "Advance to St. Charles Place. If you pass Go, collect $200.",           0,                  0,               True,               11,          False,       False,            False)
chance_3 = card_action (3,              "Bank pays you dividend of $50",                           50,                  0,              False,                0,          False,       False,            False)

# Community_chest_card_db
chest_card_deck = []
#                    serial                         text                                     money_add_amount, location_move_size, location_set_idc, location_set_dest, jail_idc, get_out_of_jail_idc, house_idc):
chest_0 = card_action(0,                       "Advance to Go",                                     0,                  0,               True,                0,          False,       False,            False)
chest_1 = card_action(1,              "Bank error in your favor, collect 200$",                    200,                 0,              False,                0,          False,       False,            False)
chest_2 = card_action(2,                    "Doctor's fees. Pay $50",                              -50,                 0,              False,                0,          False,       False,            False)
chest_3 = card_action(3,               "From sale of stock you get $50",                           50,                  0,              False,                0,          False,       False,            False)
chest_4 = card_action(4,             "Holiday Fund matures. Receive $100",                         100,                 0,              False,                0,          False,       False,            False)
chest_5 = card_action(5,               "Income tax refund. Collect $20",                           20,                  0,              False,                0,          False,       False,            False)
chest_6 = card_action(6,            "Life insurance matures – Collect $100",                       100,                 0,              False,                0,          False,       False,            False)
chest_7 = card_action(7,                   "Hospital Fees. Pay $50",                               -50,                 0,              False,                0,          False,       False,            False)
chest_8 = card_action(8,                    "School fees. Pay $50",                                -50,                 0,              False,                0,          False,       False,            False)
chest_9 = card_action(9,                "Receive $25 consultancy fee",                             25,                  0,              False,                0,          False,       False,            False)
chest_10 = card_action(10,  "You have won second prize in a beauty contest. Collect $10",          10,                  0,              False,                0,          False,       False,            False)
chest_11 = card_action(11,                   "You inherit $100",                                   100,                 0,              False,                0,          False,       False,            False)
chest_12 = card_action(12,                 "Get Out of Jail Free",                                  0,                  0,              False,                0,          False,        True,            False) 
chest_13 = card_action(13,"Go to Jail. Go directly to jail. Do not pass Go, Do not collect $200",   0,                  0,              False,                0,           True,       False,            False)
chest_14 = card_action(14,   "Street repairs: Pay $40 per house and $115 per hotel you own",        0,                  0,              False,                0,          False,       False,             True) 
# chest_15 = card_action(15, "Grand Opera Night. Collect $50 from every player for opening night seats", ??) 
# chest_16 = card_action(16, "It is your birthday. Collect $10 from every player", ??)



# Properties_db
# count: brown 2, teal 3, purple 3, orange 3, red 3, yellow 3 green 3 blue 2
#              0    1               2                 3       4      5      6     7      8     9     10    1
#              #  color            name              type    cost  house  Rent  Rent1  Rent2 Rent3 Rent4 Rent5
property_lst=[[0, "None",          "Go",             "go"   , 0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [1, "brown", "Mediterranean Avenue", "street", 60,    50,     2,   10,    30,   90,   160,  250], \
              [2, "None",    "Community Chest",     "chest",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [3, "brown",    "Baltic Avenue",     "street", 60,    50,     4,   20,    60,   180,  320,  450], \
              [4, "None",      "Income Tax",          "tax",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [5, "None",    "Reading Railroad",     "rail", 200,    0,     0 ,   0,     0,    0,    0,    0 ], \
              [6, "teal",     "Oriental Avenue",   "street", 100,   50,     6,   30,    90,   270,  400,  550], \
              [7, "None",        "Chance!",        "chance",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [8, "teal",     "Vermont Avenue",    "street", 100,   50,     6,   30,    90,   270,  400,  550], \
              [9, "teal",   "Connecticut Avenue",  "street", 120,   50,     8,   40,   100,   300,  450,  600], \
              [10, "None",        "Jail",            "jail",  0,     0,     0,    0,     0,    0,    0,    0 ], \
              [11, "purple", "St. Charles Place",  "street", 140,  100,    10,   50,   150,   450,  625,  750], \
              [12, "None",   "Electric Company",   "utlity", 150,    0,     0 ,   0,     0,    0,    0,    0 ], \
              [13, "purple",  "States Avenue",     "street", 140,  100,    10,   50,   150,   450,  625,  750], \
              [14, "purple", "Virginia Avenue",    "street", 160,  100,    12,   60,   180,   500,  700,  900], \
              [15, "None", "Pennsylvania Railroad",  "rail", 200,    0,     0 ,   0,     0,    0,    0,    0 ], \
              [16, "orange", "St. James Place",    "street", 180,  100,    14,   70,   200,   550,  750,  950], \
              [17, "None",    "Community Chest",    "chest",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [18, "orange", "Tennessee Avenue",   "street", 180,  100,    14,   70,   200,   550,  750,  950], \
              [19, "orange", "New York Avenue",    "street", 200,  100,    16,   80,   220,   600,  800, 1000], \
              [20, "None",      "Free parking",      "park",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [21, "red",    "Kentucky Avenue",    "street", 220,  150,    18,   90,   250,   700,  875, 1050], \
              [22, "None",       "Chance!",        "chance",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [23, "red",    "Indiana Avenue",     "street", 220,  150,    18,   90,   250,   700,  875, 1050], \
              [24, "red",    "Illinois Avenue",    "street", 240,  150,    20,  100,   300,   725,  900, 1100], \
              [25, "None",     "B.&O. Railroad",     "rail", 200,    0,     0 ,   0,     0,    0,    0,    0 ], \
              [26, "yellow", "Atlantic Avenue",    "street", 260,  150,    22,  110,   330,   800,  975, 1150], \
              [27, "yellow",  "Ventnor Avenue",    "street", 260,  150,    22,  110,   330,   800,  975, 1150], \
              [28, "None",      "Water Works",     "utlity", 150,    0,     0 ,   0,     0,    0,    0,    0 ], \
              [29, "yellow",  "Marvin Gardens",    "street", 280,  150,    24,  120,   360,   850, 1025, 1200], \
              [30, "None",     "Go to Jail",    "goto_jail",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [31, "green",   "Pacific Avenue",    "street", 300,  200,    26,  130,   390,   900, 1100, 1275], \
              [32, "green","North Carolina Avenue","street", 300,  200,    26,  130,   390,   900, 1100, 1275], \
              [33, "None",    "Community Chest",    "chest",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [34, "green", "Pennsylvania Avenue", "street", 320,  200,    28,  150,   450,  1000, 1200, 1400], \
              [35, "None",   "Short Line Railroad",  "rail", 200,    0,     0 ,   0,     0,    0,    0,    0 ], \
              [36, "None",        "Chance!",       "chance",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [37, "blue",      "Park Place",      "street", 350,  200,    35,  175,   500,  1100, 1300, 1500], \
              [38, "None",      "Luxary Tax",         "lux",  0,     0,     0 ,   0,     0,    0,    0,    0 ], \
              [39, "blue",      "Boardwalk",       "street", 400,  200,    50,  200,   600,  1400, 1700, 2000], \
             ]
# Gameplay functions

def buying_conformation (marker, money, cost):
  if cost > money:
    print ('Too bad, {} can not afford this\n'.format(marker))
    return False
  buy = take_response('{} have {}. This property costs {}. Would {} would like to buy it?\n'.format(marker, money, cost, marker), marker)
  if buy in 'Yy':
    return True
  return False

def paying_calculation (property_lst, num_house, num_hotel, location):
  return property_lst[location][num_house+num_hotel+6]

def roll_dice (num_dice):
    return [random.randint(1, 6) for i in range(num_dice)]

def take_response (sentence, marker):
  if marker == com_str:
    print(sentence)
    print("{} choose to take the action!".format(marker))
    return 'Y'
  else:
    res = input(sentence)
    return res

def shuffle_deck (deck_type):
  if deck_type == 'chance':
    lst = list(range(chance_deck_size))
  else:
    lst = list(range(chest_deck_size))
  random.shuffle(lst) 
  return lst

# Graphics functions

def middle_line (width, middle_char = ' '):   # Assume len(middle_char)+2 < width 
  len2 = len(middle_char)//2
  if (len(middle_char) % 2 == 0):
    return '|'+(''.join([' ' for i in range(width//2-1-len2)]))+middle_char+(''.join([' ' for i in range(width//2-len2)]))+'|' 
  else:  # (len(middle_char) % 2 == 1):  odd number 
    return '|'+(''.join([' ' for i in range(width//2-1-len2)]))+middle_char+(''.join([' ' for i in range(width//2-1-len2)]))+'|' 

def rect (height, width, middle_char = ' '):  # both higher than 5 and odd
  first_line = ''.join(['_' for i in range(width)])
  last_line = ''.join(['\u0305 ' for i in range(width)])
  phase = '|'+(''.join([' ' for i in range(width-2)]))+'|'
  rectan = first_line+'\n'+ \
           '\n'.join([phase for i in range(height//2)])+ \
           '\n'+ \
           middle_line(width, middle_char)+  \
           '\n'+ \
           '\n'.join([phase for i in range(height//2)])+ \
           '\n'+last_line

  return rectan

def create_header (sentence):
  if (len(sentence) % 2 == 0):
    return rect(1,len(sentence)+5,sentence)
  else:
    return rect(1,len(sentence)+4,sentence)

def join_vert_with_frame (obj_iter):
  count_lines = [obj.count('\n') for obj in obj_iter]
  num_rows = 5 + 2*(sum(count_lines)//2)
  
  count_cols = [len(obj.split('\n')[0]) for obj in obj_iter]
  num_cols = 5 + 2*(max(count_cols)//2)
  
  first_line = ''.join(['_' for i in range(num_cols)])
  last_line = ''.join(['\u0305 ' for i in range(num_cols)])
  
  lines_lst = [obj.split('\n') for obj in obj_iter]
  lines = []
  for i in range(len(lines_lst)):
    for line in lines_lst[i][:-1]:
      lines.append(line)
  
  shape = [middle_line (num_cols,str(line)) for line in lines]
  return first_line+'\n'+'\n'.join(shape)+'\n'+last_line

def prop_card (sentences):
  limit_char = 6
  return join_vert_with_frame([create_header(sentence[:limit_char]) for sentence in sentences])

def join_horz (obj_iter):
  count_cols = [obj.count('\n') for obj in obj_iter]
  num_cols = 5 + 2*(sum(count_cols)//2)
  lines_lst = [obj.split('\n') for obj in obj_iter]
  numpy_array = np.array(lines_lst)
  transpose = numpy_array.T
  lines = transpose.tolist()
  shape = [middle_line (num_cols,'|'.join(line)) for line in lines]
  return shape[0].replace('|','_')+'\n'+'\n'.join(shape[1:-1])+'\n'+shape[-1].replace('|','\u0305 ')

def create_prop_card (prop):
    return prop_card([str(prop[0]), prop[2], prop[3]])

def create_game_board (property_trk):
  upper_frame = join_horz([create_prop_card(property_trk[i]) for i in range(20,31)])
  lower_frame = join_horz([create_prop_card(property_trk[i]) for i in range(10,-1,-1)])

  space_line = ''.join([' ' for i in range(34,len(lower_frame.split('\n')[0]))])
  space = '\n'.join([space_line for i in range(1+lower_frame.count('\n'))])
  
  shape_lines = [join_horz([create_prop_card(property_trk[19-i]), space, create_prop_card(property_trk[31+i])]) for i in range (9)]
  shape = '\n'.join(shape_lines)
  
  return upper_frame+'\n'+shape+'\n'+lower_frame

def create_player_sts (property_trk, player):
  player_sts1 = '               {}                 \n    Money: {}       \nLocation: {} - {}\n        Properties:        \n'.format(player.marker, player.money, player.location,property_trk[player.location][6]) 
  player_sts2 = '\n'.join([prop[6] for prop in property_trk if prop[2] == player.marker])
  return join_vert_with_frame([player_sts1+player_sts2])

# Player class
class player_type:                                                                                              
  def __init__(self, marker, player_order, computer = False, action = 1, money = starting_money, location = 0, number_of_houses = 0, number_of_hotels = 0, in_jail = False, free_out_jail_card = False):
        self.marker = marker
        self.player_order = player_order
        self.computer = computer
        self.action = action
        self.money = money
        self.location = location
        self.number_of_houses = number_of_houses
        self.number_of_hotels = number_of_hotels
        self.in_jail = in_jail
        self.free_out_jail_card = free_out_jail_card
  
  def go_to_jail (self):
    print('Go to jail!')
    self.location = 10
    self.in_jail = True  

  def jail_card_check(self):
    if self.in_jail == True:
      print('{} is in jail!\n'.format(self.marker))
      if self.free_out_jail_card > 0:            # Checks if player has get out of jail free card
        use_card = take_response('Do you want to use your "Get out of jail free" card? Enter Y for Yes or N for No', self.marker)
        if use_card in 'Yy':                                   # if player choose to use the card
          self.free_out_jail_card -= 1
          self.get_out_jail()

  def get_out_jail (self):
    print ('You got out of jail!')
    self.in_jail = False 
    
  def move_player (self, step_size):
    new_loc = self.location + step_size
    if new_loc > board_size:   # player passed go
      self.location = new_loc - board_size
      self.money += go_amount
    if new_loc == board_size:   # player landed on go
      self.location = 0
      self.money += 2*go_amount
    if new_loc < board_size:
      self.location = new_loc

  def take_lux_action (self):
    player.money -= 100
  
  def take_tax_action (self):
    player.money -= 200
  
  def take_park_action (self):
    player.action -= 2

  def take_card_action (self, card):
    print (card.text)
    player.money += card.money_add_amount
    player.location += card.location_move_size
    if card.location_set_idc:
      if card.location_set_dest < player.location:
        player.money += go_amount
      player.location = card.location_set_dest
    if card.jail_idc:
      player.go_to_jail()
    if card.get_out_of_jail_idc:
      player.get_out_of_jail_idc += 1
    if card.house_idc:
      player.money -= 40*player.number_of_houses + 110*player.number_of_hotels

# Game trackers

action_dic = {'lux': 'take_lux_action',    
              'tax': 'take_tax_action',   
              'park': 'take_park_action',   
              'chest': 'take_card_action',    
              'chance': 'take_card_action',   
              }
#                 0        1          2         3         4         5         6
#                 #       type      owner     occup     #house    #hotel     name
property_trk = [[prop[0], prop[3], emp_str,  emp_str,       0,        0,    prop[2]] for prop in property_lst]

# Players settings
player1_marker = '  P1 '
player1_order = 0
player1 = player_type (player1_marker, player1_order)

# oppenent
player2_marker = com_str
player2_order = 1
player2 = player_type (player2_marker, player2_order, computer = True)

# Turn order setting
turn_counter, turn = 0 , 0
player_lst = list(sorted([player1, player2], key = lambda x: x.player_order))

# Reset locations
for player in player_lst:
  property_trk[player.location][3] = player.marker

# reset double counter
double_counter = 0

# shuffle card_decks & intiallize 
chance_card_deck = shuffle_deck ('chance')
chest_card_deck = shuffle_deck ('chest')
card = chance_0

# Print board
print (create_game_board(property_trk))

# Turn announcement
print("it's now {} turn!".format(player_lst[turn].marker))

# Turn play
play = take_response('Do you want to roll the dice? Y for yes\n' ,player_lst[turn].marker)

while play in 'Yy':
  # Clear screen
  clear_output(wait=True)
  print(create_player_sts(property_trk, player_lst[turn]))

  # Check whether player in jail and wants to use card
  player_lst[turn].jail_card_check()

  # Take action
  while player_lst[turn].action > 0:
    command_string = ''
    player_lst[turn].action -= 1
    
    # Roll dice
    dice_result = roll_dice(dice_num)
    print('{} rolled {}'.format(player_lst[turn].marker, dice_result))
    
    # Update double counter / double "get out of jail"
    if len(set(dice_result)) <= 1:
      double_counter += 1
      if player_lst[turn].in_jail == True:
        player_lst[turn].get_out_jail()
    else:
      double_counter = 0
    
    # if player didn't get out of jail
    if player_lst[turn].in_jail == True:
      print('{} did not make it out of jail\n'.format(player_lst[turn].marker)) 

    # check for 3 times double
    if double_counter == 3:
      print('3 doubles in a row!')
      player_lst[turn].go_to_jail()
    
    # Advance player
    if player_lst[turn].in_jail == False:
      property_trk[player_lst[turn].location][3] = emp_str
      player_lst[turn].move_player(sum(dice_result))
      property_trk[player_lst[turn].location][3] = player_lst[turn].marker
      print('{} landed on: {} - {}'.format(player_lst[turn].marker, player_lst[turn].location, property_trk[player_lst[turn].location][1]))

      # Jail action
      if property_trk[player_lst[turn].location][1] in 'goto_jail':
        player_lst[turn].go_to_jail()
      
      # Tax/luxary tax/free parking actions
      if property_trk[player_lst[turn].location][1] in 'tax_lux_park':
        command_string = 'player_lst[turn].'+action_dic[property_trk[player_lst[turn].location][1]]+'()'
      
      # Community chest/chane actions
      if property_trk[player_lst[turn].location][1] in 'chest_chance':
        deck_string = property_trk[player_lst[turn].location][1]+'_card_deck'
        card_number = eval(deck_string+'.pop(0)')
        card = eval(property_trk[player_lst[turn].location][1]+'_'+str(card_number))
        if eval(deck_string) == []:
          eval(deck_string+' = shuffle_deck ("'+[property_trk[player_lst[turn].location][1]]+'")')
        command_string = 'player_lst[turn].'+action_dic[property_trk[player_lst[turn].location][1]]+'(card)'
      
      if command_string:
        eval(command_string)
      
      # Property can be bought
      if property_trk[player_lst[turn].location][1] in 'rail_utlity_street':
        
        # Property is vacant
        if (property_trk[player_lst[turn].location][2] == emp_str):
          buy = buying_conformation (player_lst[turn].marker, player_lst[turn].money, property_lst[player_lst[turn].location][4])
          if buy:
            print('{} bought this property'.format(player_lst[turn].marker))
            property_trk[player_lst[turn].location][2] = player_lst[turn].marker
            player_lst[turn].money -= property_lst[player_lst[turn].location][4]
        
        # Property isn't vacant
        if (property_trk[player_lst[turn].location][2] != emp_str) and (property_trk[player_lst[turn].location][2] != player_lst[turn].marker):
          owner = property_trk[player_lst[turn].location][2]
          # Payment calculation
          if property_trk[player_lst[turn].location][1] in 'street':
            pay = paying_calculation (property_lst, property_trk[player_lst[turn].location][4], property_trk[player_lst[turn].location][5], player_lst[turn].location)
          if property_trk[player_lst[turn].location][1] in 'rail':
            rail_owners = [prop[2] for prop in property_trk if prop[1] in 'rail']
            pay = property_lst[player_lst[turn].location][6] * rail_owners.count(owner)
          if property_trk[player_lst[turn].location][1] in 'utlity':
            utlity_owners = [prop[2] for prop in property_trk if prop[1] in 'utlity']
            pay = sum(dice_result)*(6*utlity_owners.count(owner)-2)
          # Actual payment
          if player_lst[turn].money >= pay:
            print('{} paid {} to {}'.format(player_lst[turn].marker, pay, owner))
            player_lst[turn].money -= pay
            for player in player_lst:
              if player.marker == owner:
                player.money += pay
          else:
            print('{} can not pay and lost the game!'.format(player_lst[turn].marker)) 

  # Print board
  # print (create_game_board(property_trk))

  # End of turn
  player_lst[turn].action +=1
  turn_counter += 1
  # Promot another turn
  turn = turn_counter % len(player_lst)
  play = input('Do you want to roll the dice? Y for yes\n')
