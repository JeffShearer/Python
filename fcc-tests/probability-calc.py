import copy
import random
from collections import Counter
# Consider using the modules imported above.


class Hat:
    colors = dict()
    name = ""
    drawn = ""
    list = []
    contents =[]
    draw_list = []
    experiment_list= []

    
    

    # ** allows you to pass a variable # of arguments that are keyworded (a single * would be non-keyworded)
    # But since this is a dictionary of K-V pairs, a double asterisk is appropriate (kwargs)
    def __init__(self,**colors):
        self.name = self
        self.colors = colors
        #print(self.contents)
        
        # converts dictionary into list, iterating new list items for the quantity of each ball provided
        for k,v in self.colors.items():
            self.list.append([k]*v)
        #flattens list of lists into a single list for easier processing.
        # note - this final list causes an error in replit because the colors aren't correctly ordered in the list, but it works fine for the purpsoes of the draw method
        for sublist in self.list:
            for item in sublist:
                self.contents.append(item)



    

    def draw(self,quantity):
        # set variable to hold the draw count for decrementing in a for loop
        draw_count = quantity
        # need to set draw list to a blank list to ensure whenever a new instance of .draw is called, it starts with a blank list!
        self.draw_list = []
        #note the list() which iterates over a copy of the list. The more obvious approach, iterate over the list itself 
        # caused weird behavior - only iterated over ~1/2 of the list

        #create a copy of contents for when this method is called multiple times in  the experiemnts function
        contents_copy = self.contents.copy()

        for ball in contents_copy:
            if draw_count > 0:
                #random.choice will randomly select a value in the list
                self.choice = random.choice(contents_copy)
                # then append it to the draw list
                self.draw_list.append(self.choice)
                # remove it from the original list
                contents_copy.remove(self.choice)
                # and decrement draw count
                draw_count -=1
        return self.draw_list


    
# function to run the draw method over a series of experiments, and calculating a probability of a particular result
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_list = []
    expected = []
    successes = 0
    experiments = num_experiments
     # much kike in .draw, this converts expected_balls into list, iterating new list items for the quantity of each ball provided
    for k,v in expected_balls.items():
            expected_list.append([k]*v)
    for sublist in expected_list:
        for item in sublist:
            expected.append(item)
    
    # runs the loop every time until # of experiments = 0
    while experiments > 0:
        # creates a copy of the draw list from .draw, using the num_balls drawn as the argument
        draw_list_copy = hat.draw((num_balls_drawn))
        #compares the draw list with the expected list, and increments successes by 1 if a match is found
        #uses counter method (imported)
        diff_list = list((Counter(expected)- Counter(draw_list_copy)).elements())
        if diff_list == []:
            successes += 1
        # decrement the experiment count
        experiments -= 1
   
  
    # calculate probability, note denominator uses original num_experiments operator, not experiments which should now = 0
    probability = successes / num_experiments
    return probability

hat = Hat(blue=3,red=2,green=6)
print(experiment(hat=hat, expected_balls={"blue":2,"green":2}, num_balls_drawn=4, num_experiments=1000))


