# Vigen-re-cipher
###執行環境 
python2.7x
###virginia  加密解密  
####如何使用
---

    $ python virginia.py key model code 

key 為鑰匙  
code 為加解密的字串   
model 有兩種 -e 執行加密 -d 執行解密  
`code可接受空格和底線，並且英文大小寫都可執行加解密  `  
`key可支援英文大小寫`
#### example
python virginia.py "lemon" -e "attackatdA \_"    
`lxfopvefrN _ `  
python virginia.py "lemon" -d "lxfopvefrN \_"  
`attackatdA _`
###Caesar 加密解密  
####如何使用
---

    $ python Caesar.py code model shifting 

shifting 為位移的數字  
code 為加解密的字串   
model 有兩種 -e 執行加密 -d 執行解密  
`code可接受空格和底線，並且英文大小寫都可執行加解密  `  
#### example
python Caesar.py "A a_nnersmakethmaN" -e 3    
`D d_qqhuvpdnhwkpdQ `  
python Caesar.py "D d_qqhuvpdnhwkpdQ" -d 3  
`A a_nnersmakethmaN`  
## 線上demo
 [ipynb 線上看](http://nbviewer.ipython.org/url/hpdswy.ee.ncku.edu.tw/~wy/ipynb/Caesar&%20Virginia%E5%8A%A0%E5%AF%86%E8%A7%A3%E5%AF%86.ipynb)
