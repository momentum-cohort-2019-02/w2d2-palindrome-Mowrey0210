text_input = str(input("Please input some text:"))


def clean_input(text):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()
    new_text =""
    for char in text:
        if char in all_letters:
            new_text += char
    return(new_text.lower())      
    # print(new_text.lower()) 

clean_input(text_input)

def check_string(palindrome):

    palindrome = clean_input(palindrome)

    if len(palindrome) == 1:
        return print('is a palindrome') 

    elif palindrome[0] != palindrome[-1]:
       return print('is not a palindrome')    

    else:
        while palindrome[0] == palindrome[-1]:
            if len(palindrome) <= 1:
                return print("is a palindrome") 
            else:
                # remove+= palindrome[0:],
                # palindrome[-1:]
                # new_str = palindrome
                new_str=''
                new_str.replace(palindrome[0],'')
                new_str.replace(palindrome[-1],'')
                # palindrome.replace(0,'')
                # palindrome.replace(-1,'')             # # palindrome.pop[0]
                # # palindrome.pop[-1]                
            return print("is a palindrome") 
            
        return print("is not a palindrome")  

check_string(text_input)
            



        










