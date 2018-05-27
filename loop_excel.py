import random
import xlsxwriter

workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet('data')

def gen_random_list(x):
    inputlist = []
    #x = 10
    for y in range(x):
        inputlist.append(random.randint(0,y))
    #print ("inputlist")
    #print (inputlist)
    return inputlist


#print (gen_random_list(20))
key = 0
dirlist = {}
inputval = 30
masterlist = []
templist = []
listdatapoints = 10

#simulate input data 
inlist1 = gen_random_list(inputval)
inlist2 = gen_random_list(inputval)
inlist3 = gen_random_list(inputval)
inlist4 = gen_random_list(inputval)

for x in range(inputval):
    templist.append(inlist1[x])
    templist.append(inlist2[x])
    templist.append(inlist3[x])
    templist.append(inlist4[x])
    
    masterlist.append(templist)
    templist = []
 
for x in range(inputval):
    dirlist.update({key:masterlist[x]})
    key += 1

"""
for key, value in dirlist.items():
    print (key, value)
"""

    
row = 0
col = 0
worksheet.write(row, col, 'Key')
worksheet.write(row, col + 1, 'Value1')
worksheet.write(row, col + 2, 'Value2')
worksheet.write(row, col + 3, 'Value3')
worksheet.write(row, col + 4, 'Value4')

for key in dirlist.keys():
    row += 1
    col = 0
    
    worksheet.write(row, col, key)

    for item in dirlist[key]:
        worksheet.write(row, col + 1 , item)
        #row += 1
        col += 1

workbook.close()

