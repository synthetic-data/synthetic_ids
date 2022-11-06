# -*- coding: utf-8 -*-
"""...
"""
import pickle
from uuid import uuid4


a = {'246': str(uuid4())}

with open('../data/zid_sid.pickle', 'wb') as file:
    pickle.dump(a, file, protocol=pickle.HIGHEST_PROTOCOL)

with open('../data/zid_sid.pickle', 'rb') as file:
    b = pickle.load(file)

print('ok')