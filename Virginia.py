# -*- coding: utf-8 -*-
import re
import sys
class VirginiaCode(object):
    def __init__(self):
        self.key = sys.argv[1]
        self.code = sys.argv[3]
        self.model = sys.argv[2]
        self.letterSList = self.mapSletter()
        self.letterBList = self.mapBletter()
        
    def mapSletter(self):
        letter = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
        return letter.split(',')
    
    def mapBletter(self):
        letter = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
        return letter.split(',')
    
    # 產生秘鑰
    def virginiaKeyPro(self,cipher,key):
        keyTmp = key * ((len(cipher)/len(key))+1)
        return keyTmp[:len(cipher)]
    
    # 加密
    def virginiaEncryp(self,cipher,key):
        virginiaKey = self.virginiaKeyPro(cipher,key)
        encryp=''
        for a,b in zip(cipher,virginiaKey):
            if a ==' ' or a=='_' or a=='＿':
                encryp+=a
            else:
                if re.match(r'[a-z]', a) != None:
                    if re.match(r'[a-z]', b) != None:
                        keyIndex = self.letterSList.index(b)
                    elif re.match(r'[A-Z]', b) != None:
                        keyIndex = self.letterBList.index(b)
                    cipherIndex = self.letterSList.index(a)
                    encrypLetter = self.letterSList[(keyIndex+cipherIndex)%26]
                    encryp+=encrypLetter
                elif re.match(r'[A-Z]', a) != None:
                    if re.match(r'[a-z]', b) != None:
                        keyIndex = self.letterSList.index(b)
                    elif re.match(r'[A-Z]', b) != None:
                        keyIndex = self.letterBList.index(b)
                    cipherIndex = self.letterBList.index(a)
                    encrypLetter = self.letterBList[(keyIndex+cipherIndex)%26]
                    encryp+=encrypLetter                
                else:
                    print('無法加密'+'\n'+'請輸入英文(目前只提供小寫) or 空白 底線皆可加密')
                    return None  
        return encryp
    
    # 解密
    def virginiaDecrypt(self,cipher,key):
        virginiaKey = self.virginiaKeyPro(cipher,key)
        decrypt = ''
        for a,b in zip(cipher,virginiaKey):
            if a ==' ' or a=='_' or a=='＿':
                decrypt+=a
            else:
                if re.match(r'[a-z]', a) != None:
                    if re.match(r'[a-z]', b) != None:
                        keyIndex = self.letterSList.index(b)
                    elif re.match(r'[A-Z]', b) != None:
                        keyIndex = self.letterBList.index(b)
                    cipherIndex = self.letterSList.index(a)
                    decryptLetter = self.letterSList[( cipherIndex-keyIndex+26 )%26]
                    decrypt+=decryptLetter
                elif re.match(r'[A-Z]', a) != None:
                    if re.match(r'[a-z]', b) != None:
                        keyIndex = self.letterSList.index(b)
                    elif re.match(r'[A-Z]', b) != None:
                        keyIndex = self.letterBList.index(b)
                    cipherIndex = self.letterBList.index(a)
                    decryptLetter = self.letterBList[( cipherIndex-keyIndex+26 )%26]
                    decrypt+=decryptLetter                
                else:
                    print('無法解密'+'\n'+'請輸入英文(目前只提供小寫) or 空白 底線皆可解密')
                    return None                
        return decrypt

    def run(self):
        if self.model=='-e':  
            print(self.virginiaEncryp(self.code,self.key))
        elif self.model=='-d':
            print(self.virginiaDecrypt(self.code,self.key))
        else:
            print('model錯誤 只有 -e,-d')
#主函數
def main() :
    virginiaCode = VirginiaCode()
    virginiaCode.run()

if __name__ == '__main__' :
    main()