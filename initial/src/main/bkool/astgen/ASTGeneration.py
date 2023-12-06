from ast import expr, expr_context
from platform import node
from turtle import bk
from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from main.bkool.utils.AST import ArrayCell, ArrayLiteral, BoolType, BooleanLiteral, CallExpr, ConstDecl, FloatLiteral, IntLiteral, NewExpr, NullLiteral, SelfLiteral, StringLiteral, StringType, VarDecl
#from symbol import exprlist

class ASTGeneration(BKOOLVisitor):
    '''
    program: classdecl* EOF;
    '''
    def visitProgram(self,ctx:BKOOLParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])
    '''
    classdecl: CLASS ID (EXTENDS ID)? LP memdecl* RP;
    '''
    def visitClassdecl(self,ctx:BKOOLParser.ClassdeclContext):
        memdecllst = [self.visit(x) for x in ctx.memberdecl()]
        res = []
        for i in memdecllst:
            try: 
                if len(i) > 0: res = res + i
            except:
                res.append(i)
        return ClassDecl(Id(ctx.ID(0).getText()),res,Id(ctx.ID(1).getText()) if len(ctx.ID()) > 1 else None)
    '''
    memberdecl:  attributedecl | methoddecl; 
    '''
    def visitMemberdecl(self,ctx:BKOOLParser.MemberdeclContext):
        if ctx.attributedecl():
            return self.visit(ctx.attributedecl())
        return self.visit(ctx.methoddecl())
    '''
    attributedecl: vardecl | constdecl
    '''
    def visitAttributedecl(self,ctx:BKOOLParser.AttributedeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.constdecl)
    '''
    vardecl: STATIC? typ attrlist SEMI
    '''
    def visitVardecl(self,ctx:BKOOLParser.VardeclContext):
        attrlist = self.visit(ctx.attrlist())
        type = self.visit(ctx.typ())
        if ctx.STATIC():
            return [AttributeDecl(Static(),VarDecl(id,type, expr)) for (id, expr) in attrlist]
        return [AttributeDecl(Instance(), VarDecl(id, type, expr)) for (id,expr) in attrlist]
    '''
    #typ: INT | FLOAT | BOOLEAN | STRING | ID | arraytype;
    '''
    def visitTyp(self,ctx:BKOOLParser.TypContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        return self.visit(ctx.arraytype())
    '''
    #attrlist: attrname subattrlist;
    '''
    def visitAttrlist(self,ctx:BKOOLParser.AttrlistContext):
        return [self.visit(ctx.attrname())] + self.visit(ctx.subattrlist())
    '''
    #attrname: ID INITASSIGN expr | ID;
    '''
    def visitAttrname(self,ctx:BKOOLParser.AttrnameContext):
        if ctx.INITASSIGN():
            return (Id(ctx.ID().getText()), self.visit(ctx.expr()))
        return (Id(ctx.ID().getText()), None) 
    '''
    #subattrlist: COMMA attrname subattrlist | ;
    '''
    def visitSubattrlist(self,ctx:BKOOLParser.SubattrlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.attrname())] + self.visit(ctx.subattrlist())
    '''
    #constdecl: FINAL typ constattrlist SEMI | FINAL STATIC typ constattrlist SEMI | STATIC FINAL typ constattrlist SEMI;
    '''
    def visitConsdecl(self,ctx:BKOOLParser.ConstdeclContext):
        constattrlist = self.visit(ctx.constattrlist())
        type = self.visit(ctx.typ())
        if ctx.STATIC():
            return [AttributeDecl(Static(),ConstDecl(id,type,expr)) for (id,expr) in constattrlist]
        return [AttributeDecl(Instance(),ConstDecl(id, type, expr)) for (id,expr) in constattrlist]
    '''
    #constattrlist: constattr subconstattrlist;
    '''
    def visitConstattrlist(self,ctx:BKOOLParser.ConstattrlistContext):
        return [self.visit(ctx.constattr())] + self.visit(ctx.subconstattrlist())
    '''
    #constattr: ID INITASSIGN expr;
    '''
    def visitConstattr(self,ctx:BKOOLParser.ConstattrContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.expr()))
    '''
    #subconstattrlist: COMMA constattr subconstattrlist | ;
    '''
    def visitSubconstattrlist(self,ctx:BKOOLParser.SubconstattrlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.constattr())] + self.visit(cts.subconstattrlist())
    '''
    #methoddecl: staticmethods | instancemethods;
    '''
    def visitMethoddecl(self,ctx:BKOOLParser.MethoddeclContext):
        return self.visit(ctx.staticmethods()) if ctx.staticmethods() else self.visit(ctx.instancemethods())
    '''
    #staticmethods: STATIC returntype ID LB paramlist? RB blockstmt;
    '''
    def visitStaticmethods(self,ctx:BKOOLParser.StaticmethodsContext):
        return MethodDecl(Static(), Id(ctx.ID().getText()), self.visit(ctx.paramlist()) if ctx.paramlist() else[],
                          self.visit(ctx.returntype()), self.visit(ctx.blockstmt()))
    '''
    #instancemethods: returntype? ID LB paramlist? RB blockstmt;
    '''
    def visitInstancemethods(self,ctx:BKOOLParser.InstancemethodsContext):
        return MethodDecl(Instance(), Id(ctx.ID().getText()) if ctx.returntype() else Id("<init>"),
                          self.visit(ctx.paramlist()) if ctx.paramlist() else [],
                          self.visit(ctx.returntype()) if ctx.returntype() else None, self.visit(ctx.blockstmt()))
    '''
    #paramlist: param subparamlist;
    '''
    def visitParamlist(self,ctx:BKOOLParser.ParamlistContext):
        return self.visit(ctx.param()) + self.visit(ctx.subparamlist())
    '''
    #subparamlist: SEMI param subparamlist | ;
    '''
    def visitSubparamlist(self,ctx:BKOOLParser.SubparamlistContext):
        if ctx.getChildCount == 0:
            return []
        return self.visit(ctx.param()) + self.visit(ctx.subparamlist())
    '''
    #param: typ ID idlist;
    '''
    def visitParam(self,ctx:BKOOLParser.ParamContext):
        type = self.visit(ctx.typ())
        id_list = [Id(ctx.ID().getText())] + self.visit(ctx.idlist())
        return [VarDecl(id,type,None) for id in id_list]
    '''
    #returntype: typ | VOID;
    '''
    def visitReturntype(self,ctx:BKOOLParser.ReturntypeContext):
        return VoidType() if ctx.VOID() else self.visit(ctx.typ())
    '''
    #idlist: COMMA ID idlist | ;
    '''
    def visitIdlist(self,ctx:BKOOLParser.IdlistContext):
        if ctx.getChildCount() == 0:
            return [];
        retrn [Id(ctx.ID().getText())] + self.visit(ctx.idlist())
    '''
    #blockstmt: LP stmtlist RP;
    '''
    def visitBlockstmt(self,ctx:BKOOLParser.BlockstmtContext):
        return self.visit(ctx.stmtlist())
    '''
    #stmtlist: stmt stmtlist | ;
    '''
    def visitStmtlist(self,ctx:BKOOLParser.StmtlistContext):
        if getChildCount() == 0:
            return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
    '''
    #stmt: attributedecl | assignstmt | ifstmt | forstmt | breakstmt | continuestmt | returnstmt | expr SEMI;
    '''
    def visitStmt(self,ctx:BKOOLParser.StmtContext):
        if ctx.attributedecl():
            return self.visit(ctx.attributedecl())
        elif ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        return self.visit(ctx.expr())
    '''
    #assignstmt: lhs ASSIGN expr SEMI;
    '''
    def visitAssignstmt(self,ctx:BKOOLParser.AssignstmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))
    '''
    #forstmt: FOR scalarvar ASSIGN expr (TO | DOWNTO) expr DO stmt
    '''
    def visitForstmt(self,ctx:BKOOLParser.ForstmtContext):
        return For(self.visit(ctx.scalarvar()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), True if ctx.TO() else False,
                   self.visit(ctx.stmt()))
    '''
    #ifstmt: IF expr THEN stmt (ELSE stmt)? | blockstmt;
    '''
    def visitIfstmt(self,ctx:BKOOLParser.IfstmtContext):
        return If(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)) if ctx.ELSE() else None)
    '''
    #breakstmt: BREAK SEMI;
    '''
    def visitBreakstmt(self,ctx:BKOOLParser.BreakstmtContext):
        return Break()
    '''
    #continuestmt: CONTINUE SEMI;
    '''
    def visitContinuestmt(self,ctx:BKOOLParser.ContinuestmtContext):
        return Continue()
    '''
    #returnstmt: RETURN expr SEMI;
    '''
    def visitReturnstmt(self,ctx:BKOOLParser.ReturnstmtContext):
        return Return(self.visit(ctx.expr()))
    '''
    #expr: expr OP0 expr1 | expr1;
    '''
    def visitExpr(self,ctx:BKOOLParser.ExprContext):
        left = expr
        right = expr1
        other = expr1
        if ctx.other:
            return self.visit(ctx.other)
        return BinaryOP(ctx.OP0().getText(), self.visit(ctx.left), self.visit(ctx.right))
    '''
    #expr1: expr1 OP1 expr2 | expr2;
    '''
    def visitExpr1(self,ctx:BKOOLParser.Expr2Context):
        left = expr1
        right = expr2
        other = expr2
        if ctx.other:
            return self.visit(ctx.other)
        return BinaryOP(ctx.OP1().getText(), self.visit(ctx.left), self.visit(ctx.right))
    '''
    #expr2: expr3 OP2 expr3 | expr3;
    '''
    def visitExpr2(self,ctx:BKOOLParser.Expr2Context):
        left = expr3
        right = expr3
        other = expr3
        if ctx.other:
            return self.visit(ctx.other)
        return BinaryOP(ctx.OP2().getText(), self.visit(ctx.left), self.visit(ctx.right))
    '''
    #expr3: expr4 OP3 expr4 | expr4;
    '''
    def visitExpr3(self,ctx:BKOOLParser.Expr3Context):
        left = expr4
        right = expr4
        other = expr4
        if ctx.other:
            return self.visit(ctx.other)
        return BinaryOP(ctx.OP3().getText(), self.visit(ctx.left), self.visit(ctx.right))
    '''
    #expr4: expr4 OP4 expr5 | expr5;
    '''
    def visitExpr4(self,ctx:BKOOLParser.Expr4Context):
        left = expr4
        right = expr5
        other = expr5
        if ctx.other:
            return self.visit(ctx.other)
        return BinaryOP(ctx.OP4().getText(), self.visit(ctx.left), self.visit(ctx.right))
    '''
    #expr5: NOT expr5 | expr6
    '''
    def visitExpr5(self,ctx:BKOOLParser.Expr5Context):
        right = expr5
        orther = expr6
        if ctx.other:
            return self.visit(ctx.other)
        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.right))
    '''
    #expr6: expr6 CONCAT expr7 | expr7;
    '''
    def visitExpr6(self,ctx:BKOOLParser.Expr6Context):
        left = expr6
        right = expr7
        other = expr7
        if ctx.other:
            return self.visit(ctx.other)
        return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.left), self.visit(ctx.right))
    '''
    #expr7: expr8 LSB expr RSB | expr8;
    '''
    def visitExpr7(self,ctx:BKOOLParser.Expr7Context):
        left = expr8
        right = expr
        other = expr8
        if ctx.other:
            return self.visit(ctx.other)
        return ArrayCell(self.visit(ctx.left), self.visit(ctx.right))
    '''
    #expr8: expr8 DOT ID | expr8 DOT ID LB exprlist RB | expr9;
    '''
    def visitExpr8(self,ctx:BKOOLParser.Expr8Context):
        left = expr8
        right = exprlist
        other = expr9
        if ctx.other:
            return self.visit(ctx.other)
        elif ctx.right:
            return CallExpr(self.visit(ctx.left), Id(ctx.ID().getText()), self.visit(ctx.right))
        return FieldAccess(self.visit(ctx.left), Id(ctx.ID().getText()))
    '''
    #expr9: NEW ID LB exprlist RB | expr10;
    '''
    def visitExpr9(self,ctx:BKOOLParser.Expr9Context):
        left = exprlist
        other = expr10
        if ctx.other:
            return self.visit(ctx.other)
        return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.left))
    '''
    #expr10: LP exprlist RP | expr11;
    '''
    def visitExpr10(self,ctx:BKOOLParser.Expr10Context):
        left = exprlist
        other = expr11
        if ctx.other:
            return self.visit(ctx.other)
        return ArrayLiteral(self.visit(ctx.left))
    '''
    #expr11: LB expr RB | expr12;
    '''
    def visitExpr11(self,ctx:BKOOLParser.Expr11Context):
        left = expr
        other = expr12
        if ctx.other:
            return self.visit(ctx.other)
        return self.visit(ctx.left)
    '''
    #expr12: OP0 expr12 | operands;
    '''
    def visitExpr12(self,ctx:BKOOLParser.Expr12Context):
        right = expr12
        other = operands
        if ctx.other:
            return self.visit(ctx.other)
        return UnaryOp(ctx.OP0().getText(),self.visit(ctx.right))
    '''
    #operands: THIS | INTLIT | FLOATLIT | TRUE | FALSE | NIL | ID | STRLIT;
    '''
    def visitOperands(self,ctx:BKOOLParser.OperandsContext):
        if ctx.THIS():
            return SelfLiteral()
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        return StringLiteral(ctx.STRLIT().getText())
    '''
    #exprlist: expr argumentslist | ;
    '''
    def visitExprlist(self,ctx:BKOOLParser.ExprlistContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expr())] + self.visit(ctx.argumentslist())
    '''
    #fieldaccess: expr DOT ID | expr DOT ID LB exprlist RB | ID DOT ID | ID DOT ID LB exprlist RB;
    '''
    def visitFieldaccess(self,ctx:BKOOLParser.FieldaccessContext):
        left = expr
        right = exprlist
        if ctx.right:
            return CallExpr(self.visit(ctx.left), Id(ctx.ID().getText()), self.visit(ctx.right))
        return FieldAccess(self.visit(ctx.left), Id(ctx.ID().getText()))
    '''
    #argumentslist: COMMA expr argumentslist | ;
    '''
    def visitArgumentslist(self,ctx:BKOOLParser.ArgumentslistContext):
        if getChildCount() == 0:
            return []
        return [self.visit(ctx.expr())] + self.visit(ctx.argumentslist())
    '''
    #scalarvar: ID;
    '''
    def visitScalarvar(self,ctx:BKOOLParser.ScalarvarContext):
        return Id(ctx.ID().getText())
    '''
    #lhs: ID | arraycell | fieldaccess;
    '''
    def visitLhs(self,ctx:BKOOLParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arraycell():
            return self.visit(ctx.arraycell())
        return self.visit(ctx.fieldaccess())
    '''
    #arraycell: expr LSB expr RSB;
    '''
    def visitArraycell(self,ctx:BKOOLParser.ArraycellContext):
        left = expr(0)
        right = expr(1)
        return ArrayCell(self.visit(ctx.left), self.visit(ctx.right))
    '''
    #arraytype: (FLOAT | INT | BOOLEAN | STRING | ID) LSB INTLIT RSB;
    '''
    def visitArraytype(self,ctx:BKOOLParser.ArraytypeContext):
        sz = int(ctx.INTLIT().getText())
        if ctx.FLOAT():
            return ArrayType(sz, FloatType())
        elif ctx.INT():
            return ArrayType(sz, IntType())
        elif ctx.BOOLEAN():
            return ArrayType(sz, BoolType())
        elif ctx.STRING():
            return ArrayType(sz, StringType())
        return ArrayType(sz, ClassType(Id(ctx.ID().getText())))
    '''
    #attributeinstancedecl: typ attrlist SEMI | FINAL typ constattrlist SEMI ;
    '''
    def visitAttributeinstancedecl(self,ctx:BKOOLParser.AttributeinstancedeclContext):
        if ctx.FINAL():
            constattrlist = self.visit(ctx.constattrlist())
            type = self.visit(ctx.typ());
            return [ConstDecl(id, type, expr) for (id, expr) in constattrlist]
        else:
            attrlist = self.visit(ctx.attrlist())
            type = self.visit(ctx.typ())
            return [VarDecl(id, type, expr) for (id, expr) in attrlist]
    '''
    #literallist: literal subliterallist | ;
    '''
    def visitLiterallist(self, ctx:BKOOLParser.LiterallistContext):
        if getChildCount() == 0:
            return []
        return [self.visit(ctx.literal())] + self.visit(ctx.suliterallist())
    '''
    #subliterallist: COMMA literal subliterallist | ;
    '''
    def visitSubliterallist(self, ctx:BKOOLParser.SubliterallistContext):
        if getChildCount() == 0:
            return []
        return [self.visit(ctx.literal())] + self.visit(ctx.subliterallist())
    '''
    #literal: FLOATLIT | INTLIT | TRUE | FALSE | NIL | STRLIT | THIS;
    '''
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NullLiteral()
        elif ctx.STRLIT():
            return StringLiteral(ctx.STRLIT().getText())
        return SelfLiteral()