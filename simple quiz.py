print('welcome to py quiz')
answer=input('are u ready to play ?(yes/no):')
score = 0
total_questions = 3

if answer.lower()=='yes':
    answer=input('Q1:what is my favourite game?')
    if answer.lower()=='pubg':
        score += 1
        print('correct! sath me khelenge aaja')
    else:
        print('moye moye!  wrong answer😉')

    answer=input('Q2:what is my name ?')
    if answer.lower()=='karibasu':
        score += 1
        print('correct! tnx yaar mere baare me janane ke liye')
    else:
        print('moye moye! atleast mere naam janlo😉')

    answer=input('Q3:do i have a girlfriend(yes/no) ?')
    if answer.lower()=='no':
        score += 1
        print('correct! abe sahi answer dekhe mood math kharab kar')
    else:
        print('moye moye! lekin ye sunke acha lag raha hai')    


print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
        