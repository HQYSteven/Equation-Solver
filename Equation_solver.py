'''
This is a file contains a script which can solve solving equation
'''
import sys
import math


class equationSolver(object):
    def __init__(self) -> None:
        self.equationSlice = []
        self.equation = ''
        self.equationType = None
        self.left = []
        self.right = []
        self. a = 1
        self.b = 0
        self.debug = False
        self.c = 0
        self.helpPage = '''
Thank You For Using Equation Solver
Options:
--help/-h                              The help Page
--univariate-one-degree/-uo            What You Want To Solve is univariate one degree equation(kx+b=0)
--univariate-binary/ub                 What You Want To Solve is univariate binary equation(ax^2+bx+c = 0)
--equation/-e                          Type The equation*(ax^2 + bx + c = 0,for example)
--debug/d                              Debug Mode
'''

    def preparations(self, args: list) -> None:
        # Get the length of the keyboard options
        equationFollowing = False
        argLength = len(args)
        if argLength == 1:
            print(self.helpPage)
        if argLength >= 1:
            for option in args:
                if equationFollowing:
                    self.equation = option
                    print(f"Get The Equation:{self.equation}")
                    equationFollowing = False
                if (option == '--univariate-one-degree' or option == "-uo"):
                    self.equationType = 0
                if (option == "--univariate-binary" or option == '-ub'):
                    self.equationType = 1
                if (option == '--equation' or option == '-e'):
                    equationFollowing = True
                if (option == '--debug' or option == '-d'):
                    self.debug = True

    def sliceEquation(self) -> None:
        temp = ''
        for string in self.equation:
            if string in ["+", "-", "*", "=", "(", ")"]:
                if temp != "":
                    self.equationSlice.append(temp)

                self.equationSlice.append(string)
                temp = ''
                continue
            temp += string if string != " " else ""
        self.equationSlice.append(temp)
        for temp in self.equationSlice:
            if "/" in temp:
                num1 = ""
                num2 = ""
                second = False
                for s in temp:
                    if s == "/":
                        second = True
                        continue
                    if not second:
                        num1 += s
                    else:
                        num2 += s if s != "x" else ""
                index = self.equationSlice.index(temp)
                temp = float(num1)/float(num2)
                self.equationSlice[index] = str(temp)
        if self.debug:
            print(
            f"[Slice]:Succeed in Slicing The Equation:                                                  {','.join(self.equationSlice)}\n")

    def divide(self) -> None:
        right = False
        for temp in self.equationSlice:
            if temp != "=":
                if not right:
                    self.left.append(temp)
                if right:
                    self.right.append(temp)
            else:
                right = True
        print(
            f"[divide]:item divided :                                                                   left:{''.join(self.left)},right:{''.join(self.right)}\n")

    def shift(self) -> None:
        if self.right != ["0"]:
            newRight = []
            if "-" not in self.right[0] and "+" not in self.right[0]:
                    self.right.insert(0, "+")
            if self.equationType == 1:
                for string in self.right:
                    if string in ["+", "-",]:
                        self.left.append("+"if string == "-" else "-")
                        continue
                    self.left.append(string)
                self.right = ["0"]
            if self.equationType == 0:
                sAppended = False
                for string in self.right:
                    if string in ["+", "-",]:
                        self.left.append("+"if string == "-" else "-")
                        sAppended = True
                        continue
                    if "x" in string:
                        self.left.append(string)
                        sAppended = False
                    else:
                        if sAppended == True:
                            if self.left[-1] == "-":
                                newRight.append("+")
                            else:
                                newRight.append("-")
                            del self.left[-1]
                        else:
                            newRight.append("+")
                        newRight.append(string)
                self.right = newRight
        if self.debug:
            print(
            f"[shift]:Item Shifted :                                                                    {''.join(self.left)} = {''.join(self.right)}\n")

    def classify(self) -> None:
        self.oneTermList = []
        self.twoTermList = []
        self.constantList = ["0"]
        if self.equationType == 1:
            
            index = 0
            for temp in self.left:
                if "x" in temp and "^" not in temp:
                    temp = self.left[index-1]+temp
                    self.oneTermList.append(temp)
                elif "x" in temp and "^" in temp:
                    temp = self.left[index-1]+temp
                    self.twoTermList.append(temp)
                elif temp not in ["+", "-", "*",]:
                    temp = self.left[index-1]+temp
                    self.constantList.append(temp)
                index += 1
            print("[Classify]:This is a univariate binary equation")
            print(f"[Classify]:Get One Term One-order term :                                                  {','.join(self.oneTermList)}\n\
           Get Two-order Term :                                                           {','.join(self.twoTermList)},\n\
           Get Constants:                                                                 {','.join(self.constantList)}\n")
        if self.equationType == 0:
            index = 0
            for temp in self.left:
                if "x" in temp:
                    temp = self.left[index-1]+temp
                    self.oneTermList.append(temp)
                index +=1
            index =0
            for temp in self.right:
                if temp not in ["+", "-", "*",]:
                    temp = self.right[index-1]+temp
                    self.constantList.append(temp)
                index += 1

            print("[Classify]:This is a univariate one-degree equation")        
            print(f"[Classify]:Get one-degree term :                                                          {','.join(self.oneTermList)}\n\
           Get Constants:                                                                 {','.join(self.constantList)}\n")

    def combine(self) -> None:
        if self.equationType == 1:
            two_term_coefficient_list = []

            for temp2 in self.twoTermList:
                temp2 = temp2[:-3:]
                if temp2 == "+" or temp2 == "-":
                    temp2 += '1'
                two_term_coefficient_list.append(temp2)
            two_Term_coefficient_new = 0
            for num in two_term_coefficient_list:
                two_Term_coefficient_new += float(num)
            print(
                f"[Combine]:Combine The two term coefficients -> New two term coefficient:                  {two_Term_coefficient_new}\n")
            self.a = two_Term_coefficient_new
        
        constant_new = 0
        
        for num in self.constantList:
            constant_new += float(num)
        self.c = constant_new
        print(
            f"[Combine]:Combine The Constants -> New Constant:                                          {constant_new}\n")

        One_Term_coefficient_List = []

        for temp in self.oneTermList:
            temp = temp[:-1:]
            if temp == "+" or temp == "-":
                temp += '1'
            One_Term_coefficient_List.append(temp)
        One_Term_coefficient_new = 0
        for num in One_Term_coefficient_List:
            One_Term_coefficient_new += float(num)
        print(
            f"[Combine]:Combine The one term coefficients -> New one term coefficient:                  {One_Term_coefficient_new}\n")
        self.b = One_Term_coefficient_new

    def calculate(self):

        self.result1 = 0
        self.result2 = 0
        if self.equationType == 1:
            delta = self.b*self.b - 4*self.a*self.c
            print(
                f"[Delta]:Calculate Delta:                                                                  {delta}\n")
            if delta > 0:
                self.result1 = (-self.b+math.sqrt(delta))/(self.a*2)
                self.result2 = (-self.b-math.sqrt(delta))/(self.a*2)
                print(f"[Result]: X1 = {self.result1},X2 = {self.result2}")
            if delta == 0:
                self.result1 = (-self.b+math.sqrt(delta))/(self.a*2)
                print(f"[Result]: X1 = X2 = {self.result1}")
            if delta < 0:
                print("It has no root!")
        if self.equationType == 0:
            if self.b == 0:
                print("[Calculate]: There is no solution! (dividing zero)")
            else:
                self.result1 = self.c/self.b
                print(f"[Calculate]:Result: x = {self.result1} ")


arg = sys.argv
self = equationSolver()
equationSolver.preparations(self, arg)
equationSolver.sliceEquation(self)
equationSolver.divide(self)
equationSolver.shift(self)
equationSolver.classify(self)
equationSolver.combine(self)
equationSolver.calculate(self)
