#
# WARNING: This file has been automatically generated from x86_64/counter.ll
#

import libirpy.itypes as itypes

def _init_types(ctx,):
  irpy = ctx['eval']


def _init_globals(ctx,):
  irpy = ctx['eval']
  irpy.declare_global_variable(ctx,'@counter',itypes.parse_type(ctx,'i32*'),irpy.constant_int(ctx,0,32,),itypes.parse_type(ctx,'i32'))
  irpy.declare_global_constant(ctx,'@_str',itypes.parse_type(ctx,'[16 x i8]*'),irpy.constant_data_array(ctx,itypes.parse_type(ctx,'[16 x i8]'),'c"do increase___\0A\00"',),itypes.parse_type(ctx,'[16 x i8]'))
  irpy.declare_global_constant(ctx,'@_str_1',itypes.parse_type(ctx,'[27 x i8]*'),irpy.constant_data_array(ctx,itypes.parse_type(ctx,'[27 x i8]'),'c"current counter value: %d\0A\00"',),itypes.parse_type(ctx,'[27 x i8]'))
  irpy.declare_global_constant(ctx,'@_str_2',itypes.parse_type(ctx,'[15 x i8]*'),irpy.constant_data_array(ctx,itypes.parse_type(ctx,'[15 x i8]'),'c"do decreas___\0A\00"',),itypes.parse_type(ctx,'[15 x i8]'))
  irpy.declare_global_constant(ctx,'@_str_3',itypes.parse_type(ctx,'[14 x i8]*'),irpy.constant_data_array(ctx,itypes.parse_type(ctx,'[14 x i8]'),'c"do iszero___\0A\00"',),itypes.parse_type(ctx,'[14 x i8]'))


