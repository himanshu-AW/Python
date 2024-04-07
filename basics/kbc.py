questions=[ 
    ["which of the following corresponds to 'ek bataa do' ? ","Pura","Sawa","Adha","Pauna",3],    #1
    ["In the Game of Ludo  the Disc or tokens are of how manuy colours ?","One","Two","Three","Four",4],   #2
    ["Which of the following gods is also known ads 'Gauri Nandan' ?","Agni","Indra","Hanuman","Ganesha",3],     #3
    ["Which Of The folling are names  of National park located in Madhya Pradedsh?","Krishna & Kanhiya","Kanha & Madhav","Ghanshyam & Murari","Girdhar & Gopal",2],  #4
    ["Bahubali Festival is related to ","Isalam","Hinduism","Buddhism","Jainism",4],   #5
    ["The International literacy day is observed on ","Sep 8","Nov 28","May 2","Sep 22",1],  #6
    ["Which day is observed as the World Standards Day ?","June 26","Oct 14","Nov 15","Dec 2",2],  #7
    ["where was the BRICS summit held in 2014 ?","Brazil","India ","Russia ","china ",1],   #8
    ["Who wrote the inroduction to the english translaton of Rabindranath Tagore's Gitanjali ?","P.B. Shelley","Alfred Tennyson","W.B. Yeats","T.S. Elliot",3],   #9
    ["Which of these leaders was a recipient of a gallantry Award in 1987 by a state government for savin two girls from drowning ?","Anandiben Patel","Vasundhara Raje Scindia","Uma Bharti","Mamta Banerjee", 1],  #10
    ["The wife of Which of hese famous sports persons was once caption of india volleyball team ?","K.D.Jadav","Dhyan Chand","Prakash Padukone","Milkha Singh",4],  #11
    ["Starting With the earlist , arrange the folling events in Narendra Modi's life in Chronolical order .FFF(Fastest Finger First)","CM of Gujarat","Took oath as"," Joined BjP"," Became RSS Pracharak",4], #12
    ["Which of these teams can only be used for women ?","Dirghaayu","Suhagan","Chiranjeevi","sushil",2],    #13
    ["The Language of lakshadweep. a Union Territory of india , is ","Tamil","Hindi","Malayalam","Telgue",3],  #14
    ["in which group of places the Kumbha mela is held every twelve years ?","Ujjain. Purl; Prayag. Haridawar","Prayag. Haridwar, Ujjain, Nasik","Rameshwaram. Purl, Badrinath. Dwaika","Chittakoot, Ujjain, Prayag;Haridwar " ,2],  #15
    ]
amount=[1000,2000,4000,8000,10000,20000,40000,80000,160000,320000,640000,10000000,20000000,40000000,70000000]
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\t--:Your Question {i+1} is Rs. {amount[i]}:--\n")
    print(f"Q{i+1}. {question[0]}")
    print(f" 1. {question[1]}         2. {question[2]} ")
    print(f" 3. {question[3]}         4. {question[4]} ")
    print("Select any one Option Or You can exit :",end="")
    replay=int(input())
    if replay==question[5]:
        print("Your Answer Is Correct \n")
    else:
        if i>=5 and i<10:
            print("You Choose Wrong Answer!! ")
            print(f"You won Total amount : {amount[i-1]}")
        elif i>=10 and i<15:
            print("You Choose Wrong Answer!! ")
            print(f"You won Total amount : {amount[i-1]}")
        else:
            print(" You Have Choosen Wrong Answer !!")
            print("Your Amount is ",0)
        break