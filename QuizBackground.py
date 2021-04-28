class Question:
    def __init__(self, prompt, choices, answer):
        self.prompt = prompt
        self.choices = choices
        self.answer = answer

Questions_book = ['In which book did Harry Potter first meet Luna Lovegod?', 'In which book does Harry Potter meet Rufus Scrimgeour?', 'In which book is Sirius black first mentioned?',
'In which book did Harry Potter first meet Horace Slughorn?', 'In which book did Harry Potter first meet Cho Chang?', 'In which book did Harry Potter first meet Charlie Weasley?',
'In which book did Harry Potter first meet Narcissa Malfoy?', 'In which book did Harry Potter first meet Zacharias Smith?']

Questions_multiple_choice = ['I dont think you should be an Auror, Harry... ... The Aurors are part of the ___', 'Oh hello Harry, did you know one of your eyebrows is bright ___', 'Which of the following shops CANNOT be found in Diagon Alley',
'First name of the barman who works at the Leaky Cauldron', 'Enter, stranger, but take heed...', 'Harry met his first fellow Hogwarts student at Madam Malkins Robes, who was it?',
'What was the name of the pygmy puff Ginny bought from Weasleys Wizard Wheezes', 'In ootp what three things are scattered on the floor of The Knight Bus when Harry, Ron, and Hermione are heading back to Hogwarts',
'What are the name of Severus Snapes parents','Who is the author of Unfogging The Future', 'What is Harry\'s date of birth']

Questions_enter_yourself = ['Upon tapping the wall that magically reveals Diagon Alley, what formation will lead to success', 'How many exceptions are there to Gamp\'s Elemental Law?']

book_dict = {'ootp' : 'Order of The Pheonix', 'hbp' : 'Half Blood Prince', 'ps' : 'Philosophers Stone', 'poa' : 'Prisoner of Azkaban', 'gof' : 'Goblet of Fire'}

book_answer_choices = '{ootp}\n{hbp}\n{ps}\n{poa}\n{gof}'.format(**book_dict)
#print(book_answer_choices)

multiple_choice_answers = [['humdinger league','rotfang conspiracy','durmstrang plot','mugwump scheme'], ['purple', 'yellow','red','green'],['Weasleys Wizard Wheezes','Eyelops Owl Emporium','honeydukes','ollivanders'],
['tom','aberforth','greg', 'theo'],['the verse you should take time to read', 'take only what you dearly need', 'we know of every darkest deed', 'of what awaits the sin of greed'],['draco','hermione', 'ronald', 'terry'],
['hugo', 'arnold', 'barry','craig'],['egg shells, digestives, and bat wings', 'cat hair, feathers, and cat litter', 'frogspawn, cockroaches, and custard creams', 'beetle dung, dead wassps, and a mug of tea'],
['Theodore Snape and Ethel Prince','Tripp Snape and Eliane Prince','Toby Snape and Ellen Prince','Tobias Snape and Eileen Prince'],['Selina Sapworthy', 'Cassandra Vablatsky','Greta Catchlove', 'Galatea Merrythought'],
['1980', '1990', '1981','1991']
]

questions = [
    Question(Questions_book[0], book_answer_choices, book_dict['ootp']),
    Question(Questions_book[1], book_answer_choices, book_dict['hbp']),
    Question(Questions_book[2], book_answer_choices, book_dict['ps']),
    Question(Questions_book[3], book_answer_choices, book_dict['hbp']),
    Question(Questions_book[4], book_answer_choices, book_dict['poa']),
    Question(Questions_book[5], book_answer_choices, book_dict['gof']),
    Question(Questions_book[6], book_answer_choices, book_dict['gof']),
    Question(Questions_book[7], book_answer_choices, book_dict['ootp']),
]

questions_multiple = [
     Question(Questions_multiple_choice[0], multiple_choice_answers[0], multiple_choice_answers[0][1]),
     Question(Questions_multiple_choice[1], multiple_choice_answers[1], multiple_choice_answers[1][1]),
     Question(Questions_multiple_choice[2], multiple_choice_answers[2], multiple_choice_answers[2][2]),
     Question(Questions_multiple_choice[3], multiple_choice_answers[3], multiple_choice_answers[3][0]),
     Question(Questions_multiple_choice[4], multiple_choice_answers[4], multiple_choice_answers[4][3]),
     Question(Questions_multiple_choice[5], multiple_choice_answers[5], multiple_choice_answers[5][0]),
     Question(Questions_multiple_choice[6], multiple_choice_answers[6], multiple_choice_answers[6][1]),
     Question(Questions_multiple_choice[7], multiple_choice_answers[7], multiple_choice_answers[7][2]),
     Question(Questions_multiple_choice[8], multiple_choice_answers[8], multiple_choice_answers[8][3]),
     Question(Questions_multiple_choice[9], multiple_choice_answers[9], multiple_choice_answers[9][1]),
     Question(Questions_multiple_choice[10], multiple_choice_answers[10], multiple_choice_answers[10][0])
]



def run_test(questions):
    print('The Ultimate Harry Potter Quiz')
    score = 0
    for question in questions:
        answer = input('\n' + question.prompt + '\n' + question.choices + '\n\n\n')
        if answer.lower() == question.answer.lower():
            score += 1
            print('You are correct!')
        else:
            print('Unfortunately you are wrong... ')

    for question in questions_multiple:
        print('\n' + question.prompt + '\n')
        for choice in question.choices:
            print(choice)
        answer = input('\n')

        if answer == question.answer.lower():
            score +=1
            print('You are correct!')
        else:
            print('Unfortunately you are not correct...')

    print('You got ' + str(score) + '/' + str(len(questions) + len(questions_multiple)) + ' correct')

    if score == 0:
        print('You are Argus Filch')
    elif score == 1 or score <= 3:
        print('You are Gregory Goyle...')
    elif score == 4 or score <= 7:
        print('You are Ronald Weasely!')
    elif score == 8 or score <= 9:
        print('You are Neville Longbottom')
    elif score == 10 or score <=11:
        print('You are Minerva McGonagall!')
    elif score == 12 or score <= 13:
        print('You are Lily Potter!')
    elif score == 14 or score < 15:
        print('You are Harry Potter!')
    elif score == 15 or score <= 16:
        print('You are Albus Dumbledore!')
    elif score == 17:
        print('You are Nicolas Flamel')
    elif score == 18 or score > 18:
        print('You are Hermione Granger!')
    return score

RunTest = run_test(questions)
