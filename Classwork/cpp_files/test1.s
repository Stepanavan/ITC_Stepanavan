	.file	"test1.cpp"
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.text
	.align 2
	.type	_ZZ4mainEN5xxxxxD2Ev, @function
_ZZ4mainEN5xxxxxD2Ev:
.LFB1022:
	.cfi_startproc
	.cfi_personality 0,__gxx_personality_v0
	.cfi_lsda 0,.LLSDA1022
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%ebx
	subl	$4, %esp
	.cfi_offset 3, -12
	movl	8(%ebp), %eax
	addl	$16, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB0:
	.cfi_escape 0x2e,0x10
	call	_ZNSsD1Ev
.LEHE0:
	addl	$16, %esp
	movl	8(%ebp), %eax
	addl	$12, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB1:
	call	_ZNSsD1Ev
.LEHE1:
	addl	$16, %esp
	movl	8(%ebp), %eax
	addl	$8, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB2:
	call	_ZNSsD1Ev
.LEHE2:
	addl	$16, %esp
	movl	8(%ebp), %eax
	addl	$4, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB3:
	call	_ZNSsD1Ev
.LEHE3:
	addl	$16, %esp
	jmp	.L9
.L6:
	movl	%eax, %ebx
	movl	8(%ebp), %eax
	addl	$12, %eax
	subl	$12, %esp
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
	jmp	.L4
.L7:
	movl	%eax, %ebx
.L4:
	movl	8(%ebp), %eax
	addl	$8, %eax
	subl	$12, %esp
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
	jmp	.L5
.L8:
	movl	%eax, %ebx
.L5:
	movl	8(%ebp), %eax
	addl	$4, %eax
	subl	$12, %esp
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
	movl	%ebx, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB4:
	call	_Unwind_Resume
.LEHE4:
.L9:
	movl	-4(%ebp), %ebx
	leave
	.cfi_restore 5
	.cfi_restore 3
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE1022:
	.globl	__gxx_personality_v0
	.section	.gcc_except_table,"a",@progbits
.LLSDA1022:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1022-.LLSDACSB1022
.LLSDACSB1022:
	.uleb128 .LEHB0-.LFB1022
	.uleb128 .LEHE0-.LEHB0
	.uleb128 .L6-.LFB1022
	.uleb128 0
	.uleb128 .LEHB1-.LFB1022
	.uleb128 .LEHE1-.LEHB1
	.uleb128 .L7-.LFB1022
	.uleb128 0
	.uleb128 .LEHB2-.LFB1022
	.uleb128 .LEHE2-.LEHB2
	.uleb128 .L8-.LFB1022
	.uleb128 0
	.uleb128 .LEHB3-.LFB1022
	.uleb128 .LEHE3-.LEHB3
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB4-.LFB1022
	.uleb128 .LEHE4-.LEHB4
	.uleb128 0
	.uleb128 0
.LLSDACSE1022:
	.text
	.size	_ZZ4mainEN5xxxxxD2Ev, .-_ZZ4mainEN5xxxxxD2Ev
	.align 2
	.type	_ZZ4mainEN5xxxxxC2Ev, @function
_ZZ4mainEN5xxxxxC2Ev:
.LFB1025:
	.cfi_startproc
	.cfi_personality 0,__gxx_personality_v0
	.cfi_lsda 0,.LLSDA1025
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%ebx
	subl	$4, %esp
	.cfi_offset 3, -12
	movl	8(%ebp), %eax
	addl	$4, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB5:
	call	_ZNSsC1Ev
.LEHE5:
	addl	$16, %esp
	movl	8(%ebp), %eax
	addl	$8, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB6:
	.cfi_escape 0x2e,0x10
	call	_ZNSsC1Ev
.LEHE6:
	addl	$16, %esp
	movl	8(%ebp), %eax
	addl	$12, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB7:
	call	_ZNSsC1Ev
.LEHE7:
	addl	$16, %esp
	movl	8(%ebp), %eax
	addl	$16, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB8:
	call	_ZNSsC1Ev
.LEHE8:
	addl	$16, %esp
	jmp	.L17
.L16:
	movl	%eax, %ebx
	movl	8(%ebp), %eax
	addl	$12, %eax
	subl	$12, %esp
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
	jmp	.L12
.L15:
	movl	%eax, %ebx
.L12:
	movl	8(%ebp), %eax
	addl	$8, %eax
	subl	$12, %esp
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
	jmp	.L13
.L14:
	movl	%eax, %ebx
