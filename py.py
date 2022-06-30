import os


i = 1
num = int(input(' enter you number for attacking:  '))
while i < num:
    i+=1
    file = open(str(i)+'.txt' , 'w')
    file.write('hello world!\nhello world\nhello world\n')
    file.close()
os.system('clear&&ls -p')
a = str(input('exit   y, n?'))
if a == 'y':
    exit()
else:
    os.system('clear')
    print('\t\t\t___________')
    print('\t\t\t|         |')
    print('\t\t\t|   0 0   |')
    print('\t\t\t|   ٰٰٰٰٖ  ٰٰٰٰ    |')
    print('\t\t\t|    ًًًًً ًًًًًّّّ ًًًًً   |')
    print('\t\t\t|    َََََ<ٍٍٍٍٍٍٍٍٍٍّْٰٰٖ^َََََّٖ>  |')
    print('\t\t\t|         |')
    print('\t\t\t|         |')
    logout = input('\n Exit  y,n ?')
    if type(logout) != str:
      while type(logout)!=str:
        logout = input('\n Exit  y,n ?')
    else if logout === 'n':
      os.system('clear')
      print('\t\t\t___________')
      print('\t\t\t|         |')
      print('\t\t\t|   0 0   |')
      print('\t\t\t|   ٰٰٰٰٖ  ٰٰٰٰ    |')
      print('\t\t\t|    ًًًًً ًًًًًّّّ ًًًًً   |')
      print('\t\t\t|    َََََ<ٍٍٍٍٍٍٍٍٍٍّْٰٰٖ^َََََّٖ>  |')
      print('\t\t\t|         |')
      print('\t\t\t|         |')
    else if logout === 'y'||logout === 'Y':
      os.system('clear')
      print('\n\n••••••••••••••\n')
      print('\n\n••••••••••••••\n')
      print('\n\n••••••••••••••\n')