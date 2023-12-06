# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u0193\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0103\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u010b\n\35\3\36")
        buf.write("\3\36\3\36\3\36\5\36\u0111\n\36\3\37\3\37\3 \3 \3!\3!")
        buf.write("\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3+\3+\3,\3,\3-\6-\u0131\n-\r-\16-\u0132\3.\3.")
        buf.write("\3.\7.\u0138\n.\f.\16.\u013b\13.\3.\5.\u013e\n.\3.\3.")
        buf.write("\3.\5.\u0143\n.\3/\3/\5/\u0147\n/\3/\3/\3\60\6\60\u014c")
        buf.write("\n\60\r\60\16\60\u014d\3\60\3\60\3\61\3\61\3\61\3\61\7")
        buf.write("\61\u0156\n\61\f\61\16\61\u0159\13\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\62\3\62\7\62\u0162\n\62\f\62\16\62\u0165\13")
        buf.write("\62\3\62\3\62\3\63\3\63\5\63\u016b\n\63\3\63\6\63\u016e")
        buf.write("\n\63\r\63\16\63\u016f\3\64\3\64\3\64\3\65\3\65\3\65\3")
        buf.write("\66\3\66\7\66\u017a\n\66\f\66\16\66\u017d\13\66\3\67\3")
        buf.write("\67\7\67\u0181\n\67\f\67\16\67\u0184\13\67\38\38\38\3")
        buf.write("9\39\39\39\3:\3:\5:\u018f\n:\3:\3:\3:\3\u0157\2;\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\2g\2i\2k\2m\64o\65q\66s\67\3")
        buf.write("\2\f\4\2--//\6\2\'\',,\61\61^^\3\2\62;\5\2\13\f\16\17")
        buf.write("\"\"\4\2\f\f\16\17\4\2GGgg\t\2$$^^ddhhppttvv\6\2\f\f\16")
        buf.write("\17$$^^\5\2C\\aac|\6\2\62;C\\aac|\2\u01a1\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3")
        buf.write("\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5}\3\2\2\2\7\u0083\3\2\2")
        buf.write("\2\t\u0089\3\2\2\2\13\u0092\3\2\2\2\r\u0095\3\2\2\2\17")
        buf.write("\u009a\3\2\2\2\21\u00a2\3\2\2\2\23\u00a8\3\2\2\2\25\u00ab")
        buf.write("\3\2\2\2\27\u00af\3\2\2\2\31\u00b3\3\2\2\2\33\u00ba\3")
        buf.write("\2\2\2\35\u00bf\3\2\2\2\37\u00c3\3\2\2\2!\u00ca\3\2\2")
        buf.write("\2#\u00cf\3\2\2\2%\u00d5\3\2\2\2\'\u00da\3\2\2\2)\u00de")
        buf.write("\3\2\2\2+\u00e3\3\2\2\2-\u00e9\3\2\2\2/\u00f0\3\2\2\2")
        buf.write("\61\u00f3\3\2\2\2\63\u00fa\3\2\2\2\65\u00fc\3\2\2\2\67")
        buf.write("\u0102\3\2\2\29\u010a\3\2\2\2;\u0110\3\2\2\2=\u0112\3")
        buf.write("\2\2\2?\u0114\3\2\2\2A\u0116\3\2\2\2C\u0119\3\2\2\2E\u011b")
        buf.write("\3\2\2\2G\u011d\3\2\2\2I\u011f\3\2\2\2K\u0121\3\2\2\2")
        buf.write("M\u0123\3\2\2\2O\u0125\3\2\2\2Q\u0127\3\2\2\2S\u0129\3")
        buf.write("\2\2\2U\u012b\3\2\2\2W\u012d\3\2\2\2Y\u0130\3\2\2\2[\u0142")
        buf.write("\3\2\2\2]\u0144\3\2\2\2_\u014b\3\2\2\2a\u0151\3\2\2\2")
        buf.write("c\u015f\3\2\2\2e\u0168\3\2\2\2g\u0171\3\2\2\2i\u0174\3")
        buf.write("\2\2\2k\u017b\3\2\2\2m\u017e\3\2\2\2o\u0185\3\2\2\2q\u0188")
        buf.write("\3\2\2\2s\u018c\3\2\2\2uv\7d\2\2vw\7q\2\2wx\7q\2\2xy\7")
        buf.write("n\2\2yz\7g\2\2z{\7c\2\2{|\7p\2\2|\4\3\2\2\2}~\7d\2\2~")
        buf.write("\177\7t\2\2\177\u0080\7g\2\2\u0080\u0081\7c\2\2\u0081")
        buf.write("\u0082\7m\2\2\u0082\6\3\2\2\2\u0083\u0084\7e\2\2\u0084")
        buf.write("\u0085\7n\2\2\u0085\u0086\7c\2\2\u0086\u0087\7u\2\2\u0087")
        buf.write("\u0088\7u\2\2\u0088\b\3\2\2\2\u0089\u008a\7e\2\2\u008a")
        buf.write("\u008b\7q\2\2\u008b\u008c\7p\2\2\u008c\u008d\7v\2\2\u008d")
        buf.write("\u008e\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090\7w\2\2\u0090")
        buf.write("\u0091\7g\2\2\u0091\n\3\2\2\2\u0092\u0093\7f\2\2\u0093")
        buf.write("\u0094\7q\2\2\u0094\f\3\2\2\2\u0095\u0096\7g\2\2\u0096")
        buf.write("\u0097\7n\2\2\u0097\u0098\7u\2\2\u0098\u0099\7g\2\2\u0099")
        buf.write("\16\3\2\2\2\u009a\u009b\7g\2\2\u009b\u009c\7z\2\2\u009c")
        buf.write("\u009d\7v\2\2\u009d\u009e\7g\2\2\u009e\u009f\7p\2\2\u009f")
        buf.write("\u00a0\7f\2\2\u00a0\u00a1\7u\2\2\u00a1\20\3\2\2\2\u00a2")
        buf.write("\u00a3\7h\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7q\2\2\u00a5")
        buf.write("\u00a6\7c\2\2\u00a6\u00a7\7v\2\2\u00a7\22\3\2\2\2\u00a8")
        buf.write("\u00a9\7k\2\2\u00a9\u00aa\7h\2\2\u00aa\24\3\2\2\2\u00ab")
        buf.write("\u00ac\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7v\2\2\u00ae")
        buf.write("\26\3\2\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7g\2\2\u00b1")
        buf.write("\u00b2\7y\2\2\u00b2\30\3\2\2\2\u00b3\u00b4\7u\2\2\u00b4")
        buf.write("\u00b5\7v\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7k\2\2\u00b7")
        buf.write("\u00b8\7p\2\2\u00b8\u00b9\7i\2\2\u00b9\32\3\2\2\2\u00ba")
        buf.write("\u00bb\7v\2\2\u00bb\u00bc\7j\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write("\u00be\7p\2\2\u00be\34\3\2\2\2\u00bf\u00c0\7h\2\2\u00c0")
        buf.write("\u00c1\7q\2\2\u00c1\u00c2\7t\2\2\u00c2\36\3\2\2\2\u00c3")
        buf.write("\u00c4\7t\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7v\2\2\u00c6")
        buf.write("\u00c7\7w\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7p\2\2\u00c9")
        buf.write(" \3\2\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc\7t\2\2\u00cc")
        buf.write("\u00cd\7w\2\2\u00cd\u00ce\7g\2\2\u00ce\"\3\2\2\2\u00cf")
        buf.write("\u00d0\7h\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7n\2\2\u00d2")
        buf.write("\u00d3\7u\2\2\u00d3\u00d4\7g\2\2\u00d4$\3\2\2\2\u00d5")
        buf.write("\u00d6\7x\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7k\2\2\u00d8")
        buf.write("\u00d9\7f\2\2\u00d9&\3\2\2\2\u00da\u00db\7p\2\2\u00db")
        buf.write("\u00dc\7k\2\2\u00dc\u00dd\7n\2\2\u00dd(\3\2\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\u00e0\7j\2\2\u00e0\u00e1\7k\2\2\u00e1")
        buf.write("\u00e2\7u\2\2\u00e2*\3\2\2\2\u00e3\u00e4\7h\2\2\u00e4")
        buf.write("\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7c\2\2\u00e7")
        buf.write("\u00e8\7n\2\2\u00e8,\3\2\2\2\u00e9\u00ea\7u\2\2\u00ea")
        buf.write("\u00eb\7v\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7v\2\2\u00ed")
        buf.write("\u00ee\7k\2\2\u00ee\u00ef\7e\2\2\u00ef.\3\2\2\2\u00f0")
        buf.write("\u00f1\7v\2\2\u00f1\u00f2\7q\2\2\u00f2\60\3\2\2\2\u00f3")
        buf.write("\u00f4\7f\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6\7y\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7q\2\2\u00f9")
        buf.write("\62\3\2\2\2\u00fa\u00fb\t\2\2\2\u00fb\64\3\2\2\2\u00fc")
        buf.write("\u00fd\t\3\2\2\u00fd\66\3\2\2\2\u00fe\u00ff\7?\2\2\u00ff")
        buf.write("\u0103\7?\2\2\u0100\u0101\7#\2\2\u0101\u0103\7?\2\2\u0102")
        buf.write("\u00fe\3\2\2\2\u0102\u0100\3\2\2\2\u01038\3\2\2\2\u0104")
        buf.write("\u010b\7@\2\2\u0105\u0106\7@\2\2\u0106\u010b\7?\2\2\u0107")
        buf.write("\u010b\7>\2\2\u0108\u0109\7>\2\2\u0109\u010b\7?\2\2\u010a")
        buf.write("\u0104\3\2\2\2\u010a\u0105\3\2\2\2\u010a\u0107\3\2\2\2")
        buf.write("\u010a\u0108\3\2\2\2\u010b:\3\2\2\2\u010c\u010d\7(\2\2")
        buf.write("\u010d\u0111\7(\2\2\u010e\u010f\7~\2\2\u010f\u0111\7~")
        buf.write("\2\2\u0110\u010c\3\2\2\2\u0110\u010e\3\2\2\2\u0111<\3")
        buf.write("\2\2\2\u0112\u0113\7#\2\2\u0113>\3\2\2\2\u0114\u0115\7")
        buf.write("`\2\2\u0115@\3\2\2\2\u0116\u0117\7<\2\2\u0117\u0118\7")
        buf.write("?\2\2\u0118B\3\2\2\2\u0119\u011a\7?\2\2\u011aD\3\2\2\2")
        buf.write("\u011b\u011c\7*\2\2\u011cF\3\2\2\2\u011d\u011e\7+\2\2")
        buf.write("\u011eH\3\2\2\2\u011f\u0120\7]\2\2\u0120J\3\2\2\2\u0121")
        buf.write("\u0122\7_\2\2\u0122L\3\2\2\2\u0123\u0124\7}\2\2\u0124")
        buf.write("N\3\2\2\2\u0125\u0126\7\177\2\2\u0126P\3\2\2\2\u0127\u0128")
        buf.write("\7=\2\2\u0128R\3\2\2\2\u0129\u012a\7<\2\2\u012aT\3\2\2")
        buf.write("\2\u012b\u012c\7\60\2\2\u012cV\3\2\2\2\u012d\u012e\7.")
        buf.write("\2\2\u012eX\3\2\2\2\u012f\u0131\t\4\2\2\u0130\u012f\3")
        buf.write("\2\2\2\u0131\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133Z\3\2\2\2\u0134\u0135\5Y-\2\u0135\u0139")
        buf.write("\7\60\2\2\u0136\u0138\t\4\2\2\u0137\u0136\3\2\2\2\u0138")
        buf.write("\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a\u013d\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013e\5")
        buf.write("e\63\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0143")
        buf.write("\3\2\2\2\u013f\u0140\5Y-\2\u0140\u0141\5e\63\2\u0141\u0143")
        buf.write("\3\2\2\2\u0142\u0134\3\2\2\2\u0142\u013f\3\2\2\2\u0143")
        buf.write("\\\3\2\2\2\u0144\u0146\7$\2\2\u0145\u0147\5k\66\2\u0146")
        buf.write("\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u0149\7$\2\2\u0149^\3\2\2\2\u014a\u014c\t\5\2\2")
        buf.write("\u014b\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014b\3")
        buf.write("\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150")
        buf.write("\b\60\2\2\u0150`\3\2\2\2\u0151\u0152\7\61\2\2\u0152\u0153")
        buf.write("\7,\2\2\u0153\u0157\3\2\2\2\u0154\u0156\13\2\2\2\u0155")
        buf.write("\u0154\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0157\u0155\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157\3")
        buf.write("\2\2\2\u015a\u015b\7,\2\2\u015b\u015c\7\61\2\2\u015c\u015d")
        buf.write("\3\2\2\2\u015d\u015e\b\61\2\2\u015eb\3\2\2\2\u015f\u0163")
        buf.write("\7%\2\2\u0160\u0162\n\6\2\2\u0161\u0160\3\2\2\2\u0162")
        buf.write("\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0166\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\b")
        buf.write("\62\2\2\u0167d\3\2\2\2\u0168\u016a\t\7\2\2\u0169\u016b")
        buf.write("\t\2\2\2\u016a\u0169\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("\u016d\3\2\2\2\u016c\u016e\t\4\2\2\u016d\u016c\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u0170f\3\2\2\2\u0171\u0172\7^\2\2\u0172\u0173\t")
        buf.write("\b\2\2\u0173h\3\2\2\2\u0174\u0175\7^\2\2\u0175\u0176\n")
        buf.write("\b\2\2\u0176j\3\2\2\2\u0177\u017a\n\t\2\2\u0178\u017a")
        buf.write("\5g\64\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a")
        buf.write("\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017cl\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0182\t\n\2")
        buf.write("\2\u017f\u0181\t\13\2\2\u0180\u017f\3\2\2\2\u0181\u0184")
        buf.write("\3\2\2\2\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183")
        buf.write("n\3\2\2\2\u0184\u0182\3\2\2\2\u0185\u0186\13\2\2\2\u0186")
        buf.write("\u0187\b8\3\2\u0187p\3\2\2\2\u0188\u0189\7$\2\2\u0189")
        buf.write("\u018a\5k\66\2\u018a\u018b\b9\4\2\u018br\3\2\2\2\u018c")
        buf.write("\u018e\7$\2\2\u018d\u018f\5k\66\2\u018e\u018d\3\2\2\2")
        buf.write("\u018e\u018f\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\5")
        buf.write("i\65\2\u0191\u0192\b:\5\2\u0192t\3\2\2\2\24\2\u0102\u010a")
        buf.write("\u0110\u0132\u0139\u013d\u0142\u0146\u014d\u0157\u0163")
        buf.write("\u016a\u016f\u0179\u017b\u0182\u018e\6\b\2\2\38\2\39\3")
        buf.write("\3:\4")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN = 1
    BREAK = 2
    CLASS = 3
    CONTINUE = 4
    DO = 5
    ELSE = 6
    EXTENDS = 7
    FLOAT = 8
    IF = 9
    INT = 10
    NEW = 11
    STRING = 12
    THEN = 13
    FOR = 14
    RETURN = 15
    TRUE = 16
    FALSE = 17
    VOID = 18
    NIL = 19
    THIS = 20
    FINAL = 21
    STATIC = 22
    TO = 23
    DOWNTO = 24
    OP0 = 25
    OP1 = 26
    OP2 = 27
    OP3 = 28
    OP4 = 29
    NOT = 30
    CONCAT = 31
    ASSIGN = 32
    INITASSIGN = 33
    LB = 34
    RB = 35
    LSB = 36
    RSB = 37
    LP = 38
    RP = 39
    SEMI = 40
    CL = 41
    DOT = 42
    COMMA = 43
    INTLIT = 44
    FLOATLIT = 45
    STRLIT = 46
    WS = 47
    COMMENT = 48
    LINECOMMENT = 49
    ID = 50
    ERROR_CHAR = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESCAPE = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'break'", "'class'", "'continue'", "'do'", "'else'", 
            "'extends'", "'float'", "'if'", "'int'", "'new'", "'string'", 
            "'then'", "'for'", "'return'", "'true'", "'false'", "'void'", 
            "'nil'", "'this'", "'final'", "'static'", "'to'", "'downto'", 
            "'!'", "'^'", "':='", "'='", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "';'", "':'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
            "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", "RETURN", 
            "TRUE", "FALSE", "VOID", "NIL", "THIS", "FINAL", "STATIC", "TO", 
            "DOWNTO", "OP0", "OP1", "OP2", "OP3", "OP4", "NOT", "CONCAT", 
            "ASSIGN", "INITASSIGN", "LB", "RB", "LSB", "RSB", "LP", "RP", 
            "SEMI", "CL", "DOT", "COMMA", "INTLIT", "FLOATLIT", "STRLIT", 
            "WS", "COMMENT", "LINECOMMENT", "ID", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                  "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
                  "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                  "FINAL", "STATIC", "TO", "DOWNTO", "OP0", "OP1", "OP2", 
                  "OP3", "OP4", "NOT", "CONCAT", "ASSIGN", "INITASSIGN", 
                  "LB", "RB", "LSB", "RSB", "LP", "RP", "SEMI", "CL", "DOT", 
                  "COMMA", "INTLIT", "FLOATLIT", "STRLIT", "WS", "COMMENT", 
                  "LINECOMMENT", "EXPONENT", "ESC", "NONEESC", "CHARACTERS", 
                  "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.ERROR_CHAR_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text)
     


