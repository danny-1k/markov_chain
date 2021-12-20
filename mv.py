import numpy as np

actions = ['a','b','c','d']

transition_names = [[f'{i}{j}' for j in actions] for i in actions]

# print('\n'.join([' '.join(i) for i in transition_names]))

trans_probs = [
    [.01, .33,.33,.33],
    [.97, .01,.01,.01],
    [.97, .01,.01,.01],
    [.95 , .01,.01,.03]
]

assert sum([sum(trans_probs[i]) for i in range(len(actions))]) == len(actions), 'All rows of transition matrix should sum up to 1'


def forcast(num_iters,start='S',print_res=True):
    if print_res:
        print('\n')
        print('Starting with :',start)
    current = start

    action_list = [start]

    prob = 1

    for i in range(num_iters):
        transition = np.random.choice(transition_names[actions.index(current)],p=trans_probs[actions.index(current)])
        action_list.append(transition[1])
        
        current = transition[1]

        prob *= trans_probs[actions.index(transition[0])][actions.index(transition[1])]

    if print_res:
        print('actions taken :','->'.join(action_list))
        print('Probability of this sequence of actions :',prob)

    else:
        return action_list

forcast(2,'d')

print('\n\n')

start = 'a'
end = 'd'
num_runs = 10000
num_iters = 3

gens = []

count = 0

for i in range(num_runs):
    if forcast(num_iters,start,False)[-1] == end:
        count+=1

print(f'probability of starting with `{start}` and ending in `{end}` over the course of {num_iters} iters is ~ {(count/num_runs)*100:.0f}%')

print('\n')