; ModuleID = 'counter.c'
source_filename = "counter.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@counter = internal unnamed_addr global i32 0, align 4, !dbg !0
@.str = private unnamed_addr constant [16 x i8] c"do increase...\0A\00", align 1
@.str.1 = private unnamed_addr constant [27 x i8] c"current counter value: %d\0A\00", align 1
@.str.2 = private unnamed_addr constant [15 x i8] c"do decreas...\0A\00", align 1
@.str.3 = private unnamed_addr constant [14 x i8] c"do iszero...\0A\00", align 1

; Function Attrs: norecurse noredzone nounwind readonly uwtable
define i32 @iszero() local_unnamed_addr #0 !dbg !11 {
  %1 = load i32, i32* @counter, align 4, !dbg !15, !tbaa !16
  %2 = icmp ne i32 %1, 0, !dbg !20
  %3 = zext i1 %2 to i32, !dbg !15
  ret i32 %3, !dbg !21
}

; Function Attrs: norecurse noredzone nounwind uwtable
define i32 @inc() local_unnamed_addr #1 !dbg !22 {
  %1 = load i32, i32* @counter, align 4, !dbg !23, !tbaa !16
  %2 = icmp eq i32 %1, -1, !dbg !25
  br i1 %2, label %5, label %3, !dbg !26

; <label>:3:                                      ; preds = %0
  %4 = add i32 %1, 1, !dbg !27
  store i32 %4, i32* @counter, align 4, !dbg !27, !tbaa !16
  br label %5, !dbg !28

; <label>:5:                                      ; preds = %0, %3
  %6 = phi i32 [ 0, %3 ], [ -1, %0 ]
  ret i32 %6, !dbg !29
}

; Function Attrs: norecurse noredzone nounwind uwtable
define i32 @dec() local_unnamed_addr #1 !dbg !30 {
  %1 = load i32, i32* @counter, align 4, !dbg !33, !tbaa !16
  %2 = icmp eq i32 %1, 0, !dbg !35
  br i1 %2, label %5, label %3, !dbg !36

; <label>:3:                                      ; preds = %0
  %4 = add i32 %1, -1, !dbg !37
  store i32 %4, i32* @counter, align 4, !dbg !37, !tbaa !16
  br label %5, !dbg !38

; <label>:5:                                      ; preds = %0, %3
  %6 = phi i32 [ 0, %3 ], [ -1, %0 ]
  ret i32 %6, !dbg !39
}

; Function Attrs: noredzone nounwind uwtable
define i32 @main(i32, i8** nocapture readnone) local_unnamed_addr #2 !dbg !40 {
  tail call void @llvm.dbg.value(metadata i32 %0, i64 0, metadata !47, metadata !49), !dbg !50
  tail call void @llvm.dbg.value(metadata i8** %1, i64 0, metadata !48, metadata !49), !dbg !51
  %3 = tail call i32 (i8*, ...) @printf(i8* getelementptr   ([16 x i8], [16 x i8]* @.str, i64 0, i64 0)) #5, !dbg !52
  %4 = load i32, i32* @counter, align 4, !dbg !53, !tbaa !16
  %5 = icmp eq i32 %4, -1, !dbg !55
  br i1 %5, label %8, label %6, !dbg !56

; <label>:6:                                      ; preds = %2
  %7 = add i32 %4, 1, !dbg !57
  store i32 %7, i32* @counter, align 4, !dbg !57, !tbaa !16
  br label %8, !dbg !58

; <label>:8:                                      ; preds = %2, %6
  %9 = phi i32 [ -1, %2 ], [ %7, %6 ], !dbg !59
  %10 = tail call i32 (i8*, ...) @printf(i8* getelementptr   ([27 x i8], [27 x i8]* @.str.1, i64 0, i64 0), i32 %9) #5, !dbg !60
  %11 = tail call i32 (i8*, ...) @printf(i8* getelementptr   ([15 x i8], [15 x i8]* @.str.2, i64 0, i64 0)) #5, !dbg !61
  %12 = load i32, i32* @counter, align 4, !dbg !62, !tbaa !16
  %13 = icmp eq i32 %12, 0, !dbg !64
  br i1 %13, label %16, label %14, !dbg !65

; <label>:14:                                     ; preds = %8
  %15 = add i32 %12, -1, !dbg !66
  store i32 %15, i32* @counter, align 4, !dbg !66, !tbaa !16
  br label %16, !dbg !67

