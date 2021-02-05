import pandas as pd
import numpy as np


def collect_dupe_strains(filename):
    index = 0
    strain_name = []
    od = []
    gfp_p_od = []
    data_csv = pd.read_csv(filename)
    strain = data_csv['strain_name'].values
    strain_list = data_csv['strain_name'].values.tolist()
    strain_dedupe = list(dict.fromkeys(strain_list))
    print(strain_dedupe)
    for strains in strain_dedupe:
        index += 1
        od_single = []
        gfp_p_single = []
        for j in range(0, len(strain)):
            if strain[j] == strains:
                od_index = data_csv.loc[data_csv.strain_name == strain, 'od'].values[j]
                gfp_p_index = data_csv.loc[data_csv.strain_name == strain, 'gfp_p_od'].values[j]
                od_single.append(float(od_index))
                gfp_p_single.append(float(gfp_p_index))
        od_average = sum(od_single)/len(od_single)
        gfp_average = sum(gfp_p_single)/len(gfp_p_single)
        od.append(od_average)
        gfp_p_od.append(gfp_average)
        strain_name.append(strains)
    data_frame = {"strain_name": strain_name, "od": od, "gfp_p_od": gfp_p_od}
    df = pd.DataFrame(data_frame, columns = ['strain_name', 'od', 'gfp_p_od'])
    df.to_csv('/Users/ciaraconway/Desktop/rep3_8200_end.csv', index=False)
    data_test = df.head(10)
    print(data_test)
    return df

collect_dupe_strains('/Users/ciaraconway/Desktop/rep_1_8200_2.csv')



