import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime
import math

behavior_raw_data = pd.read_csv("./NTU_2019/BehaviorDataForNTU.txt",sep=',',encoding="utf-8")
df = pd.DataFrame(behavior_raw_data)

NtoA_raw_data = pd.read_excel('./NTU_2019/N_to_A.xlsx', encoding='utf-8')
LPtoA_raw_data = pd.read_excel('./NTU_2019/L_to_A and P_to_A.xlsx', encoding='utf-8')

NtoA_raw_data = pd.DataFrame(NtoA_raw_data)
LPtoA_raw_data = pd.DataFrame(LPtoA_raw_data)
NtoA_raw_data.columns = NtoA_raw_data.columns.str.replace(' ', '_')
LPtoA_raw_data.columns = LPtoA_raw_data.columns.str.replace(' ', '_')

# new_df: 去除所有online member id為nan的row
new_df = df.loc[(df['OnlineMemberId'].astype(str) != 'nan')]


memberId = NtoA_raw_data['Online_Member_Id']
memberId = memberId.reset_index()
del memberId['index']

start_date = NtoA_raw_data['Trades_Date'] - pd.Timedelta(90, unit='d')
end_date = NtoA_raw_data['Trades_Date']
start_date = start_date.reset_index()
end_date = end_date.reset_index()
del start_date['index'], end_date['index']

mask = list()
result_df_list = list()
for i in range(len(NtoA_raw_data)):
    # print(i)
    mask = (new_df['OnlineMemberId'] == memberId['Online_Member_Id'][i]) & (new_df['HitDateTime'] > str(start_date['Trades_Date'][i])) & (new_df['HitDateTime'] <= str(end_date['Trades_Date'][i]))
    result_df_list.append(new_df.loc[mask])
    
result_df = result_df_list[0]
for i in range(1, len(result_df_list)):
    result_df = result_df.append(result_df_list[i])

del result_df['VisitorId'],result_df['OperationSystem'],result_df['CategoryId'],result_df['SearchKeyWord'],result_df['TransactionNum'],result_df['ProductPrice'],result_df['ProductQuantity'],result_df['ProductId'],result_df['TransactionRevenue']

result_df.to_excel("N to A behavior.xlsx")


memberId = LPtoA_raw_data['Online_Member_Id']
memberId = memberId.reset_index()
del memberId['index']

start_date = LPtoA_raw_data['Trades_Date'] - pd.Timedelta(90, unit='d')
end_date = LPtoA_raw_data['Trades_Date']
start_date = start_date.reset_index()
end_date = end_date.reset_index()
del start_date['index'], end_date['index']

mask = list()
result_df_LP_list = list()
for i in range(len(LPtoA_raw_data)):
    # print(i)
    mask = (new_df['OnlineMemberId'] == memberId['Online_Member_Id'][i]) & (new_df['HitDateTime'] > str(start_date['Trades_Date'][i])) & (new_df['HitDateTime'] <= str(end_date['Trades_Date'][i]))
    result_df_LP_list.append(new_df.loc[mask])

result_df_LP = result_df_LP_list[0]
for i in range(1, len(result_df_LP_list)):
    result_df_LP = result_df_LP.append(result_df_LP_list[i])

del result_df_LP['VisitorId'],result_df_LP['OperationSystem'],result_df_LP['CategoryId'],result_df_LP['SearchKeyWord'],result_df_LP['TransactionNum'],result_df_LP['ProductPrice'],result_df_LP['ProductQuantity'],result_df_LP['ProductId'],result_df_LP['TransactionRevenue']

result_df_LP.to_excel("LP to A behavior.xlsx")
