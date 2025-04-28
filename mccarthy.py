import sys
import re

class McCarthyInterpreter:
    def __init__(self):
        self.variables = {}
        
    def evaluate_arithmetic(self, expr):
        # Handle multiplication
        if 'multiply' in expr:
            parts = expr.split('multiply')
            # Filter out empty strings and strip whitespace
            parts = [part.strip() for part in parts if part.strip()]
            if len(parts) != 3:  # Changed to expect 3 parts: num1 multiply num2
                return None
                
            # Get first number
            if parts[0] in self.variables:
                num1 = int(self.variables[parts[0]])
            else:
                num1 = int(parts[0])
                
            # Get second number
            if parts[2] in self.variables:
                num2 = int(self.variables[parts[2]])
            else:
                num2 = int(parts[2])
                
            return str(num1 * num2)
            
        # Handle addition
        if 'add' in expr:
            parts = expr.split('add')
            # Filter out empty strings and strip whitespace
            parts = [part.strip() for part in parts if part.strip()]
            if len(parts) != 2:
                return None
                
            # Get first number
            if parts[0] in self.variables:
                num1 = int(self.variables[parts[0]])
            else:
                num1 = int(parts[0])
                
            # Get second number
            if parts[1] in self.variables:
                num2 = int(self.variables[parts[1]])
            else:
                num2 = int(parts[1])
                
            return str(num1 + num2)
            
        return None
        
    def evaluate_string_operation(self, expr):
        # Handle string reversal
        if expr.startswith('reverse(') and expr.endswith(')'):
            inner = expr[8:-1].strip()
            if inner in self.variables:
                return self.variables[inner][::-1]
            elif inner.startswith('"') and inner.endswith('"'):
                return inner[1:-1][::-1]
                
        # Handle string repetition
        if expr.startswith('repeat(') and expr.endswith(')'):
            parts = expr[7:-1].split(',')
            if len(parts) == 2:
                string_part = parts[0].strip()
                count_part = parts[1].strip()
                
                # Get the string
                if string_part in self.variables:
                    string = self.variables[string_part]
                elif string_part.startswith('"') and string_part.endswith('"'):
                    string = string_part[1:-1]
                else:
                    string = string_part
                
                # Get the count
                if count_part in self.variables:
                    count = int(self.variables[count_part])
                else:
                    count = int(count_part)
                    
                return string * count
        return None
        
    def evaluate_expression(self, expr):
        # If it's just a variable name, return its value
        if expr in self.variables:
            return self.variables[expr]
            
        # Try arithmetic first
        arithmetic_result = self.evaluate_arithmetic(expr)
        if arithmetic_result is not None:
            return arithmetic_result
            
        # Try string operations next
        string_result = self.evaluate_string_operation(expr)
        if string_result is not None:
            return string_result
            
        # Handle string concatenation
        if 'concatenate' in expr:
            parts = expr.split('concatenate')
            # Filter out empty strings and strip whitespace
            parts = [part.strip() for part in parts if part.strip()]
            result = ''
            for part in parts:
                if part.startswith('"') and part.endswith('"'):
                    result += part[1:-1]
                elif part in self.variables:
                    result += str(self.variables[part])
                else:
                    result += str(part)
            return result
            
        # Handle string literals
        if expr.startswith('"') and expr.endswith('"'):
            return expr[1:-1]
        
        # Handle numbers
        if expr.isdigit():
            return expr
            
        return expr

    def execute(self, line):
        line = line.strip()
        if not line:
            return
            
        # Handle speak command
        if line.startswith('speak '):
            expr = line[6:].strip()
            value = self.evaluate_expression(expr)
            print(value)
            
        # Handle listen command
        elif line.startswith('let ') and ' equals listen' in line:
            var_name = line[4:line.index(' equals listen')].strip()
            value = input()
            self.variables[var_name] = value
            
        # Handle variable assignment
        elif ' equals ' in line and line.startswith('let '):
            parts = line[4:].split(' equals ', 1)
            var_name = parts[0].strip()
            expr = parts[1].strip()
            
            # Evaluate the expression
            if 'multiply' in expr:
                parts = expr.split('multiply')
                parts = [part.strip() for part in parts if part.strip()]
                if len(parts) == 3:  # Changed to expect 3 parts: num1 multiply num2
                    num1 = int(self.variables[parts[0]] if parts[0] in self.variables else parts[0])
                    num2 = int(self.variables[parts[2]] if parts[2] in self.variables else parts[2])
                    self.variables[var_name] = str(num1 * num2)
            else:
                value = self.evaluate_expression(expr)
                self.variables[var_name] = value

def main():
    if len(sys.argv) != 2:
        print("Usage: python mccarthy.py <program_file>")
        sys.exit(1)
        
    interpreter = McCarthyInterpreter()
    
    try:
        with open(sys.argv[1], 'r') as file:
            for line in file:
                interpreter.execute(line)
    except FileNotFoundError:
        print(f"Error: File {sys.argv[1]} not found")
        sys.exit(1)

if __name__ == "__main__":
    main() 