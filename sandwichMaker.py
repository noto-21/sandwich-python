import pyinputplus as pyip

menu_items = {'Bread': {'Wheat': 0.30, 'White': 0.25, 'Sourdough': 0.25, 'Rye': 0.40},
              'Meat': {'Chicken': 0.65, 'Turkey': 0.65, 'Ham': 0.70, 'Tofu': 0.60, 'Beef': 0.85},
              'Cheese': {'Cheddar': 0.12, 'Swiss': 0.15, 'Mozzarella': 0.17, 'White Cheddar': 0.12},
              'Toppings': {'Mayo': 0.10, 'Mustard': 0.10, 'Lettuce': 0.15, 'Tomato': 0.15}}

cost = 0


def prompt_generator(menu, item_order):
    prompt = ('please select %s:\n(' % list(menu.keys())[item_order]).title()
    for k, v in menu[list(menu.keys())[item_order]].items():
        prompt += f'{k}->${v:.2f}, '.title()
    prompt += '\b\b)\n'
    return prompt


breadC = pyip.inputMenu(choices=list(menu_items[list(menu_items.keys())[0]].keys()),
                        prompt=prompt_generator(menu_items, 0))
meatC = pyip.inputMenu(choices=list(menu_items[list(menu_items.keys())[1]].keys()),
                       prompt=prompt_generator(menu_items, 1))
cheese_yn = pyip.inputYesNo(prompt='Add %s? (extra $): ' % list(menu_items.keys())[2].title())
if cheese_yn == 'yes':
    cheeseC = pyip.inputMenu(choices=list(menu_items[list(menu_items.keys())[2]].keys()),
                             prompt=prompt_generator(menu_items, 2))
else:
    menu_items[list(menu_items.keys())[2]].setdefault(cheese_yn, 0)
    cheeseC = cheese_yn

for top, price in menu_items['Toppings'].items():
    yn = pyip.inputYesNo(prompt=f'Add {top}? (${price:.2f} extra): ')
    if yn == 'yes':
        cost += price

cost += (menu_items[list(menu_items.keys())[0]][breadC] +
         menu_items[list(menu_items.keys())[1]][meatC] +
         menu_items[list(menu_items.keys())[2]][cheeseC])

amount = pyip.inputInt(prompt='\nHow many?: x', min=1)

print(f'\nSubtotal - ${cost * amount:.2f}')
print(f'Tax - ${0.13 * (cost * amount):.2f} ($0.13/dollar)')
print(f'Total - ${(cost * amount) * 1.13:.2f}')
