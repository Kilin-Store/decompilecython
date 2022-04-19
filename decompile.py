#!/usr/bin/python1.7
#coding=utf-8
import marshal,os,sys,time

os.system("clear")
aleju = ("""
     ╔╦╗┌─┐┬─┐┌─┐┬ ┬┌─┐┬
     ║║║├─┤├┬┘└─┐├─┤├─┤│
     ╩ ╩┴ ┴┴└─└─┘┴ ┴┴ ┴┴─┘
     Creator : Mikasa Ex
     Youtube : Firzz Tutorial\n""")
def aleeju():
        try:
                print (aleju)
                print ('   [-] Contoh > /sdcard/file.py')
                file = input ('   [-] File Kamu : ')
                fileopen = open(file).read()
                a = compile(fileopen, 'dg', 'exec')
                m = marshal.dumps(a)
                s = repr(m)
                b = ('import marshal\nexec(marshal.loads(' + s +'))')
                c = file.replace('.py', '.py')
                d = open(c, 'w')
                d.write(b)
                d.close()
                print ('   [-] Berhasil > ',c)
                time.sleep(1)
                aq = input ('  [-] Ingin encrypt lagi? [Y/N]')
                if aq =="":
                        print ('   Command not found !')
                        os.sys.exit()
                elif aq =="y" or aq =="Y":
                        aleeju()
                else:
                        if aq =="n" or aq =="N":
                                print ('   > Terimakasih anjeng ;v\n')
                        else:
                                print ('   Command not found !')
                                os.sys.exit()
        except IOError:
                print ('   File Tidak Ditemukan ! ')
                time.sleep(1)
                aleeju()

if __name__=='__main__':
        aleeju()
