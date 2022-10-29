# email vaildation using python
from curses.ascii import isalpha

email=input("enter email id")  #abcdef@gmail.com  , g@g.in(6) 
error_code=0

output_error={
    0:"Vaild email id",
    1:"Email id can't contain spaces",
    2:"Email id should end with .xyz or .ab",
    3:"Email id should have @",
    4:"Email id should start with aplhabet",
    5:"Email id should have minimum length of 6"
}


if len(email)>=6:
    if email[0].isalpha()==True:
        if '@' in email and email.count('@')==1:
            if ( email[-4]=='.') ^ (email[-3]=='.'):
                for i in email:
                    if i ==' ': # i==i.isspace()
                        error_code=1
                        break
                    # elif i.isalpha():
                    #     if i==i.upper():
                    #         i=i.lower()
                        
                
            else:
                error_code=2
        else:
            error_code=3
           
    else:
        error_code=4
    
else:
    error_code=5

    
print(output_error[error_code])
