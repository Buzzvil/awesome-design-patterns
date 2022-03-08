from example import AbstractExpression, Add, Number, Subtract

from typing import List

sentence = "5 + 4 - 3 + 7 - 2"
print(sentence)

token = sentence.split(" ")
print(token)

AST: List[AbstractExpression] = []
# init
AST.append(Add(Number(token[0]), Number(token[2]))) if token[1] == "+" else AST.append(Subtract(Number(token[0]), Number(token[2])))
  
for i in range(4, len(token), 2):
  if token[i-1] == "+":
    AST.append(Add(AST[(i-4)//2], Number(token[i])))
  elif token[i-1] == "-":
    AST.append(Subtract(AST[(i-4)//2], Number(token[i])))

AST_root = AST.pop()
print(AST_root.interpret())
print(AST_root)

