import os
import sys
import random
import termtables
import wonderwords
import cst

MAX_BUY_ATTEMPTS: int = 0
MAX_VEHICLE_COST: int = 150
MIN_VEHICLE_COST: int = 120

if len(sys.argv) == 3:
    MAX_VEHICLE_COST = int(sys.argv[2])
    MIN_VEHICLE_COST = MAX_VEHICLE_COST - 20
if len(sys.argv) == 4:
    MIN_VEHICLE_COST = int(sys.argv[2])
    MAX_VEHICLE_COST = int(sys.argv[3])

armor_data: 'list[dict]' = cst.read('data/armor.csv')
frame_data: 'list[dict]' = cst.read('data/frame.csv')
engine_data: 'list[dict]' = cst.read('data/engine.csv')
wheels_data: 'list[dict]' = cst.read('data/wheels.csv')

vehicle_armor: str = ''
vehicle_frame: str = ''
vehicle_engine: str = ''
vehicle_wheels: str = ''

vehicle_hp: int = 0
vehicle_space: int = 0
vehicle_max_speed: int = 0
vehicle_traction: int = 0

vehicle_armor_description: str = ''
vehicle_frame_description: str = ''
vehicle_engine_description: str = ''
vehicle_wheels_description: str = ''

vehicle_money: int = MAX_VEHICLE_COST

# Continuously generate cars until we get one within the price limit:
while True:

    is_too_expensive: bool = False

    # Randomly choose the order of part types to buy:
    build_actions = [0, 1, 2, 3]
    random.shuffle(build_actions)

    while len(build_actions) > 0:
        build_action = build_actions.pop()

        if build_action == 0: # Buy armor.
            buy_attempts = 0
            while True:
                buy_attempts += 1
                armor = random.choice(armor_data)
                if armor['cost'] < vehicle_money:
                    vehicle_money -= armor['cost']
                    vehicle_armor = armor['name']
                    vehicle_armor_description = armor['description']
                    vehicle_hp += armor['hp_mod']
                    vehicle_space += armor['space_mod']
                    vehicle_max_speed += armor['max_speed_mod']
                    vehicle_traction += armor['traction_mod']
                    break
                if buy_attempts > MAX_BUY_ATTEMPTS:
                    is_too_expensive = True
                    break
        
        elif build_action == 1: # Buy frame.
            buy_attempts = 0
            while True:
                buy_attempts += 1
                frame = random.choice(frame_data)
                if frame['cost'] < vehicle_money:
                    vehicle_money -= frame['cost']
                    vehicle_frame = frame['name']
                    vehicle_frame_description = frame['description']
                    vehicle_hp += frame['hp_mod']
                    vehicle_space += frame['space_mod']
                    vehicle_max_speed += frame['max_speed_mod']
                    vehicle_traction += frame['traction_mod']
                    break
                if buy_attempts > MAX_BUY_ATTEMPTS:
                    is_too_expensive = True
                    break
        
        elif build_action == 2: # Buy engine.
            buy_attempts = 0
            while True:
                buy_attempts += 1
                engine = random.choice(engine_data)
                if engine['cost'] < vehicle_money:
                    vehicle_money -= engine['cost']
                    vehicle_engine = engine['name']
                    vehicle_engine_description = engine['description']
                    vehicle_hp += engine['hp_mod']
                    vehicle_space += engine['space_mod']
                    vehicle_max_speed += engine['max_speed_mod']
                    vehicle_traction += engine['traction_mod']
                    break
                if buy_attempts > MAX_BUY_ATTEMPTS:
                    is_too_expensive = True
                    break
        
        elif build_action == 3: # Buy wheels.
            buy_attempts = 0
            while True:
                buy_attempts += 1
                wheels = random.choice(wheels_data)
                if wheels['cost'] < vehicle_money:
                    vehicle_money -= wheels['cost']
                    vehicle_wheels = wheels['name']
                    vehicle_wheels_description = wheels['description']
                    vehicle_hp += wheels['hp_mod']
                    vehicle_space += wheels['space_mod']
                    vehicle_max_speed += wheels['max_speed_mod']
                    vehicle_traction += wheels['traction_mod']
                    break
                if buy_attempts > MAX_BUY_ATTEMPTS:
                    is_too_expensive = True
                    break
    
    if not is_too_expensive and vehicle_money <= (MAX_VEHICLE_COST - MIN_VEHICLE_COST):
        break
    else:
        vehicle_money = MAX_VEHICLE_COST
        vehicle_hp: int = 0
        vehicle_space: int = 0
        vehicle_max_speed: int = 0
        vehicle_traction: int = 0

# Generate a vehicle name:
word_randomizer = wonderwords.RandomWord()
name_type = random.choice([0, 1, 2])
if name_type == 0:
    vehicle_name = word_randomizer.word(include_parts_of_speech=['adjectives'])
    vehicle_name += ' ' + word_randomizer.word(include_parts_of_speech=['nouns'])
elif name_type == 1:
    vehicle_name = word_randomizer.word(include_parts_of_speech=['nouns'])
    vehicle_name += ' ' + word_randomizer.word(include_parts_of_speech=['nouns'])
elif name_type == 2:
    vehicle_name = word_randomizer.word(include_parts_of_speech=['nouns'])
    vehicle_name += ' of '
    vehicle_name += word_randomizer.word(include_parts_of_speech=['nouns'])
vehicle_name = vehicle_name.title()

# Show vehicle description:
if vehicle_armor_description != '':
    vehicle_armor_description = f' ({vehicle_armor_description})'
if vehicle_frame_description != '':
    vehicle_frame_description = f' ({vehicle_frame_description})'
if vehicle_engine_description != '':
    vehicle_engine_description = f' ({vehicle_engine_description})'
if vehicle_wheels_description != '':
    vehicle_wheels_description = f' ({vehicle_wheels_description})'

output = termtables.to_string(
    [
        [f'Name: {vehicle_name}', f'Money: {vehicle_money}'],
        [f'Armor: {vehicle_armor}', f'HP: {vehicle_hp}/{vehicle_hp}{vehicle_armor_description}'],
        [f'Frame: {vehicle_frame}', f'Space: {vehicle_space}{vehicle_frame_description}'],
        [f'Engine: {vehicle_engine}', f'Max Speed: {vehicle_max_speed}{vehicle_engine_description}'],
        [f'Wheels: {vehicle_wheels}', f'Traction: {vehicle_traction}{vehicle_wheels_description}']
    ],
    style="           ===="
)
print(output)

os.makedirs(os.path.dirname('output/'), exist_ok=True)
with open('output/vehicles.txt', 'a+') as f:
    f.write(output)
    f.write('\n\n')

# Show weapons description:
# termtables.print(
#     [
#         ['', '', '', '', '']
#     ],
#     header=['Weapon', 'Slots', 'Range', 'To Hit', 'Damage'],
#     style="           ===="
# )
