import os, os.path, pandas as pd

#directory name
directory = "conf_files"

#lists that will contain data
names = []
description = []
ip_address = []
subnet_mask = []
gateway = []

#loop read each conf file
for file in os.listdir(directory):
  #check if element is a file
  if os.path.isfile(os.path.join(directory, file)):
    #open file for reading
    file = open(os.path.join(directory,file), 'r')
    #read all lines in file
    lines = file.readlines()
    #loop to find specific words in file lines
    #loop uses all file lines length
    for l in range(len(lines)):
      #if word is found then it gets next line data
      if "Name" in lines[l].strip():
         names.append(lines[l+1].strip())
      if "Description" in lines[l].strip():
         description.append(lines[l+1].strip())
      if "IP address" in lines[l].strip():
         ip_address.append(lines[l+1].strip())
      if "Subnet mask" in lines[l].strip():
         subnet_mask.append(lines[l+1].strip())
      if "Gateway" in lines[l].strip():
         gateway.append(lines[l+1].strip())

#create dictionary with all lists
csv_data = {'Name': names, 'Description': description, 'IP address': ip_address, 'Subnet mask': subnet_mask, 'Gateway': gateway}

#create pandas data frame that contains all data
df = pd.DataFrame(csv_data)

#save data frame to .csv file
df.to_csv(os.path.join(directory,"summary.csv"),index=False)
