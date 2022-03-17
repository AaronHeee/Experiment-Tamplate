import torch
import random
import numpy as np

def random_seed(seed=None):
    if seed is None:
        seed = torch.initial_seed() % 2**32
    torch.use_deterministic_algorithms(True)
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    return seed
    
def last_commit_msg():
    from subprocess import check_output
    hashed_id = check_output('git log -1 --pretty=format:"%H"'.split()).decode('utf-8').rstrip('\n').replace('\n', '').replace('\"', '')[:8]
    msg_short = '_'.join(check_output('git log -1 --pretty=format:"%B"'.split()).decode('utf-8').strip('\n').replace('\n', '').replace('\"', '').split(' '))
    return f"{msg_short}_{hashed_id}"
