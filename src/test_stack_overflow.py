import csv
import re
import string
from collections import defaultdict
from string import digits
taglist=defaultdict(lambda :0)
stopwords = ['me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what','whom', 'this', 'that', 'these', 'those', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but','because', 'as', 'until', 'of', 'at', 'by','with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when','why', 'how', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'aint', 'arent', 'couldnt', 'didnt', 'doesnt', 'hadnt', 'hasnt', 'havent', 'isnt', 'ma', 'mightnt', 'mustnt', 'neednt', 'shant', 'shouldnt', 'wasnt', 'werent', 'wont', 'wouldnt','cant']
java_tag=0
android_tag=0
javascript_tag=0
multithreading_tag=0
mysql_tag=0
swing_tag=0
exception_tag=0
eclipse_tag=0
python_tag=0
django_tag=0
dictionary_tag=0
matplotlib_tag=0
numpy_tag=0
scala_tag=0
functional_programming_tag=0
count=0;
no_match_found=1
with open("C:\\Masters\\CIS732\\dataset\\Train\\Train_result.csv","rb") as source:
    rdr= csv.reader( source )
    w = csv.writer(open("C:\\Masters\\CIS732\\dataset\\Train\\Train_result_sample_new_final_subsampling_10000.csv", "w"))
    all = []
    for r in rdr:
        #s=r[1].replace("?","").replace("<p>","").replace(",","").replace('"',"").replace("...","")
        words=r[2].split()
        taglist[words[0]]= taglist[words[0]]+1
        row=[]
        if re.match("java",r[2]):
            java_tag=1
            no_match_found=0
        if re.match("android",r[2]):
            android_tag=1
            no_match_found=0
        if re.match("javascript",r[2]):
            javascript_tag = 1
            no_match_found=0
        if re.match("multithreading",r[2]):
            multithreading_tag = 1
            no_match_found=0
        if re.match("mysql",r[2]):
            mysql_tag = 1
            no_match_found=0
        if re.match("swing",r[2]):
            swing_tag = 1
            no_match_found=0
        if re.match("exception",r[2]):
            exception_tag = 1
            no_match_found=0
        if re.match("eclipse",r[2]):
            eclipse_tag = 1
            no_match_found=0
        if re.match("python",r[2]):
            python_tag = 1
            no_match_found=0
        if re.match("django",r[2]):
            django_tag = 1
            no_match_found=0
        if re.match("dictionary",r[2]):
            dictionary_tag = 1
            no_match_found=0
        if re.match("matplotlib",r[2]):
            matplotlib_tag = 1
            no_match_found=0
        if re.match("numpy",r[2]):
            numpy_tag = 1
            no_match_found=0
        if re.match("scala",r[2]):
            scala_tag = 1
            no_match_found=0
        if re.match("functional-programming",r[2]):
            functional_programming_tag = 1
            no_match_found = 0
        if(java_tag==0 & android_tag==0 & javascript_tag==0 & multithreading_tag==0 & mysql_tag==0 & swing_tag==0 & exception_tag==0 & eclipse_tag==0 & python_tag==0 & django_tag==0 & dictionary_tag==0 & matplotlib_tag==0 & numpy_tag==0 & scala_tag & functional_programming_tag==0):
            no_match_found=1
        if no_match_found ==0:
            count=count+1
            #row.append(r[0])
            remove_punctuations = re.sub(r'[?|$|.|!|#|%|(|)|:|/|\|+|+|-|*|&|^|@|}|{|]|[|,]', r'', r[1])
            x=remove_punctuations.replace("'", "").split()
            y=[word for word in x if not (word.isdigit() or isinstance(word,float))]
            z = [word for word in y if word.lower() not in stopwords]
            title_without_stopwords = string.join(z, " ")
            row.append("'"+title_without_stopwords+"'")
            row.append(java_tag)
            row.append(android_tag)
            row.append(javascript_tag)
            row.append(multithreading_tag)
            row.append(mysql_tag)
            row.append(swing_tag)
            row.append(exception_tag)
            row.append(eclipse_tag)
            row.append(python_tag)
            row.append(django_tag)
            row.append(dictionary_tag)
            row.append(matplotlib_tag)
            row.append(numpy_tag)
            row.append(scala_tag)
            row.append(functional_programming_tag)
            # r[0],r[1],c_sharp_tag,java_tag,php_tag,javascript_tag,android_tag,c_plus_plus_tag,iphone_tag,python_tag,jquery_tag,ruby_on_rails_tag,linux_tag,asp_net_tag,mysql_tag,sql_tag,c_tag
            if count<=10000:
                w.writerow(row)
                java_tag = 0
                android_tag = 0
                javascript_tag = 0
                multithreading_tag = 0
                mysql_tag = 0
                swing_tag = 0
                exception_tag = 0
                eclipse_tag = 0
                python_tag = 0
                django_tag = 0
                dictionary_tag = 0
                matplotlib_tag = 0
                numpy_tag = 0
                scala_tag = 0
                functional_programming_tag = 0
            else:
                break

    #w.writerow(all)