.L13:
	movl	8(%ebp), %eax
	addl	$4, %eax
	subl	$12, %esp
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
	movl	%ebx, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB9:
	call	_Unwind_Resume
.LEHE9:
.L17:
	movl	-4(%ebp), %ebx
	leave
	.cfi_restore 5
	.cfi_restore 3
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE1025:
	.section	.gcc_except_table
.LLSDA1025:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1025-.LLSDACSB1025
.LLSDACSB1025:
	.uleb128 .LEHB5-.LFB1025
	.uleb128 .LEHE5-.LEHB5
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB6-.LFB1025
	.uleb128 .LEHE6-.LEHB6
	.uleb128 .L14-.LFB1025
	.uleb128 0
	.uleb128 .LEHB7-.LFB1025
	.uleb128 .LEHE7-.LEHB7
	.uleb128 .L15-.LFB1025
	.uleb128 0
	.uleb128 .LEHB8-.LFB1025
	.uleb128 .LEHE8-.LEHB8
	.uleb128 .L16-.LFB1025
	.uleb128 0
	.uleb128 .LEHB9-.LFB1025
	.uleb128 .LEHE9-.LEHB9
	.uleb128 0
	.uleb128 0
.LLSDACSE1025:
	.text
	.size	_ZZ4mainEN5xxxxxC2Ev, .-_ZZ4mainEN5xxxxxC2Ev
	.section	.rodata
.LC0:
	.string	""
.LC1:
	.string	"Hamilton"
.LC2:
	.string	"Ontario"
	.align 4
.LC3:
	.string	"\325\204\325\270\326\202\325\277\326\204\325\241\325\243\326\200\325\245\326\204 \325\267\325\245\325\266\326\204\325\253 \325\260\325\241\325\264\325\241\326\200\325\250 "
	.align 4
.LC4:
	.string	"\325\204\325\270\326\202\325\277\326\204\325\241\325\243\326\200\325\245\326\204 \326\203\325\270\325\262\325\270\326\201\325\253 \325\241\325\266\325\270\326\202\325\266\325\250\326\211 "
	.align 4
.LC5:
	.string	"\325\204\325\270\326\202\325\277\326\204\325\241\325\243\326\200\325\245\326\204 \326\204\325\241\325\262\325\241\326\204\325\250\326\211 "
	.align 4
.LC6:
	.string	"\325\204\325\270\326\202\325\277\326\204\325\241\325\243\326\200\325\245\326\204 \325\264\325\241\326\200\325\246\325\250\326\211 "
	.align 4
.LC7:
	.string	"\325\204\325\270\326\202\325\277\326\204\325\241\325\243\326\200\325\245\326\204 \326\203\325\270\325\275\325\277\325\241\325\265\325\253\325\266 \325\253\325\266\325\244\325\245\326\204\325\275\325\250\326\211 "
.LC8:
	.string	"\325\267\325\245\325\266\326\204\325\253 \325\260\325\241\325\264\325\241\326\200\325\250 "
.LC9:
	.string	"\326\203\325\270\325\262\325\270\326\201\325\253 \325\241\325\266\325\270\326\202\325\266\325\250\326\211 "
.LC10:
	.string	"\326\204\325\241\325\262\325\241\326\204\325\250\326\211 "
.LC11:
	.string	"\325\264\325\241\326\200\325\246\325\250\326\211 "
	.align 4
.LC12:
	.string	"\326\203\325\270\325\275\325\277\325\241\325\265\325\253\325\266 \325\253\325\266\325\244\325\245\326\204\325\275\325\250\326\211 "
