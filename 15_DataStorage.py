# ð¥ð¥ð¥æ°æ®å­å¨(ææ°æ®å­å¨å°ç¡¬çä¸)

# â°ï¸ä¿®æ¹ ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# ð¥æå¼æä»¶
f = open('TheBest.txt', 'w') # é»è®¤åå»ºå¨ä¸»æä»¶å¤¹ä¸ãæå¼çæ¨¡å¼('w' ä¸ºåå¥æ¨¡å¼)
f.write('ðHello World!') # æä½æä»¶, æåä¸ªå­ç¬¦ä¸²åå¥å°æä»¶ä¸­
f.writelines(['ðThe long words.'])# æå¤ä¸ªå­ç¬¦ä¸²åå¥å°æä»¶ä¸­, å¦æéè¦éè¦èªå·±æ·»å æ¢è¡ç¬¦  \n
f.close() # â¡ï¸å³é­æä»¶å¯¹è±¡åï¼è¾å¥æä¼ä»ç¼å²åºåå¥å°æä»¶ä¸­



# ð¥éæ°æå¼æä»¶ï¼ï¼éæ°åç¹åå®¹è¿å»ï¼â¡ï¸æ³¨æï¼æä»¶è¢«å³é­åå°±æ æ³åå¥äºï¼è¦éæ°æå¼ï¼ï¼
# ð¥æå¼æä»¶çæ¹å¼ä¸:
f = open('TheBest.txt', 'r+') # éæ°æå¼æä»¶, åå¥æ°åå®¹(â¡ï¸â¡ï¸ç¨'r', è¿æ ·æä¸ä¼éæ°æªæ­ï¼ï¼)
f.write('ðNew words~') # æä½æä»¶, åå¥æ°çåå®¹s
# print(f.readable()) 



# ð¥æå¼æä»¶çæ¹å¼äº:
from pathlib import Path
g = Path.cwd()
g = g / "TheBest2.txt"
gg = g.open('w')
gg.write('ðä½ å¥½å')
gg.flush()




# ð¥ð¥ð¥ç¨ with è¯­å¥æå¼æä»¶(ä¸éè¦æå¨çå³é­æä»¶!!!)
with open('TheBest4.txt', 'w') as vv:
	vv.write('ð±è¿æ¯ä¸ä¸ªæ°åå®¹')  # â¡ï¸â¡ï¸â¡ï¸ä¸éè¦æå¨çå³é­æä»¶!!!




# ð¥ð¥ð¥æ°¸ä¹çæ Python å¯¹è±¡å­(å­ç¬¦ä¸²ãåç»ãåºåãå­å¸ç­) å¨å°æä»¶ä¸­ï¼ï¼åºååï¼è½¬ä¸ºäºè¿å¶çæ ¼å¼ï¼
import pickle

x, y, z = 43, 44, 45
aa = 'Zen'
ll = ['Hey', 996, 3.14]
dd = {'name': 'Zen', 'age': 18}

with open('data.pkl', 'wb') as kkn: # ð¥ ç¨ .pkl çå½¢å¼ï¼å­å¨ä¸ºäºè¿å¶æä»¶ï¼
	pickle.dump(x, kkn)
	pickle.dump(y, kkn)
	pickle.dump(z, kkn)
	pickle.dump(aa, kkn)
	pickle.dump(ll, kkn)
	pickle.dump(dd, kkn)
	# pickle((x, y, z, aa, ll, dd), kkn) # æ´ç®ä¾¿çåæ³: æåä¸ºåç»


with open('data.pkl', 'rb') as kkn: # ð¥ ç¨ .pkl è¯»åäºè¿å¶æä»¶
	x = pickle.load(kkn)
	y = pickle.load(kkn)
	z = pickle.load(kkn)
	aa = pickle.load(kkn)
	ll = pickle.load(kkn)
	dd = pickle.load(kkn)
	# x, y, z, aa, ll, dd = pickle.load(kkn) # æ´ç®ä¾¿çåæ³: æåç»è§£å

print(x, y, z, aa, ll, dd, sep = '\n') # â°ï¸ sep = '\n' ä¸ºæ¢è¡




# ð¥æä»¶å¯ä»¥è¢«è¿­ä»£ãæä»¶æé
# è¿­ä»£å®æ¯åï¼ãâ¡ï¸â¡ï¸æä»¶åæ ãæåæä»¶æ«å°¾ï¼ï¼å¯ä»¥éè¿ f.tell() æ¥æ¥çæä»¶æéçä½ç½®
for i in f:
	print(i) # æ­¤æ¶ ðNew words~ è¿æ²¡è¢«åå¥ï¼ï¼

print(f.tell())#â¡ï¸ æ¥çãæä»¶åæ ãçä½ç½®(åçå¨åªä¸ªå­ç¬¦çä½ç½®)
f.seek(0)# â¡ï¸éç½®ãæä»¶åæ ãçä½ç½®ï¼




f.close() # â¡ï¸å³é­æä»¶å¯¹è±¡åï¼è¾å¥æä¼ä»ç¼å²åºåå¥å°æä»¶ä¸­