def func_iszero(ctx,):
  irpy = ctx['eval']
  ctx['stacktrace'][-1] = {'function':'iszero'}
  def bb_0(pred,):
    irpy.debug_loc(ctx,'%1','counter.c:15:9',)
    ctx.stack["%1"] = irpy.load(ctx,itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'%2','counter.c:15:17',)
    ctx.stack["%2"] = irpy.ne(ctx,itypes.parse_type(ctx,'i1'),ctx.stack["%1"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,0,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'%3','counter.c:15:9',)
    ctx.stack["%3"] = irpy.zext(ctx,itypes.parse_type(ctx,'i32'),ctx.stack["%2"],itypes.parse_type(ctx,'i1'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:15:2',)
    return ctx.stack["%3"]

  return bb_0(None)

def func_inc(ctx,):
  irpy = ctx['eval']
  ctx['stacktrace'][-1] = {'function':'inc'}
  def bb_0(pred,):
    irpy.debug_loc(ctx,'%1','counter.c:20:5',)
    ctx.stack["%1"] = irpy.load(ctx,itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'%2','counter.c:20:13',)
    ctx.stack["%2"] = irpy.eq(ctx,itypes.parse_type(ctx,'i1'),ctx.stack["%1"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,4294967295,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:20:5',)
    return irpy.branch(ctx,ctx.stack["%2"],itypes.parse_type(ctx,'i1'),lambda: bb_5("%0"),lambda: bb_3("%0"),)

  def bb_3(pred,):
    irpy.debug_loc(ctx,'%4','counter.c:24:10',)
    ctx.stack["%4"] = irpy.add(ctx,itypes.parse_type(ctx,'i32'),ctx.stack["%1"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,1,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:24:10',)
    irpy.store(ctx,itypes.parse_type(ctx,'void'),ctx.stack["%4"],itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:25:2',)
    return bb_5("%3")

  def bb_5(pred,):
    ctx.stack["%6"] = { "%3": (lambda : irpy.constant_int(ctx,0,32,)), "%0": (lambda : irpy.constant_int(ctx,4294967295,32,)),}[pred]()
    irpy.debug_loc(ctx,'<badref>','counter.c:26:1',)
    return ctx.stack["%6"]

  return bb_0(None)

def func_dec(ctx,):
  irpy = ctx['eval']
  ctx['stacktrace'][-1] = {'function':'dec'}
  def bb_0(pred,):
    irpy.debug_loc(ctx,'%1','counter.c:35:5',)
    ctx.stack["%1"] = irpy.load(ctx,itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'%2','counter.c:35:13',)
    ctx.stack["%2"] = irpy.eq(ctx,itypes.parse_type(ctx,'i1'),ctx.stack["%1"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,0,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:35:5',)
    return irpy.branch(ctx,ctx.stack["%2"],itypes.parse_type(ctx,'i1'),lambda: bb_5("%0"),lambda: bb_3("%0"),)

  def bb_3(pred,):
    irpy.debug_loc(ctx,'%4','counter.c:38:10',)
    ctx.stack["%4"] = irpy.add(ctx,itypes.parse_type(ctx,'i32'),ctx.stack["%1"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,4294967295,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:38:10',)
    irpy.store(ctx,itypes.parse_type(ctx,'void'),ctx.stack["%4"],itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:39:2',)
    return bb_5("%3")

  def bb_5(pred,):
    ctx.stack["%6"] = { "%3": (lambda : irpy.constant_int(ctx,0,32,)), "%0": (lambda : irpy.constant_int(ctx,4294967295,32,)),}[pred]()
    irpy.debug_loc(ctx,'<badref>','counter.c:40:1',)
    return ctx.stack["%6"]

  return bb_0(None)

def func_main(ctx,arg1,arg2,):
  irpy = ctx['eval']
  ctx['stacktrace'][-1] = {'function':'main'}
  assert itypes.has_type(ctx, arg1, itypes.parse_type(ctx,'i32')), 'Incorrect BitVec size'
  ctx.stack["%0"] = arg1
  assert itypes.has_type(ctx, arg2, itypes.parse_type(ctx,'i8**')), 'Incorrect BitVec size'
  ctx.stack["%1"] = arg2
  def bb_2(pred,):
    irpy.debug_loc(ctx,'%3','counter.c:44:2',)
    ctx.stack["%3"] = irpy.call(ctx,itypes.parse_type(ctx,'i32'),irpy.getelementptr(ctx,itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'[16 x i8]*'),'@_str',),itypes.parse_type(ctx,'[16 x i8]*'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),),itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32 (i8*, ...)*'),'@printf',),itypes.parse_type(ctx,'i32 (i8*, ...)*'),)
    irpy.debug_loc(ctx,'%4','counter.c:20:5 @[ counter.c:45:2 ]',)
    ctx.stack["%4"] = irpy.load(ctx,itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'%5','counter.c:20:13 @[ counter.c:45:2 ]',)
    ctx.stack["%5"] = irpy.eq(ctx,itypes.parse_type(ctx,'i1'),ctx.stack["%4"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,4294967295,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:20:5 @[ counter.c:45:2 ]',)
    return irpy.branch(ctx,ctx.stack["%5"],itypes.parse_type(ctx,'i1'),lambda: bb_8("%2"),lambda: bb_6("%2"),)

  def bb_6(pred,):
    irpy.debug_loc(ctx,'%7','counter.c:24:10 @[ counter.c:45:2 ]',)
    ctx.stack["%7"] = irpy.add(ctx,itypes.parse_type(ctx,'i32'),ctx.stack["%4"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,1,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:24:10 @[ counter.c:45:2 ]',)
    irpy.store(ctx,itypes.parse_type(ctx,'void'),ctx.stack["%7"],itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:25:2 @[ counter.c:45:2 ]',)
    return bb_8("%6")

  def bb_8(pred,):
    irpy.debug_loc(ctx,'%9','counter.c:46:40',)
    ctx.stack["%9"] = { "%2": (lambda : irpy.constant_int(ctx,4294967295,32,)), "%6": (lambda : ctx.stack["%7"]),}[pred]()
    irpy.debug_loc(ctx,'%10','counter.c:46:2',)
    ctx.stack["%10"] = irpy.call(ctx,itypes.parse_type(ctx,'i32'),irpy.getelementptr(ctx,itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'[27 x i8]*'),'@_str_1',),itypes.parse_type(ctx,'[27 x i8]*'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),),itypes.parse_type(ctx,'i8*'),ctx.stack["%9"],itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32 (i8*, ...)*'),'@printf',),itypes.parse_type(ctx,'i32 (i8*, ...)*'),)
    irpy.debug_loc(ctx,'%11','counter.c:47:2',)
    ctx.stack["%11"] = irpy.call(ctx,itypes.parse_type(ctx,'i32'),irpy.getelementptr(ctx,itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'[15 x i8]*'),'@_str_2',),itypes.parse_type(ctx,'[15 x i8]*'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),),itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32 (i8*, ...)*'),'@printf',),itypes.parse_type(ctx,'i32 (i8*, ...)*'),)
    irpy.debug_loc(ctx,'%12','counter.c:35:5 @[ counter.c:48:2 ]',)
    ctx.stack["%12"] = irpy.load(ctx,itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'%13','counter.c:35:13 @[ counter.c:48:2 ]',)
    ctx.stack["%13"] = irpy.eq(ctx,itypes.parse_type(ctx,'i1'),ctx.stack["%12"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,0,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:35:5 @[ counter.c:48:2 ]',)
    return irpy.branch(ctx,ctx.stack["%13"],itypes.parse_type(ctx,'i1'),lambda: bb_16("%8"),lambda: bb_14("%8"),)

  def bb_14(pred,):
    irpy.debug_loc(ctx,'%15','counter.c:38:10 @[ counter.c:48:2 ]',)
    ctx.stack["%15"] = irpy.add(ctx,itypes.parse_type(ctx,'i32'),ctx.stack["%12"],itypes.parse_type(ctx,'i32'),irpy.constant_int(ctx,4294967295,32,),itypes.parse_type(ctx,'i32'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:38:10 @[ counter.c:48:2 ]',)
    irpy.store(ctx,itypes.parse_type(ctx,'void'),ctx.stack["%15"],itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:39:2 @[ counter.c:48:2 ]',)
    return bb_16("%14")

  def bb_16(pred,):
    irpy.debug_loc(ctx,'%17','counter.c:49:40',)
    ctx.stack["%17"] = { "%8": (lambda : irpy.constant_int(ctx,0,32,)), "%14": (lambda : ctx.stack["%15"]),}[pred]()
    irpy.debug_loc(ctx,'%18','counter.c:49:2',)
    ctx.stack["%18"] = irpy.call(ctx,itypes.parse_type(ctx,'i32'),irpy.getelementptr(ctx,itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'[27 x i8]*'),'@_str_1',),itypes.parse_type(ctx,'[27 x i8]*'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),),itypes.parse_type(ctx,'i8*'),ctx.stack["%17"],itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32 (i8*, ...)*'),'@printf',),itypes.parse_type(ctx,'i32 (i8*, ...)*'),)
    irpy.debug_loc(ctx,'%19','counter.c:50:2',)
    ctx.stack["%19"] = irpy.call(ctx,itypes.parse_type(ctx,'i32'),irpy.getelementptr(ctx,itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'[14 x i8]*'),'@_str_3',),itypes.parse_type(ctx,'[14 x i8]*'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),),itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32 (i8*, ...)*'),'@printf',),itypes.parse_type(ctx,'i32 (i8*, ...)*'),)
    irpy.debug_loc(ctx,'%20','counter.c:52:40',)
    ctx.stack["%20"] = irpy.load(ctx,itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32*'),'@counter',),itypes.parse_type(ctx,'i32*'),)
    irpy.debug_loc(ctx,'%21','counter.c:52:2',)
    ctx.stack["%21"] = irpy.call(ctx,itypes.parse_type(ctx,'i32'),irpy.getelementptr(ctx,itypes.parse_type(ctx,'i8*'),irpy.global_value(ctx,itypes.parse_type(ctx,'[27 x i8]*'),'@_str_1',),itypes.parse_type(ctx,'[27 x i8]*'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),irpy.constant_int(ctx,0,64,),itypes.parse_type(ctx,'i64'),),itypes.parse_type(ctx,'i8*'),ctx.stack["%20"],itypes.parse_type(ctx,'i32'),irpy.global_value(ctx,itypes.parse_type(ctx,'i32 (i8*, ...)*'),'@printf',),itypes.parse_type(ctx,'i32 (i8*, ...)*'),)
    irpy.debug_loc(ctx,'<badref>','counter.c:53:2',)
    return irpy.constant_int(ctx,0,32,)

  return bb_2(None)

def _init_metadata(ctx,):
  irpy = ctx['eval']
  irpy.declare_metadata(ctx, '!0','!DIGlobalVariableExpression(var: !1)')
  irpy.declare_metadata(ctx, '!1','distinct !DIGlobalVariable(name: "counter", scope: !2, file: !3, line: 11, type: !6, isLocal: true, isDefinition: true)')
  irpy.declare_metadata(ctx, '!2','distinct !DICompileUnit(language: DW_LANG_C99, file: !3, producer: "clang version 5.0.0-3 (tags/RELEASE_500/final)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !4, globals: !5)')
  irpy.declare_metadata(ctx, '!3','!DIFile(filename: "counter.c", directory: "/home/zhangqiang/Documents/test_hv6")')
  irpy.declare_metadata(ctx, '!4','!{}')
  irpy.declare_metadata(ctx, '!5','!{!0}')
  irpy.declare_metadata(ctx, '!6','!DIBasicType(name: "unsigned int", size: 32, encoding: DW_ATE_unsigned)')
  irpy.declare_metadata(ctx, '!11','distinct !DISubprogram(name: "iszero", scope: !3, file: !3, line: 13, type: !12, isLocal: false, isDefinition: true, scopeLine: 14, isOptimized: true, unit: !2, variables: !4)')
  irpy.declare_metadata(ctx, '!12','!DISubroutineType(types: !13)')
  irpy.declare_metadata(ctx, '!13','!{!14}')
  irpy.declare_metadata(ctx, '!14','!DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)')
  irpy.declare_metadata(ctx, '!15','!DILocation(line: 15, column: 9, scope: !11)')
  irpy.declare_metadata(ctx, '!16','!{!17, !17, i64 0}')
  irpy.declare_metadata(ctx, '!17','!{!"int", !18, i64 0}')
  irpy.declare_metadata(ctx, '!18','!{!"omnipotent char", !19, i64 0}')
  irpy.declare_metadata(ctx, '!19','!{!"Simple C/C++ TBAA"}')
  irpy.declare_metadata(ctx, '!20','!DILocation(line: 15, column: 17, scope: !11)')
  irpy.declare_metadata(ctx, '!21','!DILocation(line: 15, column: 2, scope: !11)')
  irpy.declare_metadata(ctx, '!22','distinct !DISubprogram(name: "inc", scope: !3, file: !3, line: 18, type: !12, isLocal: false, isDefinition: true, scopeLine: 19, isOptimized: true, unit: !2, variables: !4)')
  irpy.declare_metadata(ctx, '!23','!DILocation(line: 20, column: 5, scope: !24)')
  irpy.declare_metadata(ctx, '!24','distinct !DILexicalBlock(scope: !22, file: !3, line: 20, column: 5)')
  irpy.declare_metadata(ctx, '!25','!DILocation(line: 20, column: 13, scope: !24)')
  irpy.declare_metadata(ctx, '!26','!DILocation(line: 20, column: 5, scope: !22)')
  irpy.declare_metadata(ctx, '!27','!DILocation(line: 24, column: 10, scope: !22)')
  irpy.declare_metadata(ctx, '!28','!DILocation(line: 25, column: 2, scope: !22)')
  irpy.declare_metadata(ctx, '!29','!DILocation(line: 26, column: 1, scope: !22)')
  irpy.declare_metadata(ctx, '!30','distinct !DISubprogram(name: "dec", scope: !3, file: !3, line: 28, type: !31, isLocal: false, isDefinition: true, scopeLine: 29, isOptimized: true, unit: !2, variables: !4)')
  irpy.declare_metadata(ctx, '!31','!DISubroutineType(types: !32)')
  irpy.declare_metadata(ctx, '!32','!{!6}')
  irpy.declare_metadata(ctx, '!33','!DILocation(line: 35, column: 5, scope: !34)')
  irpy.declare_metadata(ctx, '!34','distinct !DILexicalBlock(scope: !30, file: !3, line: 35, column: 5)')
  irpy.declare_metadata(ctx, '!35','!DILocation(line: 35, column: 13, scope: !34)')
  irpy.declare_metadata(ctx, '!36','!DILocation(line: 35, column: 5, scope: !30)')
  irpy.declare_metadata(ctx, '!37','!DILocation(line: 38, column: 10, scope: !30)')
  irpy.declare_metadata(ctx, '!38','!DILocation(line: 39, column: 2, scope: !30)')
  irpy.declare_metadata(ctx, '!39','!DILocation(line: 40, column: 1, scope: !30)')
  irpy.declare_metadata(ctx, '!40','distinct !DISubprogram(name: "main", scope: !3, file: !3, line: 42, type: !41, isLocal: false, isDefinition: true, scopeLine: 43, flags: DIFlagPrototyped, isOptimized: true, unit: !2, variables: !46)')
  irpy.declare_metadata(ctx, '!41','!DISubroutineType(types: !42)')
  irpy.declare_metadata(ctx, '!42','!{!14, !14, !43}')
  irpy.declare_metadata(ctx, '!43','!DIDerivedType(tag: DW_TAG_pointer_type, baseType: !44, size: 64)')
  irpy.declare_metadata(ctx, '!44','!DIDerivedType(tag: DW_TAG_pointer_type, baseType: !45, size: 64)')
  irpy.declare_metadata(ctx, '!45','!DIBasicType(name: "char", size: 8, encoding: DW_ATE_signed_char)')
  irpy.declare_metadata(ctx, '!46','!{!47, !48}')
  irpy.declare_metadata(ctx, '!47','!DILocalVariable(name: "arg", arg: 1, scope: !40, file: !3, line: 42, type: !14)')
  irpy.declare_metadata(ctx, '!48','!DILocalVariable(name: "args", arg: 2, scope: !40, file: !3, line: 42, type: !43)')
  irpy.declare_metadata(ctx, '!50','!DILocation(line: 42, column: 14, scope: !40)')
  irpy.declare_metadata(ctx, '!51','!DILocation(line: 42, column: 26, scope: !40)')
  irpy.declare_metadata(ctx, '!52','!DILocation(line: 44, column: 2, scope: !40)')
  irpy.declare_metadata(ctx, '!53','!DILocation(line: 20, column: 5, scope: !24, inlinedAt: !54)')
  irpy.declare_metadata(ctx, '!54','distinct !DILocation(line: 45, column: 2, scope: !40)')
  irpy.declare_metadata(ctx, '!55','!DILocation(line: 20, column: 13, scope: !24, inlinedAt: !54)')
  irpy.declare_metadata(ctx, '!56','!DILocation(line: 20, column: 5, scope: !22, inlinedAt: !54)')
  irpy.declare_metadata(ctx, '!57','!DILocation(line: 24, column: 10, scope: !22, inlinedAt: !54)')
  irpy.declare_metadata(ctx, '!58','!DILocation(line: 25, column: 2, scope: !22, inlinedAt: !54)')
  irpy.declare_metadata(ctx, '!59','!DILocation(line: 46, column: 40, scope: !40)')
  irpy.declare_metadata(ctx, '!60','!DILocation(line: 46, column: 2, scope: !40)')
  irpy.declare_metadata(ctx, '!61','!DILocation(line: 47, column: 2, scope: !40)')
  irpy.declare_metadata(ctx, '!62','!DILocation(line: 35, column: 5, scope: !34, inlinedAt: !63)')
  irpy.declare_metadata(ctx, '!63','distinct !DILocation(line: 48, column: 2, scope: !40)')
  irpy.declare_metadata(ctx, '!64','!DILocation(line: 35, column: 13, scope: !34, inlinedAt: !63)')
  irpy.declare_metadata(ctx, '!65','!DILocation(line: 35, column: 5, scope: !30, inlinedAt: !63)')
  irpy.declare_metadata(ctx, '!66','!DILocation(line: 38, column: 10, scope: !30, inlinedAt: !63)')
  irpy.declare_metadata(ctx, '!67','!DILocation(line: 39, column: 2, scope: !30, inlinedAt: !63)')
  irpy.declare_metadata(ctx, '!68','!DILocation(line: 49, column: 40, scope: !40)')
  irpy.declare_metadata(ctx, '!69','!DILocation(line: 49, column: 2, scope: !40)')
  irpy.declare_metadata(ctx, '!70','!DILocation(line: 50, column: 2, scope: !40)')
  irpy.declare_metadata(ctx, '!71','!DILocation(line: 52, column: 40, scope: !40)')
  irpy.declare_metadata(ctx, '!72','!DILocation(line: 52, column: 2, scope: !40)')
  irpy.declare_metadata(ctx, '!73','!DILocation(line: 53, column: 2, scope: !40)')

