file = open("input.txt", 'r')
file = file.read()
monkeyz = file.split("\n\n")

import math
def remove_empty(test_list):
    test_list = list(map(str.strip, test_list))
    while("" in test_list):
        test_list.remove("")
    while ("\n" in test_list):
        test_list.remove("\n")
    return test_list


class Monkey():
    def __init__(self):
        self.id = ''
        self.operation = ''
        self.items = []
        self.test = {}
        self.test_true = ""
        self.test_false = ""
    def set_attr(self, key, value):
        setattr(self, key,value)

    def inspect_next(self):
        inspect_counter[self.id]+=1
        self.current_item = self.items.pop(0)
        worry_lvl = self.current_item
        worry_lvl = self.generate_equation(worry_lvl)
        self.new_worry_lvl = eval(worry_lvl)
        print(f'Worry level modified by {worry_lvl} to {self.new_worry_lvl}.')

    def test_item(self):
        divided_worry_lvl = math.floor(self.new_worry_lvl%lkkt)
        # divided_worry_lvl = math.ceil(self.new_worry_lvl/self.test)
        if divided_worry_lvl%self.test==0:
            target_monkey = self.test_true
        else:
            target_monkey = self.test_false
        print(f'Monkey gets bored with item. Worry level is divided by 3 to {divided_worry_lvl}.')
        return target_monkey, divided_worry_lvl

    def generate_equation(self,old,new='new'):
        eqa = self.operation.replace('old',str(old)).replace('new',str(new))
        return eqa

monkeys = []

def get_monkey_attr(monkey):
    m = Monkey()
    for attr in monkey:
        row = remove_empty(attr.split(" "))
        key = row[0].lower().replace(":", "")
        if key == 'monkey':
            key = 'id'
            value = int(row[1].replace(":", ""))
        elif key == 'starting':
            key = 'items'
            value = [int(x.replace(",", "")) for x in row[2:]]
        elif key == 'test':
            if row[1] == 'divisible':
                value = int(row[-1])
        elif key == 'if':
            key = row[1].replace(':','')
            if key== 'true':
                key = 'test_true'
                value = int(row[-1])
            elif key == 'false':
                key = 'test_false'
                value = int(row[-1])
        if key == 'operation':
            value = f"{row[3]}{row[4]}{row[5]}"
        m.set_attr(key, value)

    return m
for monkey in monkeyz:
    monkey = remove_empty(monkey.split("\n"))
    monkeys.append(get_monkey_attr(monkey))
del monkey, monkeyz

lkkt = math.prod(monkey.test for monkey in monkeys)

inspect_counter = {id:0 for id in range(len(monkeys))}

monkey_cnt = len(monkeys)
rounds = 10000
for i in range(monkey_cnt*rounds):
    monkey_id = i % monkey_cnt
    while len(monkeys[monkey_id].items)>0:
        # print(i,"inspecting:",monkey_id)
        monkeys[monkey_id].inspect_next()
        target_monkey, worry_lvl = monkeys[monkey_id].test_item()
        print(f"Item with worry level {worry_lvl} is thrown to monkey {3}")
        monkeys[target_monkey].items.append(worry_lvl)
print(rounds, inspect_counter.values())



inspect_counter = {k: v for k, v in sorted(inspect_counter.items(), key=lambda item: item[1],reverse=True)}
monkey_biznis_list = list(inspect_counter.values())[0:2]
monkey_biznis = 1
for a in monkey_biznis_list:
    monkey_biznis*=a
print(monkey_biznis)
print()