# ð¥å¨ä¸å³é­çæåµä¸åå¥æä»¶åå®¹
f = open('TheBest.txt', 'r+')
f.write("ðIt's new words")
f.flush() # â¡ï¸å·æ°ç¼å²åºï¼æåå®¹åå¥å°æä»¶ä¸­


# ð¥æªåæä»¶åå®¹(å é¤æä»¶åå®¹å°åªä¸è¡ï¼
# f.truncate(29) # ä¸:æå®åæ çä½ç½®æ¥æªå
# f = open('TheBest.txt', 'w') # äº: éæ°ç¨ w æ¨¡å¼æå¼ï¼ð¥å°±ä¼æ¸ç©ºä¹åçåå®¹ï¼ï¼






# ð¥ð¥è·¯å¾æä»¶(ç¸å¯¹è·¯å¾ï¼ç¸å¯¹äºå½åæä»¶å¤¹ï¼ç»å¯¹è·¯å¾ï¼ç¸å¯¹äºç³»ç»æ ¹ç®å½)
from pathlib import Path
x = Path.cwd()
print(x)

# ð¥ææä»¶å å°æä¸ªè·¯å¾ä¸
y = x / "TheBest.txt"






# â°ï¸æ°å¢ ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# ð¥åå»ºæä»¶å¤¹
n = x / 'NewFolder'
# n.mkdir() # â¡ï¸â¡ï¸â¡ï¸åå»ºæä»¶å¤¹(â°ï¸â°ï¸å¦ææä»¶å¤¹å·²ç»å­å¨ï¼â ï¸â ï¸å°±ä¼æ¥éï¼)


# ð¥å¦æç¶çº§è·¯å¾ä¸å­å¨ï¼åä¼æ¥éï¼è¦æ³ä¸æ¥éçè¯å¯ä»¥ç¨ exist_ok=True
n = x / 'NewFolder/A/B/C'
n.mkdir(parents=True, exist_ok=True)





# ð¥ä¿®æ¹æä»¶å¤¹åç§°
n.rename('TheBestNewName98')

# ð¥ä¿®æ¹æä»¶åç§°
m = Path('TheBest2.txt')
m.replace('TheBest3.txt')








# â°ï¸æ¥è¯¢ ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# ð¥å¤æ­ä¸ä¸ªè·¯å¾æ¯å¦æ¯æä»¶å¤¹
print(x.is_dir()) # Trueï¼æ¯æä»¶å¤¹

# ð¥å¤æ­ä¸ä¸ªè·¯å¾æ¯å¦æ¯æä»¶
print(y.is_file()) # Trueï¼æ¯æä»¶

# ð¥å¤æ­ä¸ä¸ªè·¯å¾æ¯å¦å­å¨
z = Path('C/404').exists() # Falseï¼ä¸å­å¨
print(z) # False

# ð¥è·åè·¯å¾çåç¼
print('æä»¶åç¼:',y.suffix)

# ð¥è·åæä»¶çãæåä¸é¨åã
print('æä»¶æåä¸é¨å:', y.name)

# ð¥è·åæä»¶å
print('æä»¶å:', y.stem)

# ð¥è·åæä»¶çãç¶çº§ç®å½ã
print('ç¶çº§ç®å½:', y.parent)

# ð¥è·åæä»¶çææç¶çº§ç®å½
zz = y.parents
for each in zz:
	print(each) # æå°ææè·¯å¾
	print(zz[2]) # æå°å¶ä¸­ä¸æ¡è·¯å¾

# ð¥æ¥è¯¢æä»¶ãæä»¶å¤¹çä¿¡æ¯ãå¯ä»¥ç¨æ¥æ¥è¯¢æä»¶å°ºå¯¸
print(y.stat().st_size) # st_xxxx ... éè¾¹æåç§æ¹æ³

# ð¥ç¸å¯¹è·¯å¾è½¬åä¸ºç»å¯¹è·¯å¾
print(y.resolve())

# ð¥è·åå½åè·¯å¾ä¸çææå­æä»¶å¤¹ãåå­æä»¶, å°ä¼è¿åä¸ä¸ª generator object çæå¨
print(list(x.iterdir())) # çæå¨å¯¹è±¡ï¼éè¦è½¬åä¸º list

print('__åå²çº¿__')

# ð¥è¿æ»¤åºå½åè·¯å¾ä¸çæææä»¶
res = [xx for xx in x.iterdir() if xx.is_file()]
print(res)



h = Path('.')
h.glob('%.txt') # â¡ï¸â¡ï¸â¡ï¸è·åå½åè·¯å¾ä¸çææ .txt æä»¶
list(h.glob('*/*.py')) #è·åå½åè·¯å¾ä¸çææä¸ä¸çº§ç®å½ç .py æä»¶
list(h.glob('**/*.py')) #è·åå½åè·¯å¾ä¸ãä»¥åææå­ç®å½çä¸ä¸çº§ç®å½ç .py æä»¶



# â°ï¸å é¤ ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# ð¥å é¤æä»¶å¤¹(åææ¯éè¦åå é¤éè¾¹çæä»¶ï¼)
pp = Path('TheBest4Folder')
# pp.unlink() # å é¤åå°±æ²¡äºï¼æä»¥ä¼æ¥é
# pp.parent.rmdir() # å é¤åå°±æ²¡äºï¼æä»¥ä¼æ¥é

