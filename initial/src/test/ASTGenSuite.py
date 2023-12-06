import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test1(self):
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test2(self):
        input = """class main {
            int a;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(Instance(),VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test3(self):
        input = """class main {
            int a;
            int b;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Instance(),VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test4(self):
        input = """class main {
            int a;
            static final int m =5,c=7,d=9;
            final static int a = 8;
            final int x=7;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(Instance(),VarDecl(Id("a"),IntType())),
             AttributeDecl(Static(),ConstDecl(Id("m"),IntType(),IntLiteral(5))),
             AttributeDecl(Static(),ConstDecl(Id("c"),IntType(),IntLiteral(7))),
             AttributeDecl(Static(),ConstDecl(Id("d"),IntType(),IntLiteral(9))),
             AttributeDecl(Static(),ConstDecl(Id("a"),IntType(),IntLiteral(8))),
             AttributeDecl(Instance(),ConstDecl(Id("x"),IntType(),IntLiteral(7)))])]))
        self.assertTrue(TestAST.test(input,expect,303))

   
        
    
