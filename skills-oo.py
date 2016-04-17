"""
QUESTIONS:

What are the three main design advantages that object orientation can provide?
    encapsulation - keep things/attributes tidy and together when similar
    abstraction - hides information you don't need to know
    polymorphism - makes things/attributes interchangable when they should be interchangable

What is a class?
    an object that can have attributes and can do stuff that is created by the user

What is an instance attribute?
    something descriptive that belongs only to the creation of a specific instance of a class

What is a method?
    a function inside a class. It has to act on an instance of a class

What is an instance in object orientation?
    an actual object that's been created in the class

How is a class attribute different than an instance attribute? Give an example of when you might use each.
    class attributes are assigned to every instance of that class. 
    instance attributes are only assigned to that specific instance. 

"""

class Student(object):
    """makes a student"""

    # I made the arguments optional b/c I got tired of typing over and over to test my code
    def __init__(self, first_name=None, last_name=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """holds a question and a correct answer for that question"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    # code that asks the user the question and assesses if it matches the answer
    def ask_and_evaluate(self):
        user_answer = raw_input(str(self.question) + " ")
        if user_answer == self.answer:
            return True
        else: 
            return False


class Exam(object):
    """makes an exam"""
    
    def __init__(self, name=None):
        """initializes a(n optional) name and an emplty list of questions for each Exam"""
        self.name = name
        self.questions = []

    # I wasn't sure about convention for capitialization if you're passing an class instance as a parameter... 
    def add_question(self, Question):
        """appends Question instances to the Exam"""

        self.questions.append(Question)

    def administer(self):
        """gives the exam to the student"""
        # initializes a score variable at 0
        score = 0
        # iterates through the list of questions stored in the exam
        for question in self.questions:
            # gathers True or False from the ask_and_evaluate function and stores it as correctness
            correctness = question.ask_and_evaluate()
            # increments the score if the question was right
            if correctness == True:
                score += 1
        # gives the user feedback on their score
        print "You scored {}/{} ({}%)".format(score, len(self.questions), score/len(self.questions) * 100)
        # returns the score value so it can be called later to be assigned as an attribute to the student
        return score

class Quiz(Exam):
    """makes a quiz that is a P/F version of the Exam superclass"""

    def administer(self):
        """re-define the administration of a quiz because the outcome is different than for an exam"""
        score = 0
        for question in self.questions:
            correctness = question.ask_and_evaluate()
            if correctness == True:
                score += 1
        # calculates if the student scored at least a 50% and prints a pass or fail statement accordingly
        percent_correct = score / len(self.questions)
        if percent_correct > .5:
            print "You passed!!"
        else:
            print "I'm sorry, but you didn't score at least a 50\%\ on this quiz."
        # returns the score so it can be assigned to the student as an attribute (i chose to keep the score and not the P/F return value)
        return score


def take_test(Exam, Student):
    """makes an Exam, Student, and administers test"""

    # takes the final score after administering an exam/quiz and stores it as an attribute for that student
    # to make this more interesting, I could allow multiple score attributes on each student. 
    # I'd do that by making "score" a more descriptive name
    Student.score = Exam.administer()


# example function - but I didn't make a function b/c then the variables weren't available globally to debug in -i mode
# this is just so I don't have to type this over and over every time I want to debug my code in the console. 
allison = Student("Allison")
test = Exam()
q1 = Question("How old are you?", "31")
q2 = Question("What is your favorite color?", "red")
q3 = Question("In whcih state do you live?", "ca")
test.add_question(q1)
test.add_question(q2)
test.add_question(q3)
quiz = Quiz()
quiz.add_question(q1)
quiz.add_question(q2)
quiz.add_question(q3)


