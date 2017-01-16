"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   1. Encapsulation: The data and it's corresponding attributes/methods are kept together
   2. Abstraction: The inner workings of the process (attributes and methods) are
   hidden so you can use them without knowing how they work
   3. Polymorphism: Different classes can be made that resemble each other.

2. What is a class? A type of thing with common traits

3. What is an instance attribute? A trait that is applied to a single instance/object
that is created.

4. What is a method? A method is essentially a function defined within a class

5. What is an instance in object orientation? a specific member of that class. For 
example, a dog could be a class, but Fido is an instance of the dog class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   A class attribute applies to all members of that class. An instance attribute 
   would only apply to that instance. Name would be a good instance attribute since 
   it would be specific to the instance created. Has hair would be a good class attribute
   for mammals since they will all have hair.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Students(object):
    """Class with student names and addresses"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address




class Questions(object):
    """Class with questions and answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer 
            

    def ask_and_evalute(self):
        '''prompts user to answer question and give T/F depending on answer'''
        user_question = raw_input(self.question)
        if user_question == self.correct_answer:
            print True
        else:
            print False

class Exams(Questions):
    """Exams with questions, method to add questions and method to administer test"""
    

    def __init__(self, name):
        self.name = name
        self.questions = []
       
        

    def add_question(self, question, correct_answer):
     
        super(Exams, self).__init__(question, correct_answer)
        self.questions.append([question, correct_answer])
        #print showed that all of the multiple questions get added, but not asked


    def administer(self):
        score = 0

        super(Exams, self).ask_and_evalute()

        for self.question in self.questions:
        
            if self.ask_and_evalute == True:
                score += 1
        #print score  #This part of the code isn't working correctly - score stays at 0


def take_test(exam, student):
    score = 0
    exam_name = Exams(exam)
    exam_name.add_question("Are cats awesome?", "yes")

    #Trying a list of Q's and a list of A's to iterate through to allow multiple
    #questions and answers
    # exam_name.add_question(["Are cats awesome?", 
    #                         "What is your favorite color?",
    #                         "How do I add multiple questiions? Would a dict work?"], 
    #                         ["yes", "blue", "Maybe"])
    exam_name.administer()
    score += 1
    print "Your score: ", score  # This isn't right since the score from the class method isn't working correctly,
    # I created a false score in the function so I could keep going with the exercises

#take_test('final', 'Melissa')



def example(exam, first_name, last_name, address):
    student = Students(first_name, last_name, address)
    new_exam = Exams(exam)
    # new_exam.add_question("Are cats awesome?", "yes")
    # new_exam.add_question("What is your favorite color?", 'blue')
    # new_exam.add_question("How do I add multiple questions? Would a dict work?", "Maybe")


    # new_exam.add_question(["Are cats awesome?", 
    #                         "What is your favorite color?",
    #                         "How do I add multiple questions? Would a dict work?"], 
    #                         ["yes", "blue", "Maybe"])

    #I don't understand how to get the program to ask each of the questions and not just the last one
    take_test(exam, student)

example('midterm', "Jon", "Snow", "The North")



#Did not do part 5 since it uses so many parts of Part 4 that aren't working correctly
# Quiz class could run assessment from Exam class and return True if score >= 50 %
# else return False
