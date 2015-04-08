# -*- coding: utf-8 -*-
import re
import sys
class CaesarCode(object):
    def __init__(self):
        self.code = sys.argv[1]
        self.model = sys.argv[2]
        self.shifting = int(sys.argv[3])
        self.letterSList = self.mapSletter()
        self.letterBList = self.mapBletter()
        
    def mapSletter(self):
        letter = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
        return letter.split(',')
    
    def mapBletter(self):
        letter = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'
        return letter.split(',')
    
    # 加密
    def CaesarEncryption(self,cipher,shifting):    
        encryption =''
        for t in cipher:
            # 遇到 空白和底線不加密
            if t ==' ' or t=='_' or t=='＿':
                encryption += t
            else:
                # 小寫加密
                if re.match(r'[a-z]', t) != None:
                    cipherNum = self.letterSList.index(t)
                    cipherShiftingNum = (cipherNum+shifting)%26
                    encryption += self.letterSList[cipherShiftingNum]
                # 大寫加密
                elif re.match(r'[A-Z]', t) != None:
                    cipherNum = self.letterBList.index(t)
                    cipherShiftingNum = (cipherNum+shifting)%26
                    encryption += self.letterBList[cipherShiftingNum]
                # 超出可加密的範圍
                else:
                    print(t+'\n'+'無法加密'+'\n'+'請輸入英文(大小寫皆可) or 空白 底線皆可加密')
                    return None
        return encryption 

    # 解密
    def CaesarDecrypt(self,cipher,shifting):    
        decrypt=''
        for t in cipher:
            # 遇到 空白和底線不解密
            if t ==' ' or t=='_' or t=='＿':
                decrypt += t
            else:
                # 小寫解密
                if re.match(r'[a-z]', t) != None:
                    cipherNum = self.letterSList.index(t)
                    cipherShiftingNum = (cipherNum-shifting)%26
                    decrypt +=self.letterSList[cipherShiftingNum]
                # 大寫解密
                elif re.match(r'[A-Z]', t) != None:
                    cipherNum = self.letterBList.index(t)
                    cipherShiftingNum = (cipherNum-shifting)%26
                    decrypt +=self.letterBList[cipherShiftingNum]
                # 超出可解密的範圍
                else:
                    print(t+'\n'+'無法解密'+'\n'+'請輸入英文(大小寫皆可) or 空白 底線皆可解密')
                    return None
        return decrypt 

    def run(self):
        if self.model=='-e':  
            print(self.CaesarEncryption(self.code,self.shifting))
        elif self.model=='-d':
            print(self.CaesarDecrypt(self.code,self.shifting))
        else:
            print('model錯誤 只有 -e,-d')
#主函數
def main() :
    caesarCode = CaesarCode()
    caesarCode.run()

if __name__ == '__main__' :
    main()