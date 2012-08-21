# -*- coding:utf-8 -*-
import cmd
import urllib
import sys
import chardet
from chardet.universaldetector import UniversalDetector
class definecode(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.preaddr="http://"
        self.prompt='(testcode)>'
        self.intro='''
        website 输入网址  输入要检测编码方式的网站的网址
        exit or q    退出程序
        '''
    def help_exit(self):
        print "退出程序"
    def do_exit(self,line):
        sys.exit()

    def help_website(self):
        print "输入网站的网址"
    def do_website(self,website):
         if website=='':
             website=raw_input("输入网址 ")
         if not self.preaddr in website:
             website=self.preaddr+website 
         sock = urllib.urlopen(website)
         detector = UniversalDetector()
         for line in sock.readlines():
             detector.feed(line)
             if detector.done:
                 break
         detector.close()
         sock.close()
         result = detector.result
         print "该网站的编码是 "+result['encoding']
     
    def help_files(self):
         print "输入文件完整路径和文件名"
    def do_files(self,filenames):
         if filenames=='':
             filenames=raw_input("输入文件完整路径和文件名")
         f = open(filenames)
         detector = UniversalDetector()
         for line in f.readlines():
             detector.feed(line)
             if detector.done:
                 break
         detector.close()
         f.close()
         result = detector.result
         print "该文件的编码是 "+ result['encoding']
    
    do_q = do_exit

if __name__ == '__main__':
    testcode = definecode()
    testcode.cmdloop()
