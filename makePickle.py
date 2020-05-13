from ClassEmployee import Employee as emp, Point

emp1 = emp("Zara", 2000)
emp1.displayEmployee()

import pickle
pickle.dump( emp1, open( "./emp1.pkl", "wb" ) )
print('dump pickle')
emp1_pkl = pickle.load( open( "./emp1.pkl", "rb" ) )
print('load pickle')
emp1_pkl.displayEmployee()