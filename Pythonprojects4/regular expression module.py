#regular expression module help us to easily search and get any string from large string.
#USE FILE FROM MOBILE OR ANYWHERE THERE YOU CAN FIND EVERYTHING ABOUT EACH FUNCTION THERE ARE MANY FUCTIONS.
import re
mystr="Approved by the Directorate of Technical started Education of Maharashtra on 16 September 1983,+919789789865" \
      "[1] TSEC is one of the oldest private engineering colleges of India and was among the first institutes in the" \
      " country to offer undergraduate level studies in specializations of computer engineering, information technology+917583920384 " \
      "and biomedical engineering. The Department of Biomedical Engineering is one of the oldest in India[4] and was set up in 1983." \
      "[1] The first batch of Computer Engineering graduates passed out in 1988.78986-7896" \
      "[1] The undergraduate course in Information Technology was started in 1998.[1] The departments of Electronics & Telecommunication Engineering +918475847236" \
      " as well as Chemical Engineering were established in the year 1983,[1] whereas that of Biotechnology was established in the " \
      "top of achievements of the institute lies the starting of the Ph.D. program by the University of Mumbai in the department of Information Technology." \
      "[6] aur kaisan baa"
pattern=re.compile(r'started')  #here r means raw means it will consider\n a \n only not next line notation.
pattern=re.compile(r'.')   #dot will give you any character.
pattern=re.compile(r'^Aprroved')   #^ this sign indicate string start with if string dont start with given then nothing will come.
pattern=re.compile(r'baa$')   #^$this sign indicate string end with if string dont end with given then nothing will come.
pattern=re.compile(r'es*')   #star(*)symbol means zero or many occurence here e should be  1 and s can be any number zero s also inculded so only e can also come.
pattern=re.compile(r'es+')   # + means one or more than one occurence same as star but not zero allowed like in this no only e is allowed only with 1 or more than that is allowed.
pattern = re.compile(r'es{1}') # {} this used to specifiy that exact we need this much s like here given exat 1 e and 2 s .
pattern = re.compile(r'(te){2}') # ()this used to capture in group like in this we need both te two time eg:-tete.
pattern = re.compile(r'te{1}|es') #(|) this slash is used for either it will give either tee or es in this.
#special sequencing,
pattern = re.compile(r'\AApproved') #\A return a match if specified character was in the begining of string.
pattern = re.compile(r'gy\b')  # \b return a match if specified character was in the begining or end of the words.
pattern = re.compile(r'\Bgy')    #\B return a match in which specified character are present but not in begining nor at end.


pattern=re.compile(r'\d{5}-\d{4}')   #\d is used to find numbers and in this way using {} specified we can detect specified number of 10characters or any.

#TASK IS TO FIND INDIAN NUMBERS.
pattern = re.compile(r'\+91\d{10}')









match=pattern.finditer(mystr)      #this will help you to get file location and how many are there of given str name.
for matches in match:
    print(matches)