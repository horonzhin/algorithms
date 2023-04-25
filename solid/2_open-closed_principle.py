# Open-Closed Principle (OCP)
# Класс должен быть открыт для расширения и закрыт для модификации.

class Calculator:
    def calculate(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        # wrong
        elif operator == '%':
            return operand1 / operand2


# correct
class NewCalculator(Calculator):
    def calculate(self, operand1, operand2, operator):
        if operator == '%':
            return operand1 % operand2
        else:
            return super().calculate(operand1, operand2, operator)
