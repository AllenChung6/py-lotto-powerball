# lotto picker by manny juan  (juanm@wellsfargo.com or manny@bdt.com)

from random import randint

def pick_lotto():
    max_lotto = 1
    lotto = []
    while max_lotto != 6:
        pick = randint(1, 69)
        lotto.append(pick)
        max_lotto += 1
    power_ball = randint(1, 26)
    lotto.append(power_ball)
    final_result = tuple(lotto)
    print(final_result)


def run():
    done = 0
    while not done:
        try:
            x = input('\npress Enter for Lotto picks (Q to quit). ')
        except EOFError:
            x = 'q'
        if x and (x[0] == 'q' or x[0] == 'Q'):
            done = 1
            print('done')
        else:
            print(pick_lotto())


# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    run()
else:
    print("Module lotto imported.")
    print("To run, type: lotto.run()")
    print("To reload after changes to the source, type: reload(lotto)")
# end of lotto.py
