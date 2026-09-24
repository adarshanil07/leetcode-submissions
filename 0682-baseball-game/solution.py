class Solution(object):
    def calPoints(self, operations):
        score = 0
        record = []

        for operation in operations:

            try: 
                int(operation)
                record.append(int(operation))
            
            except ValueError:
                if operation == "C":
                    record.pop()

                elif operation == "D":
                    self.double(record)
                    
                elif operation == "+":
                    self.addition(record)

        return sum(record)
                

    
    def addition(self, record):
        num1 = record[-1]
        num2 = record[-2]
        record.append(num1 + num2)
    
    def double(self, record):
        num = record[-1]
        record.append(num * 2)


        
