import numpy as np

from numpy.random import randn
import pandas as pd
np.random.seed(888)

# simulate imported dataframes (exp_df1 + 2) for a couple time-series files
file_names = [r'd:/str/blah/experiment1.csv', r'd:/str/blah/experiment1.csv']
exp_df1 = pd.DataFrame(1023.24+ randn(5,6),index=None,
columns=['m/z', 'DT', 'Area', 'm/z Error', 'DT Error', 'Area Error']
)

# reference dictionary
ref_dic = {
    '[HMo_7O_22]^–2':{'mz': 1023.24, 'mobility': 1023.50},
    '[MoO4(MoO3)13(D2O)3]2-':{'mz': 1023.24, 'mobility': 5}
}

# tolerance defaults: 1 a.m.u. tolerance # 5% tol.
mz_tol, mob_tol = 1, 0.05

for ion in ref_dic.keys():
    # get reference info for one ion
    target_mz = float(ref_dic[ion]['mz']) # ex: m/z of '[HMo_7O_22]^–2'
    target_dt = float(ref_dic[ion]['mobility'])
    # set tolerance range for ion:
    upperMZ, lowerMZ = target_mz+mz_tol, target_mz-mz_tol # unit m/z
    upperDT, lowerDT = target_dt*mob_tol, target_dt*(-mob_tol) # a percentage
    print(f'Checking {ion} mass range: {lowerMZ}-{upperMZ}')
    if(exp_df1['m/z'].between(lowerMZ, upperMZ, inclusive=True)):
        pass

    # check tolerance range against all m/z and dt values
    for i in range(len(exp_df1['m/z'])):
        exp_mz = exp_df1['m/z'][i] # experimental m/z
        exp_dt = exp_df1['DT'][i] # experimental dt
        exp_area = exp_df1['Area'][i] # counts for ion
        if (exp_mz < upperMZ and exp_mz > lowerMZ 
    and exp_dt < upperDT and exp_dt > lowerDT):
            print('Wahoo')
        else:
            print(f'{exp_mz} and {exp_area} not within tolerance')
 