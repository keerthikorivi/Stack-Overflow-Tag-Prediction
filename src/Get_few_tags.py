import csv
import re
import string
from collections import defaultdict
from string import digits

count=0;
no_match_found=1


with open("C:\\Masters\\CIS732\\dataset\\Train\\Train_result.csv","rb") as source:
    rdr= csv.reader( source )
    w = csv.writer(open("C:\\Masters\\CIS732\\dataset\\Train\\Train_result_sample_new_final_subsampling_tags_15_all.csv", "w"))
    for r in rdr:
        row=[]
        tags=""
        words = r[2].split()
        for x in words:
            if("java" in x):
                if ("javascript" in x):
                        if("javascript" not in tags):
                            tags = tags + "javascript "
                else:
                    tags=tags+"java "
            if("android" in x):
                if ("android" not in tags):
                    tags = tags + "android "
            if("multithreading" in x):
                if ("multithreading" not in tags):
                    tags = tags + "multithreading "
            if("mysql" in x):
                if ("mysql" not in tags):
                    tags = tags + "mysql "
            if("swing" in x):
                if ("swing" not in tags):
                    tags = tags + "swing "
            if("exception" in x):
                if ("exception" not in tags):
                    tags = tags + "exception "
            if("eclipse" in x):
                if ("eclipse" not in tags):
                    tags = tags + "eclipse "
            if("python" in x):
                if ("python" not in tags):
                    tags = tags + "python "
            if("django" in x):
                if ("django" not in tags):
                    tags = tags + "django "
            if("dictionary" in x):
                if ("dictionary" not in tags):
                    tags = tags + "dictionary "
            if("matplotlib" in x):
                if ("matplotlib" not in tags):
                    tags = tags + "matplotlib "
            if("numpy" in x):
                if ("numpy" not in tags):
                    tags = tags + "numpy "
            if("scala" in x):
                if ("scala" not in tags):
                    tags = tags + "scala "
            if("functional-programming" in x):
                if ("functional-programming" not in tags):
                    tags = tags + "functional-programming "
        if(tags==""):
            continue
        else:
            if count<=10000:
                row.append(r[1])
                row.append(tags)
                w.writerow(row)
                count=count+1
            else:
                break

    #w.writerow(all)
