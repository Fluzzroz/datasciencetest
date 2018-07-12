import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_group = pd.read_csv("testSamples.csv")
df_trans = pd.read_csv("transData.csv")

##Distribution of groups
print("Total number of samples:", df_group["test_group"].count())
print("Number of samples per group:\n", df_group["test_group"].value_counts(0))
print("Fractional Distribution of samples per group:\n",
      df_group["test_group"].value_counts(1))



fig, axe = plt.subplots()
df_group['test_group'].value_counts().plot(ax=axe,
                                           kind="bar",
                                           title="Group Distribution")

axe.set_xticklabels(["Control", "Test"], rotation="horizontal")

plt.savefig('Group_Distribution.png')
plt.show()


##Call-in (test group) users generate more REBILL ?
#First, assign the sample group to transactions

df_merge = pd.merge(df_trans, df_group, on="sample_id")

#split into control and test groups
df_control = df_merge[df_merge["test_group"]==0]
df_test = df_merge[df_merge["test_group"]==1]

#count the total number of control group transactions
n_control_ALL = len(df_control)
#count the number of each transaction types in control group
n_control_CB, n_control_RB, n_control_RF = df_control.groupby("transaction_type").size()

#count the total number of test group transactions
n_test_ALL = len(df_test)
#count the number of each transaction types in control group
n_test_CB, n_test_RB, n_test_RF = df_test.groupby("transaction_type").size()

#We calculate the ratio of transactions that are REBILLS for test and control
ratio_control_RB = n_control_RB / n_control_ALL
ratio_test_RB = n_test_RB / n_test_ALL

#... and compare them (ie: question 2)
print("Is a user that call-in more likely to generate additional rebill?")
print("ratio_test_RB > ratio_control_RB ?")
print(ratio_test_RB, ">", ratio_control_RB, "?")
print(ratio_test_RB>ratio_control_RB)

#question 3, same answer as #2
print("Is a user that call-in more likely to generate more revenue?")
print("ratio_test_RB > ratio_control_RB ?")
print(ratio_test_RB, ">", ratio_control_RB, "?")
print(ratio_test_RB>ratio_control_RB)

#question 4, the inverse of questions 2-3
test_CB_RB_rate = n_test_CB / n_test_RB
control_CB_RB_rate = n_control_CB / n_control_RB
print("Is a user that call-in more likely to produce a higher "
      "chargeback rate(CHARGEBACKs/REBILLs)?")
print("test_CB_RB_rate > control_CB_RB_rate ?")
print(test_CB_RB_rate, ">", control_CB_RB_rate, "?")
print(test_CB_RB_rate > control_CB_RB_rate)
