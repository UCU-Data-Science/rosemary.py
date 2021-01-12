from kitchen.utensils.Utensil import Bowl
from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt

# Add two eggs to a bowl
bowl = Bowl.use(name='eggs')
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()

# Take a pan, make two omelettes, and add them to a plate
pan = Pan.use(name='omelette')
plate = Plate.use()
for i in range(2):
    pan.add(Butter.take('slice'))
    pan.add(bowl.take('1/2'))
    pan.add(Salt.take('dash'))
    pan.cook(minutes=2)

    omelette = pan.take()
    plate.add(omelette)

Rosemary.serve(plate)
