
def beginExtraction():
	print("Dowloading Corpus...")
    	file = 'tiger_release_aug07.corrected.16012013.conll09'
	myfile = open(file)
	sentences = myfile.read()
	print("Tokenizing Corpus...")
	sentences = sentences.split('\n')
	pos_tags = []

	tokenized = [x for x in sentences if x]

	for sentences in tokenized[:500]:  
		sentences = sentences.split()
		w = sentences[1]
		pos = sentences[4]
		t = (w, pos)
		pos_tags.append(t)

	 words = []
	 pos = []
	 for pair in pos_tags:
	 	words.append(pair[0])
		pos.append(pair[1])
	 #tagset = []
	 #for POS in pos:
	 #    if POS not in tagset:
	 #        tagset.append(POS)
	 print("Extracting CFG...")
	 SENT = extractCFG(pos_tags, words, pos)
	 for value in SENT.values():
	 	if isinstance(value, dict):
			recursiveCFG(value, words, pos)

	 #for i in SENT:
	 #	print(i, '=>', SENT[i], '\n')

def extractCFG(dataset, words, pos):
	SENT = {}
    	for i in range(len(words)):
        	for j in range(len(pos)):
            	### Setting inital Sentence Starters ###
            	if words[i-1] in  '.?!':
                	SENT[pos[j]] = {}
           	for next in SENT.keys():
                	if pos[j-1] == next:
                    	SENT[next][pos[j]] = {}
    	return SENT
            
def recursiveCFG(dataset, words, pos):
    	for i in range(len(words)-1):
        	for j in range(len(pos)-1):
            		for next in dataset:
                		if pos[j-1] == next:
                    			dataset[next][pos[j]] = {}
                				if words[i+1] in '.!?':
                   					dataset[next]['NULL'] = {}
	return dataset
    
#words = []
#pos = []
#for pair in pos_tags:
#    words.append(pair[0])
#    pos.append(pair[1])
#tagset = []
#for POS in pos:
#    if POS not in tagset:
#        tagset.append(POS)
#SENT = extractCFG(pos_tags, words, pos)

#for value in SENT.values():
#    if isinstance(value, dict):
#        recursiveCFG(value, words, pos)
#        
#for i in SENT:
#    print(i, '=>', SENT[i], '\n')
    