.LC13:
	.string	"2001"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1020:
	.cfi_startproc
	.cfi_personality 0,__gxx_personality_v0
	.cfi_lsda 0,.LLSDA1020
	leal	4(%esp), %ecx
	.cfi_def_cfa 1, 0
	andl	$-16, %esp
	pushl	-4(%ecx)
	pushl	%ebp
	.cfi_escape 0x10,0x5,0x2,0x75,0
	movl	%esp, %ebp
	pushl	%edi
	pushl	%esi
	pushl	%ebx
	pushl	%ecx
	.cfi_escape 0xf,0x3,0x75,0x70,0x6
	.cfi_escape 0x10,0x7,0x2,0x75,0x7c
	.cfi_escape 0x10,0x6,0x2,0x75,0x78
	.cfi_escape 0x10,0x3,0x2,0x75,0x74
	subl	$104, %esp
	movl	$0, -52(%ebp)
	movl	$0, -48(%ebp)
	movl	$0, -44(%ebp)
	movl	$0, -40(%ebp)
	movl	$0, -36(%ebp)
	subl	$12, %esp
	leal	-32(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcEC1Ev
	addl	$16, %esp
	subl	$4, %esp
	leal	-32(%ebp), %eax
	pushl	%eax
	pushl	$.LC0
	leal	-52(%ebp), %eax
	addl	$4, %eax
	pushl	%eax
.LEHB10:
	.cfi_escape 0x2e,0x10
	call	_ZNSsC1EPKcRKSaIcE
.LEHE10:
	addl	$16, %esp
	subl	$12, %esp
	leal	-32(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcED1Ev
	addl	$16, %esp
	subl	$12, %esp
	leal	-31(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcEC1Ev
	addl	$16, %esp
	subl	$4, %esp
	leal	-31(%ebp), %eax
	pushl	%eax
	pushl	$.LC1
	leal	-52(%ebp), %eax
	addl	$8, %eax
	pushl	%eax
.LEHB11:
	call	_ZNSsC1EPKcRKSaIcE
.LEHE11:
	addl	$16, %esp
	subl	$12, %esp
	leal	-31(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcED1Ev
	addl	$16, %esp
	subl	$12, %esp
	leal	-30(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcEC1Ev
	addl	$16, %esp
	subl	$4, %esp
	leal	-30(%ebp), %eax
	pushl	%eax
	pushl	$.LC2
	leal	-52(%ebp), %eax
	addl	$12, %eax
	pushl	%eax
.LEHB12:
	call	_ZNSsC1EPKcRKSaIcE
.LEHE12:
	addl	$16, %esp
	subl	$12, %esp
	leal	-30(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcED1Ev
	addl	$16, %esp
	subl	$12, %esp
	leal	-29(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcEC1Ev
	addl	$16, %esp
	subl	$4, %esp
	leal	-29(%ebp), %eax
	pushl	%eax
	pushl	$.LC0
	leal	-52(%ebp), %eax
	addl	$16, %eax
	pushl	%eax
.LEHB13:
	call	_ZNSsC1EPKcRKSaIcE
.LEHE13:
	addl	$16, %esp
	subl	$12, %esp
	leal	-29(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcED1Ev
	addl	$16, %esp
	leal	-112(%ebp), %ebx
	movl	$2, %esi
	movl	%ebx, %edi
	jmp	.L19
.L20:
	subl	$12, %esp
	pushl	%edi
.LEHB14:
	call	_ZZ4mainEN5xxxxxC2Ev
.LEHE14:
	addl	$16, %esp
	addl	$20, %edi
	subl	$1, %esi
.L19:
	cmpl	$-1, %esi
	jne	.L20
	movl	$0, -28(%ebp)
	jmp	.L21
.L22:
	subl	$8, %esp
	pushl	$.LC3
	pushl	$_ZSt4cout
.LEHB15:
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	%ecx, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt3cin
	call	_ZNSirsERi
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC4
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	%ecx, %eax
	addl	$4, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt3cin
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC5
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	%ecx, %eax
	addl	$8, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt3cin
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC6
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	%ecx, %eax
	addl	$12, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt3cin
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC7
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	$16, %eax
	addl	%ecx, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt3cin
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RSbIS4_S5_T1_E
	addl	$16, %esp
	addl	$1, -28(%ebp)
.L21:
	cmpl	$2, -28(%ebp)
	jle	.L22
	movl	$0, -28(%ebp)
	jmp	.L23
.L24:
	subl	$8, %esp
	pushl	$.LC8
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	leal	-24(%ebp), %edi
	addl	%edi, %eax
	subl	$88, %eax
	movl	(%eax), %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt4cout
	call	_ZNSolsEi
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC9
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	%ecx, %eax
	addl	$4, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt4cout
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC10
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	%ecx, %eax
	addl	$8, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt4cout
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC11
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	%ecx, %eax
	addl	$12, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt4cout
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC12
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	leal	-112(%ebp), %ecx
	movl	-28(%ebp), %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	addl	$16, %eax
	addl	%ecx, %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt4cout
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	addl	$1, -28(%ebp)
.L23:
	cmpl	$2, -28(%ebp)
	jle	.L24
	movl	-52(%ebp), %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt4cout
	call	_ZNSolsEi
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	%eax, %edx
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$4, %eax
	pushl	%eax
	pushl	%edx
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	%eax, %edx
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$8, %eax
	pushl	%eax
	pushl	%edx
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	%eax, %edx
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$12, %eax
	pushl	%eax
	pushl	%edx
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	%eax, %edx
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$16, %eax
	pushl	%eax
	pushl	%edx
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	$26, -52(%ebp)
	subl	$8, %esp
	pushl	$.LC4
	pushl	$_ZSt4cout
	call	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	addl	$16, %esp
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$4, %eax
	pushl	%eax
	pushl	$_ZSt3cin
	call	_ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$.LC13
	leal	-52(%ebp), %eax
	addl	$16, %eax
	pushl	%eax
	call	_ZNSsaSEPKc
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	$_ZSt4cout
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	-52(%ebp), %eax
	subl	$8, %esp
	pushl	%eax
	pushl	$_ZSt4cout
	call	_ZNSolsEi
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	%eax, %edx
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$4, %eax
	pushl	%eax
	pushl	%edx
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	%eax, %edx
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$8, %eax
	pushl	%eax
	pushl	%edx
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	%eax, %edx
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$12, %eax
	pushl	%eax
	pushl	%edx
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
	addl	$16, %esp
	movl	%eax, %edx
	subl	$8, %esp
	leal	-52(%ebp), %eax
	addl	$16, %eax
	pushl	%eax
	pushl	%edx
	call	_ZStlsIcSt11char_traitsIcESaIcEERSt13basic_ostreamIT_T0_ES7_RKSbIS4_S5_T1_E
	addl	$16, %esp
	subl	$8, %esp
	pushl	$_ZSt4endlIcSt11char_traitsIcEERSt13basic_ostreamIT_T0_ES6_
	pushl	%eax
	call	_ZNSolsEPFRSoS_E
.LEHE15:
	addl	$16, %esp
	movl	$0, %esi
	leal	-112(%ebp), %ebx
	addl	$60, %ebx
.L26:
	leal	-112(%ebp), %eax
	cmpl	%eax, %ebx
	je	.L25
	subl	$20, %ebx
	subl	$12, %esp
	pushl	%ebx
.LEHB16:
	call	_ZZ4mainEN5xxxxxD2Ev
.LEHE16:
	addl	$16, %esp
	jmp	.L26
.L25:
	subl	$12, %esp
	leal	-52(%ebp), %eax
	pushl	%eax
.LEHB17:
	call	_ZZ4mainEN5xxxxxD2Ev
	addl	$16, %esp
	movl	%esi, %eax
	jmp	.L48
.L41:
	movl	%eax, %ebx
	subl	$12, %esp
	leal	-32(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcED1Ev
	addl	$16, %esp
	movl	%ebx, %eax
	subl	$12, %esp
	pushl	%eax
	call	_Unwind_Resume
.LEHE17:
.L42:
	movl	%eax, %ebx
	subl	$12, %esp
	leal	-31(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcED1Ev
	addl	$16, %esp
	jmp	.L30
.L43:
	movl	%eax, %ebx
	subl	$12, %esp
	leal	-30(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcED1Ev
	addl	$16, %esp
	jmp	.L32
.L44:
	movl	%eax, %ebx
	subl	$12, %esp
	leal	-29(%ebp), %eax
	pushl	%eax
	call	_ZNSaIcED1Ev
	addl	$16, %esp
	subl	$12, %esp
	leal	-52(%ebp), %eax
	addl	$12, %eax
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
.L32:
	subl	$12, %esp
	leal	-52(%ebp), %eax
	addl	$8, %eax
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
.L30:
	subl	$12, %esp
	leal	-52(%ebp), %eax
	addl	$4, %eax
	pushl	%eax
	call	_ZNSsD1Ev
	addl	$16, %esp
	movl	%ebx, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB18:
	call	_Unwind_Resume
.LEHE18:
.L45:
	movl	%eax, %edi
	testl	%ebx, %ebx
	je	.L35
	movl	$2, %eax
	subl	%esi, %eax
	movl	%eax, %edx
	movl	%edx, %eax
	sall	$2, %eax
	addl	%edx, %eax
	sall	$2, %eax
	leal	(%ebx,%eax), %esi
.L36:
	cmpl	%ebx, %esi
	je	.L35
	subl	$20, %esi
	subl	$12, %esp
	pushl	%esi
	call	_ZZ4mainEN5xxxxxD2Ev
	addl	$16, %esp
	jmp	.L36
.L35:
	movl	%edi, %ebx
	jmp	.L37
.L47:
	movl	%eax, %esi
	leal	-112(%ebp), %ebx
	addl	$60, %ebx
.L40:
	leal	-112(%ebp), %eax
	cmpl	%eax, %ebx
	je	.L39
	subl	$20, %ebx
	subl	$12, %esp
	pushl	%ebx
	call	_ZZ4mainEN5xxxxxD2Ev
	addl	$16, %esp
	jmp	.L40
.L39:
	movl	%esi, %ebx
	jmp	.L37
.L46:
	movl	%eax, %ebx
.L37:
	subl	$12, %esp
	leal	-52(%ebp), %eax
	pushl	%eax
	call	_ZZ4mainEN5xxxxxD2Ev
	addl	$16, %esp
	movl	%ebx, %eax
	subl	$12, %esp
	pushl	%eax
.LEHB19:
	call	_Unwind_Resume
.LEHE19:
.L48:
	leal	-16(%ebp), %esp
	popl	%ecx
	.cfi_restore 1
	.cfi_def_cfa 1, 0
	popl	%ebx
	.cfi_restore 3
	popl	%esi
	.cfi_restore 6
	popl	%edi
	.cfi_restore 7
	popl	%ebp
	.cfi_restore 5
	leal	-4(%ecx), %esp
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE1020:
	.section	.gcc_except_table
.LLSDA1020:
	.byte	0xff
	.byte	0xff
	.byte	0x1
	.uleb128 .LLSDACSE1020-.LLSDACSB1020
.LLSDACSB1020:
	.uleb128 .LEHB10-.LFB1020
	.uleb128 .LEHE10-.LEHB10
	.uleb128 .L41-.LFB1020
	.uleb128 0
	.uleb128 .LEHB11-.LFB1020
	.uleb128 .LEHE11-.LEHB11
	.uleb128 .L42-.LFB1020
	.uleb128 0
	.uleb128 .LEHB12-.LFB1020
	.uleb128 .LEHE12-.LEHB12
	.uleb128 .L43-.LFB1020
	.uleb128 0
	.uleb128 .LEHB13-.LFB1020
	.uleb128 .LEHE13-.LEHB13
	.uleb128 .L44-.LFB1020
	.uleb128 0
	.uleb128 .LEHB14-.LFB1020
	.uleb128 .LEHE14-.LEHB14
	.uleb128 .L45-.LFB1020
	.uleb128 0
	.uleb128 .LEHB15-.LFB1020
	.uleb128 .LEHE15-.LEHB15
	.uleb128 .L47-.LFB1020
	.uleb128 0
	.uleb128 .LEHB16-.LFB1020
	.uleb128 .LEHE16-.LEHB16
	.uleb128 .L46-.LFB1020
	.uleb128 0
	.uleb128 .LEHB17-.LFB1020
	.uleb128 .LEHE17-.LEHB17
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB18-.LFB1020
	.uleb128 .LEHE18-.LEHB18
	.uleb128 0
	.uleb128 0
	.uleb128 .LEHB19-.LFB1020
	.uleb128 .LEHE19-.LEHB19
	.uleb128 0
	.uleb128 0
.LLSDACSE1020:
	.text
	.size	main, .-main
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB1077:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$8, %esp
	cmpl	$1, 8(%ebp)
	jne	.L49
	cmpl	$65535, 12(%ebp)
	jne	.L49
	subl	$12, %esp
	pushl	$_ZStL8__ioinit
	call	_ZNSt8ios_base4InitC1Ev
	addl	$16, %esp
	subl	$4, %esp
	pushl	$__dso_handle
	pushl	$_ZStL8__ioinit
	pushl	$_ZNSt8ios_base4InitD1Ev
	call	__cxa_atexit
	addl	$16, %esp
.L49:
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE1077:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.type	_GLOBAL__sub_I_main, @function
_GLOBAL__sub_I_main:
.LFB1078:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$8, %esp
	subl	$8, %esp
	pushl	$65535
	pushl	$1
	call	_Z41__static_initialization_and_destruction_0ii
	addl	$16, %esp
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE1078:
	.size	_GLOBAL__sub_I_main, .-_GLOBAL__sub_I_main
	.section	.init_array,"aw"
	.align 4
	.long	_GLOBAL__sub_I_main
	.section	.rodata
	.align 4
	.type	_ZZL18__gthread_active_pvE20__gthread_active_ptr, @object
	.size	_ZZL18__gthread_active_pvE20__gthread_active_ptr, 4
_ZZL18__gthread_active_pvE20__gthread_active_ptr:
	.long	_ZL28__gthrw___pthread_key_createPjPFvPvE
	.weakref	_ZL28__gthrw___pthread_key_createPjPFvPvE,__pthread_key_create
	.hidden	__dso_handle
	.ident	"GCC: (Debian 4.9.2-10) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
