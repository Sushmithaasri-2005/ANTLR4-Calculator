from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from calc_evaluator import CalcEvaluator

def main():
    expression = input("Enter an expression: ")
    input_stream = InputStream(expression)
    # Step 1: Create a lexer and a token stream
    lexer = CalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    # Step 2: Create a parser
    parser = CalcParser(token_stream)
    # Step 3: Parse the input expression to get the parse tree
    tree = parser.expr()
    # Step 4: Create the evaluator (listener) and walk the tree
    evaluator = CalcEvaluator()
    walker = ParseTreeWalker()
    walker.walk(evaluator, tree)
    # Step 5: Retrieve and print the result
    result = evaluator.getValue()
    print("Result:", result)

if __name__ == "__main__":
    main()

