import pandas as pd
import numpy as np

NtoA_behavior_raw_data = pd.read_excel('N to A behavior.xlsx')
LPtoA_behavior_raw_data = pd.read_excel('LP to A behavior.xlsx')
del NtoA_behavior_raw_data['HitDateTime'], NtoA_behavior_raw_data['OnlineMemberId']
del LPtoA_behavior_raw_data['HitDateTime'], LPtoA_behavior_raw_data['OnlineMemberId']

NtoA_behavior_raw_data = NtoA_behavior_raw_data.reset_index()
LPtoA_behavior_raw_data = LPtoA_behavior_raw_data.reset_index()
del NtoA_behavior_raw_data['index'], LPtoA_behavior_raw_data['index']

NtoA_behavior_raw_data['result'] = 1
LPtoA_behavior_raw_data['result'] = 0


oneHotEncoding = pd.get_dummies(NtoA_behavior_raw_data['TrafficSourceCategory'], prefix = 'TrafficSourceCategory')
NtoA_behavior_raw_data = NtoA_behavior_raw_data.drop('TrafficSourceCategory', 1)
new_df = pd.concat([oneHotEncoding, NtoA_behavior_raw_data], axis=1)

oneHotEncoding = pd.get_dummies(new_df['BehaviorType'], prefix = 'BehaviorType')
new_df = new_df.drop('BehaviorType', 1)
new_df = pd.concat([oneHotEncoding, new_df], axis=1)

oneHotEncoding = pd.get_dummies(new_df['SourceType'], prefix = 'SourceType')
new_df = new_df.drop('SourceType', 1)
new_df = pd.concat([oneHotEncoding, new_df], axis=1)


oneHotEncoding = pd.get_dummies(LPtoA_behavior_raw_data['TrafficSourceCategory'], prefix = 'TrafficSourceCategory')
LPtoA_behavior_raw_data = LPtoA_behavior_raw_data.drop('TrafficSourceCategory', 1)
new_df_LP = pd.concat([oneHotEncoding, LPtoA_behavior_raw_data], axis=1)

oneHotEncoding = pd.get_dummies(new_df_LP['BehaviorType'], prefix = 'BehaviorType')
new_df_LP = new_df_LP.drop('BehaviorType', 1)
new_df_LP = pd.concat([oneHotEncoding, new_df_LP], axis=1)

oneHotEncoding = pd.get_dummies(new_df_LP['SourceType'], prefix = 'SourceType')
new_df_LP = new_df_LP.drop('SourceType', 1)
new_df_LP = pd.concat([oneHotEncoding, new_df_LP], axis=1)

new_df_LP['BehaviorType_Purchase'] = 0

result_df = new_df.append(new_df_LP)
result_df = result_df.reset_index()
del result_df['index']

result_df.to_excel('one hot encoding data.xlsx')

