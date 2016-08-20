#HackCon 2016
##Army of Binaries

###Description
The service presents you a random binary every time asking you to get the correct input so as to run the "yes" condition in the binary. The game has 31 rounds. Go fight! nc 52.88.137.165 8000

Operating System: ?

Reported Difficulty: Medium

###Connecting to it

```
nc 52.88.137.165 8000
Welcome to Sheldon Cooper presents "Fun with Bins"
In the first episode, we're going to have fun reversing simple binaries
I will send you a random binary. To pass the stage, you'll need to give me the input to reach the "Yes" condition.
Lets get started

-> Round 1
ELF>�@@(@8	@@@@@@��88@8@@@L	L	 ``H` ((`(`��TT@T@DDP�td@@44Q�tdR�td``��/lib64/ld-linux-x86-64.so.2GNU GNU�����;
f2�zL�  gUa    D
               5</N )`libc.so.6strncmpputs__stack_chk_failstdinfgetss]ui_lg``` `(`0`8`@`H�H�_2.4GLIBC_2.2.5ii
 H��t�{H���5
 �%
 @�%
 h������%
 h������%
 h������%�
 h������%�
 h������%�
 h������%R
 f�1�I��^H��H���PTI���@H��@@H�Ǧ@������fD�_`UH-X`H�H��v�H��t]�X`��f�]@f.��X`UH��X`H��H��H��H��?H�H��t�H��t
                                        ]�X`�]�fD�=
 uUH���n���]��	 �@� `H�?u�H��t�UH����]�z���UH��H�ĀdH�%(H�E�1�H�E��@H��	 H�E��dH�������H�E�H���w���H���D�H�M�H�E��dH��H���6�����u
                                                         �@�8���
�@�,����H�M�dH3
               %(t�3����ÐAWAVA��AUATL�%� UH�-� SI��I��L)�H�H�������H��t 1�L��L��D��A��H��H9�u�H�[]A\A]A^A_Ðf.���H�H��0492740db44909f34d319ec6e37c71872c6ef7472de45f280fe54a645df3e01f2a56c173b7d8ebYesNope;4��������P����� ��������zRx
          �8���*zRx
                            �$����pFJ
�                                      �?;*3$"D�����A�C
  DdP���eBBE �B(�H0�H8�M@r8A0A(B BB�x����@`@
�@``���o�@�@�@                                  @
s
 `��@P0	���o @���o���o
                                         @(`F@V@f@v@�@�@GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.2) 5.4.0 201606098@T@t@�@�@�@
                                                          @ @	P@
�@
    @
�@�@�@�@@@`` `(```H```��
                                                          `�@ @.`@Dh`S`z�@�`������H	@ `��`!(`*`=@P`f�@v� 7 H`��`�X`p�@��"5H`B QP`^�@m@@ep`;�@*}X`��@� �X`� w
                                 @crtstuff.c__JCR_LIST__deregister_tm_clones__do_global_dtors_auxcompleted.7585__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entry0492740db44909f34d319ec6e37c71872c6ef7472de45f280fe54a645df3e01f2a56c173b7d8eb.c__FRAME_END____JCR_END____init_array_end_DYNAMIC__init_array_start__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE___libc_csu_finistrncmp@@GLIBC_2.2.5_ITM_deregisterTMCloneTableputs@@GLIBC_2.2.5stdin@@GLIBC_2.2.5_edatastrlen@@GLIBC_2.2.5__stack_chk_fail@@GLIBC_2.4__libc_start_main@@GLIBC_2.2.5fgets@@GLIBC_2.2.5__data_start__gmon_start____dso_handle_IO_stdin_used__libc_csu_init__bss_startmain_Jv_RegisterClasses__TMC_END___ITM_registerTMCloneTable.symtab.strtab.shstrtab.interp.note.ABI-tag.note.gnu.build-id.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.text.fini.rodata.eh_frame_hdr.eh_frame.init_array.fini_array.jcr.dynamic.got.plt.data.bss.comment8@8#T@T 1t@t$D���o�@�N
                             �@��V�@�s^���o
                                                      @
                                                        k���o @ 0zP@P�B�@�� @�0@0p����@���@�	��@��@4�@��`� �(`(���`�H`H``X0X4
                                                ��	P�
You got it?
```

On each round we get a binary, if we copy it to a file and give it appropriate permissions we can run it.

The program asks for input and prints Nope but we need it to print Yes.


By firing up IDA, we can take a look at the main function:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax@4
  __int64 v4; // rcx@4
  char *s1; // [sp+8h] [bp-78h]@1
  char s[104]; // [sp+10h] [bp-70h]@1
  __int64 v7; // [sp+78h] [bp-8h]@1

  v7 = *MK_FP(__FS__, 40LL);
  s1 = "eb89da5ea3bb2ff43f64e800792e852cae68069623e66e9df8e805eef74a7d99e97e6842a6";
  fgets(s, 100, stdin);
  s[strlen(s) - 1] = 0;
  if ( !strncmp(s1, s, 0x64uLL) )
    puts("Yes");
  else
    puts("Nope");
  result = 0;
  v4 = *MK_FP(__FS__, 40LL) ^ v7;
  return result;
}
```

The string it uses to compare with the user input and return Yes is the 17th (or sometimes 18th) line returned with `strings bin.a`, where bin.a is the binary provided.

This repeats for 31 rounds, after correctly guessing the last one, the flag is returned.

###Payload
The payload was written in python
```
from pwn import *
from time import sleep

def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]

r = remote('52.88.137.165', '8000')
# EXPLOIT CODE GOES HERE
for round in range (1, 32):
	print r.recvuntil('-> Round '+str(round), timeout=10)
	bin = r.recvuntil('You got it?', timeout=10)	
	bin = remove_last_line_from_string(bin)
	f = open("bin.a", "w")
	f.write(bin)
	f.close()

	answer = subprocess.Popen("strings bin.a | head -n 17 | tail -1", shell=True, stdout=subprocess.PIPE).stdout.read()
	if '[]A\A]A^A_' in answer:
		print 'weird case'	#sometimes this happens lmao
		answer = subprocess.Popen("strings bin.a | head -n 18 | tail -1", shell=True, stdout=subprocess.PIPE).stdout.read()
	print answer
	r.send(answer)
	sleep(0.5)


		
r.interactive()
```
