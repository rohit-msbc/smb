from smb.SMBConnection import SMBConnection
import pandas as pd

server_name = '10.10.20.239'
username = ''
password = ''
share_name = 'Shared'
remote_file_path = '/Volumes/Shared/AdvancedInterconnects/Qingjun/phase measurement quadrature/omega temp/omega_d0726_1030pm_0154pm.xlsx'

conn = SMBConnection(username, password, 'client', server_name, use_ntlm_v2=True)
if conn.connect(server_name, 445):
    print("connected")
else:
    raise ConnectionError("Failed to connect to NAS drive.")

with open(remote_file_path, 'r') as file:
    data = pd.read_excel(remote_file_path)

conn.close()

print(data)