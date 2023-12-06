# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classdecl.
    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memberdecl.
    def visitMemberdecl(self, ctx:BKOOLParser.MemberdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributedecl.
    def visitAttributedecl(self, ctx:BKOOLParser.AttributedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrlist.
    def visitAttrlist(self, ctx:BKOOLParser.AttrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrname.
    def visitAttrname(self, ctx:BKOOLParser.AttrnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subattrlist.
    def visitSubattrlist(self, ctx:BKOOLParser.SubattrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constdecl.
    def visitConstdecl(self, ctx:BKOOLParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constattrlist.
    def visitConstattrlist(self, ctx:BKOOLParser.ConstattrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constattr.
    def visitConstattr(self, ctx:BKOOLParser.ConstattrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subconstattrlist.
    def visitSubconstattrlist(self, ctx:BKOOLParser.SubconstattrlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methoddecl.
    def visitMethoddecl(self, ctx:BKOOLParser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#staticmethods.
    def visitStaticmethods(self, ctx:BKOOLParser.StaticmethodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instancemethods.
    def visitInstancemethods(self, ctx:BKOOLParser.InstancemethodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx:BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subparamlist.
    def visitSubparamlist(self, ctx:BKOOLParser.SubparamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returntype.
    def visitReturntype(self, ctx:BKOOLParser.ReturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockstmt.
    def visitBlockstmt(self, ctx:BKOOLParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtlist.
    def visitStmtlist(self, ctx:BKOOLParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignstmt.
    def visitAssignstmt(self, ctx:BKOOLParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forstmt.
    def visitForstmt(self, ctx:BKOOLParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifstmt.
    def visitIfstmt(self, ctx:BKOOLParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakstmt.
    def visitBreakstmt(self, ctx:BKOOLParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continuestmt.
    def visitContinuestmt(self, ctx:BKOOLParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnstmt.
    def visitReturnstmt(self, ctx:BKOOLParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr1.
    def visitExpr1(self, ctx:BKOOLParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr2.
    def visitExpr2(self, ctx:BKOOLParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr3.
    def visitExpr3(self, ctx:BKOOLParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr4.
    def visitExpr4(self, ctx:BKOOLParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr5.
    def visitExpr5(self, ctx:BKOOLParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr6.
    def visitExpr6(self, ctx:BKOOLParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr7.
    def visitExpr7(self, ctx:BKOOLParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr8.
    def visitExpr8(self, ctx:BKOOLParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr9.
    def visitExpr9(self, ctx:BKOOLParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr10.
    def visitExpr10(self, ctx:BKOOLParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr11.
    def visitExpr11(self, ctx:BKOOLParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr12.
    def visitExpr12(self, ctx:BKOOLParser.Expr12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operands.
    def visitOperands(self, ctx:BKOOLParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#fieldaccess.
    def visitFieldaccess(self, ctx:BKOOLParser.FieldaccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#argumentslist.
    def visitArgumentslist(self, ctx:BKOOLParser.ArgumentslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalarvar.
    def visitScalarvar(self, ctx:BKOOLParser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraycell.
    def visitArraycell(self, ctx:BKOOLParser.ArraycellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraytype.
    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeinstancedecl.
    def visitAttributeinstancedecl(self, ctx:BKOOLParser.AttributeinstancedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literallist.
    def visitLiterallist(self, ctx:BKOOLParser.LiterallistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#subliterallist.
    def visitSubliterallist(self, ctx:BKOOLParser.SubliterallistContext):
        return self.visitChildren(ctx)



del BKOOLParser