; <label>:16:                                     ; preds = %8, %14
  %17 = phi i32 [ 0, %8 ], [ %15, %14 ], !dbg !68
  %18 = tail call i32 (i8*, ...) @printf(i8* getelementptr   ([27 x i8], [27 x i8]* @.str.1, i64 0, i64 0), i32 %17) #5, !dbg !69
  %19 = tail call i32 (i8*, ...) @printf(i8* getelementptr   ([14 x i8], [14 x i8]* @.str.3, i64 0, i64 0)) #5, !dbg !70
  %20 = load i32, i32* @counter, align 4, !dbg !71, !tbaa !16
  %21 = tail call i32 (i8*, ...) @printf(i8* getelementptr   ([27 x i8], [27 x i8]* @.str.1, i64 0, i64 0), i32 %20) #5, !dbg !72
  ret i32 0, !dbg !73
}

; Function Attrs: noredzone
declare i32 @printf(i8*, ...) local_unnamed_addr #3

; Function Attrs: nounwind readnone speculatable
declare void @llvm.dbg.value(metadata, i64, metadata, metadata) #4

attributes #0 = { norecurse noredzone nounwind readonly uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+x87,-3dnow,-3dnowa,-aes,-avx,-avx2,-avx512bw,-avx512cd,-avx512dq,-avx512er,-avx512f,-avx512ifma,-avx512pf,-avx512vbmi,-avx512vl,-avx512vpopcntdq,-f16c,-fma,-fma4,-mmx,-pclmul,-sha,-sse,-sse2,-sse3,-sse4.1,-sse4.2,-sse4a,-ssse3,-xop,-xsave,-xsaveopt" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { norecurse noredzone nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+x87,-3dnow,-3dnowa,-aes,-avx,-avx2,-avx512bw,-avx512cd,-avx512dq,-avx512er,-avx512f,-avx512ifma,-avx512pf,-avx512vbmi,-avx512vl,-avx512vpopcntdq,-f16c,-fma,-fma4,-mmx,-pclmul,-sha,-sse,-sse2,-sse3,-sse4.1,-sse4.2,-sse4a,-ssse3,-xop,-xsave,-xsaveopt" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { noredzone nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+x87,-3dnow,-3dnowa,-aes,-avx,-avx2,-avx512bw,-avx512cd,-avx512dq,-avx512er,-avx512f,-avx512ifma,-avx512pf,-avx512vbmi,-avx512vl,-avx512vpopcntdq,-f16c,-fma,-fma4,-mmx,-pclmul,-sha,-sse,-sse2,-sse3,-sse4.1,-sse4.2,-sse4a,-ssse3,-xop,-xsave,-xsaveopt" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { noredzone "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="false" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+x87,-3dnow,-3dnowa,-aes,-avx,-avx2,-avx512bw,-avx512cd,-avx512dq,-avx512er,-avx512f,-avx512ifma,-avx512pf,-avx512vbmi,-avx512vl,-avx512vpopcntdq,-f16c,-fma,-fma4,-mmx,-pclmul,-sha,-sse,-sse2,-sse3,-sse4.1,-sse4.2,-sse4a,-ssse3,-xop,-xsave,-xsaveopt" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #4 = { nounwind readnone speculatable }
attributes #5 = { nobuiltin noredzone nounwind }

!llvm.dbg.cu = !{!2}
!llvm.module.flags = !{!7, !8, !9}
!llvm.ident = !{!10}

