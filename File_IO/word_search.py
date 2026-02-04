# problem statement : search a given word in a given file and if exist then find its position or character number

# file : word_search_file.txt ; word to find : LNCT
to_find="Hello"
word=""
char_count=0
with open("./word_search_file.txt","r") as f:
    while True:
        # read one char at a time
        char=f.read(1)
        char_count+=1
         # end of file
        if char=="":
            print(f"{to_find} not found !")
            break
        # if space occurs means word changed so try next
        if char==" ":
            word=""
        else:
            word+=char
                # condition when word found
        if(word==to_find):
            print(f"{to_find} Found  at character number {char_count}!")
            break
        
