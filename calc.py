import sys


class CodingTest:

    #instance of a dictionary of parsed argument. initially set to empty 
    already_calculated_dictionary = {}
    
    
    #Checks if the position in the iteration has been parsed already (checks if the argument is in the dictionary already)
    def position_checker(self, s_expression):
        
        if s_expression in self.already_calculated_dictionary:
            not_calculated = {} 
            
            return True
        else:
            not_calculated = {s_expression}
            return False


            
        
    #iterates over the argument and parses the expression
    #keeps track of what expression is tracked 
    def register(self, s_expression):
        
        #Since we know that the last value in the expression would be ')' we can use that as the condition
        while ')' in s_expression:

            #we know that the last value in the expression is '(' so that would be the start point
            startpoint = s_expression[:s_expression.index(')')].rindex('(')

            #we know that the last value in the expression is ')' so that would be the end point
            endpoint = s_expression.index(')')

            #Checks if the expressions has not been iterated over yet
            already_calculated = self.position_checker(s_expression)
            if already_calculated:
                return self.already_calculated_dictionary[s_expression]

            #we set a  'value' which takes a complete parsed argument with no nested expressions and send it to multiplexer 
            value = self.multiplexer(s_expression[startpoint + 1:endpoint])

            
            if startpoint == 0:
                return value

            
            else:
                s_expression = s_expression[:startpoint] + str(value) + s_expression[endpoint+1:]

        return int(s_expression)
    #encode the expression first splits it into arguments
    #then checks if it is to be added, multiplied or something else
    def calculator_encoder(self, s_expression):
        
        splited_expression = self.splitter_function (s_expression)
        if splited_expression[0] == 'add':
            summed_value = self.adder(splited_expression[1], splited_expression[2])
            return summed_value
            
        elif splited_expression[0] == 'multiply':
            multiplied_value = self.multiplier(splited_expression[1], splited_expression[2])
            return multiplied_value

        else:
            value = int(s_expression)
            return value
        
    #adder function (adds exactly two numbers)
    def adder(self, x , y):
        added_value = int(x)+int(y)
        return added_value
    
    #multiplier function (multiplies exactly two numbers)
    def multiplier (self,x , y):
        
        multiplied_value = int(x)* int(y)
        return multiplied_value
    
    #Splits expression into 3 arguments, one string, 2 ints
    def splitter_function(self,s_expression):
        expression = s_expression.split()

        return expression


    #combines all the functions together

    def multiplexer(self, s_expression):
        # we check if the expression has not been calculated yet
        if s_expression in self.already_calculated_dictionary:
            return self.already_calculated_dictionary[s_expression]
        
        #if it has not, we then send it to the encoder
        value = self.calculator_encoder(s_expression)


        #We return the value then add the expression into the dictionary to keep track of calculated expressions
        self.already_calculated_dictionary[s_expression] = value
        return value

    
    

def main():
    if len(sys.argv)<2:
        print('No Arguments were passed. Please try again')
    else:
        calculated_value = CodingTest().register(sys.argv[1])
        print(calculated_value)


if __name__ == '__main__':
    main()
        