!0 = !DIGlobalVariableExpression(var: !1)
!1 = distinct !DIGlobalVariable(name: "counter", scope: !2, file: !3, line: 11, type: !6, isLocal: true, isDefinition: true)
!2 = distinct !DICompileUnit(language: DW_LANG_C99, file: !3, producer: "clang version 5.0.0-3 (tags/RELEASE_500/final)", isOptimized: true, runtimeVersion: 0, emissionKind: FullDebug, enums: !4, globals: !5)
!3 = !DIFile(filename: "counter.c", directory: "/home/zhangqiang/Documents/test_hv6")
!4 = !{}
!5 = !{!0}
!6 = !DIBasicType(name: "unsigned int", size: 32, encoding: DW_ATE_unsigned)
!7 = !{i32 2, !"Dwarf Version", i32 4}
!8 = !{i32 2, !"Debug Info Version", i32 3}
!9 = !{i32 1, !"wchar_size", i32 4}
!10 = !{!"clang version 5.0.0-3 (tags/RELEASE_500/final)"}
!11 = distinct !DISubprogram(name: "iszero", scope: !3, file: !3, line: 13, type: !12, isLocal: false, isDefinition: true, scopeLine: 14, isOptimized: true, unit: !2, variables: !4)
!12 = !DISubroutineType(types: !13)
!13 = !{!14}
!14 = !DIBasicType(name: "int", size: 32, encoding: DW_ATE_signed)
!15 = !DILocation(line: 15, column: 9, scope: !11)
!16 = !{!17, !17, i64 0}
!17 = !{!"int", !18, i64 0}
!18 = !{!"omnipotent char", !19, i64 0}
!19 = !{!"Simple C/C++ TBAA"}
!20 = !DILocation(line: 15, column: 17, scope: !11)
!21 = !DILocation(line: 15, column: 2, scope: !11)
!22 = distinct !DISubprogram(name: "inc", scope: !3, file: !3, line: 18, type: !12, isLocal: false, isDefinition: true, scopeLine: 19, isOptimized: true, unit: !2, variables: !4)
!23 = !DILocation(line: 20, column: 5, scope: !24)
!24 = distinct !DILexicalBlock(scope: !22, file: !3, line: 20, column: 5)
!25 = !DILocation(line: 20, column: 13, scope: !24)
!26 = !DILocation(line: 20, column: 5, scope: !22)
!27 = !DILocation(line: 24, column: 10, scope: !22)
!28 = !DILocation(line: 25, column: 2, scope: !22)
!29 = !DILocation(line: 26, column: 1, scope: !22)
!30 = distinct !DISubprogram(name: "dec", scope: !3, file: !3, line: 28, type: !31, isLocal: false, isDefinition: true, scopeLine: 29, isOptimized: true, unit: !2, variables: !4)
!31 = !DISubroutineType(types: !32)
!32 = !{!6}
!33 = !DILocation(line: 35, column: 5, scope: !34)
!34 = distinct !DILexicalBlock(scope: !30, file: !3, line: 35, column: 5)
!35 = !DILocation(line: 35, column: 13, scope: !34)
!36 = !DILocation(line: 35, column: 5, scope: !30)
!37 = !DILocation(line: 38, column: 10, scope: !30)
!38 = !DILocation(line: 39, column: 2, scope: !30)
!39 = !DILocation(line: 40, column: 1, scope: !30)
!40 = distinct !DISubprogram(name: "main", scope: !3, file: !3, line: 42, type: !41, isLocal: false, isDefinition: true, scopeLine: 43, flags: DIFlagPrototyped, isOptimized: true, unit: !2, variables: !46)
!41 = !DISubroutineType(types: !42)
!42 = !{!14, !14, !43}
!43 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !44, size: 64)
!44 = !DIDerivedType(tag: DW_TAG_pointer_type, baseType: !45, size: 64)
!45 = !DIBasicType(name: "char", size: 8, encoding: DW_ATE_signed_char)
!46 = !{!47, !48}
!47 = !DILocalVariable(name: "arg", arg: 1, scope: !40, file: !3, line: 42, type: !14)
!48 = !DILocalVariable(name: "args", arg: 2, scope: !40, file: !3, line: 42, type: !43)
!49 = !DIExpression()
!50 = !DILocation(line: 42, column: 14, scope: !40)
!51 = !DILocation(line: 42, column: 26, scope: !40)
!52 = !DILocation(line: 44, column: 2, scope: !40)
!53 = !DILocation(line: 20, column: 5, scope: !24, inlinedAt: !54)
!54 = distinct !DILocation(line: 45, column: 2, scope: !40)
!55 = !DILocation(line: 20, column: 13, scope: !24, inlinedAt: !54)
!56 = !DILocation(line: 20, column: 5, scope: !22, inlinedAt: !54)
!57 = !DILocation(line: 24, column: 10, scope: !22, inlinedAt: !54)
!58 = !DILocation(line: 25, column: 2, scope: !22, inlinedAt: !54)
!59 = !DILocation(line: 46, column: 40, scope: !40)
!60 = !DILocation(line: 46, column: 2, scope: !40)
!61 = !DILocation(line: 47, column: 2, scope: !40)
!62 = !DILocation(line: 35, column: 5, scope: !34, inlinedAt: !63)
!63 = distinct !DILocation(line: 48, column: 2, scope: !40)
!64 = !DILocation(line: 35, column: 13, scope: !34, inlinedAt: !63)
!65 = !DILocation(line: 35, column: 5, scope: !30, inlinedAt: !63)
!66 = !DILocation(line: 38, column: 10, scope: !30, inlinedAt: !63)
!67 = !DILocation(line: 39, column: 2, scope: !30, inlinedAt: !63)
!68 = !DILocation(line: 49, column: 40, scope: !40)
!69 = !DILocation(line: 49, column: 2, scope: !40)
!70 = !DILocation(line: 50, column: 2, scope: !40)
!71 = !DILocation(line: 52, column: 40, scope: !40)
!72 = !DILocation(line: 52, column: 2, scope: !40)
!73 = !DILocation(line: 53, column: 2, scope: !40)
