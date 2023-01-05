import csv
import pandas as pd


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

df = pd.read_csv('awsaccounts.csv', index_col=False)
df.drop(['Added By', 'Date Added', 'Description', 'Account Aliases', 'Display Name (S3)', 'Canonical ID (S3)', 'Notes'], axis=1, inplace=True)
pd.set_option('display.float_format', lambda x: '%.0f' % x)


df2 = df.rename(columns= {"Client's name for account" :'Account name','Cross Account Role ARN' :'Role ARN', 'Role Sign-in URL' :'Role Link', 'Account ID' :'Account ID'})
df2['Comment'] = df2['Account name']
df2 = df2.reindex(columns=['Account name', 'Account ID', 'Role ARN', 'Role Link', 'Comment'])

print(df2)
df2.to_csv(r'accounts.csv', index=False)



