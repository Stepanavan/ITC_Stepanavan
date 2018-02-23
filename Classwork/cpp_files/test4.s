	.file	"test4.cpp"
	.text
	.globl	main
	.type	main, @function
main:
.LFB1024:
	.cfi_startproc
	movl	$0, %eax
	ret
	.cfi_endproc
.LFE1024:
	.size	main, .-main
	.type	_GLOBAL__sub_I_main, @function
_GLOBAL__sub_I_main:
.LFB1026:
	.cfi_startproc
	subl	$24, %esp
	.cfi_def_cfa_offset 28
	pushl	$_ZStL8__ioinit
	.cfi_def_cfa_offset 32
	call	_ZNSt8ios_base4InitC1Ev
	addl	$12, %esp
	.cfi_def_cfa_offset 20
	pushl	$__dso_handle
	.cfi_def_cfa_offset 24
	pushl	$_ZStL8__ioinit
	.cfi_def_cfa_offset 28
	pushl	$_ZNSt8ios_base4InitD1Ev
	.cfi_def_cfa_offset 32
	call	__cxa_atexit
	addl	$28, %esp
	.cfi_def_cfa_offset 4
	ret
	.cfi_endproc
.LFE1026:
	.size	_GLOBAL__sub_I_main, .-_GLOBAL__sub_I_main
	.section	.init_array,"aw"
	.align 4
	.long	_GLOBAL__sub_I_main
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (Debian 4.9.2-10) 4.9.2"
	.section	.note.GNU-stack,"",@progbits
