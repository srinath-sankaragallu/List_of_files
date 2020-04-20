import os

def getfiles(pat,folder_notation = '\\'):
    ''' a recursive funtion to genarate the
    list of files in a given directory'''

    LF = []
    LF = os.listdir(pat)
    LF = list(map(lambda x: pat + folder_notation +  x , LF))
    for f in LF:
        if os.path.isdir( f ):
            LF += getfiles( f )
    return LF

########################################################3
#-- working exmaple is shown below

# lis = getfiles(r'C:\Users\xxx\AppData\Local\Programs\Python\Python38')
# #lis = getfiles(r'C:\Users\xxx\Documents\Python_Scripts')

# fp = open(r'C:\Users\xxx\Documents\Python_Scripts\list__of_files.txt','w')
# for l in lis:
#     fp.write(l)
#     fp.write('\n')
# fp.close()
