 


  
  
 
  


      ​today​=​date​.​today​() 
      ​def​ ​hero​(): 
  
 ​    ​def​ ​chalo​(): 
 ​        ​done​ ​=​ ​False 
 ​        ​#here is the animation 
 ​        ​def​ ​animate​(): 
 ​            ​for​ ​c​ ​in​ ​itertools​.​cycle​([​'|'​, ​'/'​, ​'-'​, ​'​\\​'​]) : 
 ​                ​if​ ​done​: 
 ​                    ​break 
 ​                ​sys​.​stdout​.​write​(​'​\r​hacking in the parity server for next colour--------- '​ ​+​ ​c​) 
 ​                ​sys​.​stdout​.​flush​() 
 ​                ​time​.​sleep​(​0.1​) 
 ​            ​sys​.​stdout​.​write​(​'​\r​Done!     '​) 
  
 ​        ​t​ ​=​ ​threading​.​Thread​(​target​=​animate​) 
 ​        ​t​.​start​() 
  
 ​        ​#long process here 
 ​        ​time​.​sleep​(​20​) 
 ​        ​done​ ​=​ ​True 
  
 ​    ​def​ ​chalo1​(): 
 ​        ​done​ ​=​ ​False 
 ​        ​#here is the animation 
 ​        ​def​ ​animate​(): 
 ​            ​for​ ​c​ ​in​ ​itertools​.​cycle​([​'|'​, ​'/'​, ​'-'​, ​'​\\​'​]): 
 ​                ​if​ ​done​: 
 ​                    ​break 
 ​                ​sys​.​stdout​.​write​(​'​\r​getting the colour wait --------- '​ ​+​ ​c​) 
 ​                ​sys​.​stdout​.​flush​() 
 ​                ​time​.​sleep​(​0.1​) 
 ​            ​sys​.​stdout​.​write​(​'​\r​Done!     '​) 
  
 ​        ​t​ ​=​ ​threading​.​Thread​(​target​=​animate​) 
 ​        ​t​.​start​() 
  
 ​        ​#long process here 
 ​        ​time​.​sleep​(​20​) 
 ​        ​done​ ​=​ ​True 
  
 ​    ​def​ ​clear​(): 
 ​        ​# for windows 
 ​        ​if​ ​name​ ​==​ ​'nt'​: 
 ​            ​_​ ​=​ ​system​(​'cls'​) 
 ​        ​# for mac and linux(here, os.name is 'posix') 
 ​        ​else​: 
 ​            ​_​ ​=​ ​system​(​'clear'​) 
  
 ​    ​clear​() 
 ​    ​y​=​1 
 ​    ​newperiod​=​period 
 ​    ​banner​=​'figlet RXCE' 
 ​    ​m​=​0 
 ​    ​i​=​1 
 ​    ​thisway​=​[​1​,​2​,​4​,​5​,​7​,​8​,​9​,​15​,​18​,​19​,​20​] 
 ​    ​thatway​=​[​3​,​6​,​10​,​11​,​12​,​13​,​14​,​16​,​17​] 
 ​    ​numbers​=​[] 
 ​    ​while​(​y​): 
 ​        ​clear​() 
 ​        ​system​(​banner​) 
 ​        ​print​(​"Contact me on telegram @smsn_knt"​) 
 ​        ​print​(​"Enter "​,​newperiod​,​" Parity Price :"​) 
 ​        ​current​=​input​() 
 ​        ​current​=​int​(​current​) 
 ​        ​#chalo() 
 ​        ​print​(​"​\n​---------Successfully hacked the server-----------"​) 
 ​        ​#chalo1() 
 ​        ​print​(​"​\n​---------Successfully got the colour -------------"​) 
 ​        ​print​(​'​\n​'​) 
 ​        ​def​ ​getSum​(​n​): 
 ​            ​sum​=​0 
 ​            ​for​ ​digit​ ​in​ ​str​(​n​): 
 ​                ​sum​ ​+=​ ​int​(​digit​) 
 ​            ​return​ ​sum 
 ​        ​if​ ​i​ ​in​ ​thisway​: 
 ​            ​m​=​getSum​(​current​) 
 ​            ​n​=​int​(​current​)​%​10 
 ​            ​if​((​m​%​2​==​0​ ​and​ ​n​%​2​==​0​) ​or​ (​m​%​2​==​1​ ​and​ ​n​%​2​==​1​)): 
 ​                ​if​ ​current​ ​in​ ​numbers​: 
 ​                    ​print​(​newperiod​+​1​,​" : RED"​) 
 ​                ​else​: 
 ​                    ​print​(​newperiod​+​1​,​" : GREEN"​) 
 ​            ​else​: 
 ​                ​if​ ​current​ ​in​ ​numbers​: 
 ​                    ​print​(​newperiod​+​1​,​" : GREEN"​) 
 ​                ​else​: 
 ​                    ​print​(​newperiod​+​1​,​" : RED"​) 
 ​        ​if​ ​i​ ​in​ ​thatway​: 
 ​            ​m​=​getSum​(​current​)​+​1 
 ​            ​n​=​int​(​current​)​%​10 
 ​            ​if​((​m​%​2​==​0​ ​and​ ​n​%​2​==​0​) ​or​ (​m​%​2​==​1​ ​and​ ​n​%​2​==​1​)): 
 ​                ​if​ ​current​ ​in​ ​numbers​: 
 ​                    ​print​(​newperiod​+​1​,​": RED"​) 
 ​                ​else​: 
 ​                    ​print​(​newperiod​+​1​,​": GREEN"​) 
 ​            ​else​: 
 ​                ​if​ ​current​ ​in​ ​numbers​: 
 ​                    ​print​(​newperiod​+​1​,​": GREEN"​) 
 ​                ​else​: 
 ​                    ​print​(​newperiod​+​1​,​": RED"​) 
 ​        ​i​=​i​+​1 
 ​        ​newperiod​+=​1 
 ​        ​numbers​.​append​(​current​) 
 ​        ​y​=​input​(​"Do you want to play : Press 1 and 0 to exit ​\n​"​) 
 ​        ​if​(​y​==​0​): 
 ​            ​y​=​False 
 ​        ​if​ (​len​(​numbers​)​>​11​): 
 ​            ​clear​() 
 ​            ​system​(​'figlet Thank you!!'​) 
 ​            ​print​(​"Play on next specified time!!"​) 
 ​            ​print​(​"-----------Current Time UP----------"​) 
 ​            ​sys​.​exit​(​" ​\n​ ​\n​ ​\n​ Contact on Telegram @smsn_knt"​) 
 ​            ​#print(numbers) 
  
  
 ​if​(​expirydate​>​today​ ​and​ ​playday​==​today​): 
 ​    ​now​ ​=​ ​datetime​.​datetime​.​now​() 
 ​    ​First​ ​=​ ​now​.​replace​(​hour​=​10​, ​minute​=​55​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Firstend​ ​=​ ​now​.​replace​(​hour​=​11​, ​minute​=​35​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Second​ ​=​ ​now​.​replace​(​hour​=​14​, ​minute​=​25​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Secondend​ ​=​ ​now​.​replace​(​hour​=​15​, ​minute​=​5​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Third​ ​=​ ​now​.​replace​(​hour​=​17​, ​minute​=​25​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Thirdend​ ​=​ ​now​.​replace​(​hour​=​18​, ​minute​=​5​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Final​ ​=​ ​now​.​replace​(​hour​=​20​, ​minute​=​25​, ​second​=​0​, ​microsecond​=​0​) 
 ​    ​Finalend​ ​=​ ​now​.​replace​(​hour​=​21​, ​minute​=​5​, ​second​=​0​, ​microsecond​=​0​) 
  
 ​    ​if​ (​now​>​First​ ​and​ ​now​<​Firstend​): 
 ​            ​period​=​220 
 ​            ​#hero() 
 ​    ​elif​(​now​>​Second​ ​and​ ​now​<​Secondend​): 
 ​            ​period​=​290 
 ​            ​banner​=​'figlet RXCE' 
 ​            ​system​(​banner​) 
 ​            ​print​(​"Server Overloading....."​) 
 ​            ​time​.​sleep​(​3​) 
 ​            ​print​(​"Please try again later"​) 
 ​            ​exit​() 
 ​            ​#hero() 
 ​    ​elif​(​now​>​Third​ ​and​ ​now​<​Thirdend​): 
 ​            ​period​=​350 
 ​            ​hero​() 
 ​    ​elif​(​now​>​Final​ ​and​ ​now​<​Finalend​): 
 ​            ​period​=​410 
 ​            ​hero​() 
 ​    ​else​: 
 ​        ​banner​=​'figlet RXCE' 
 ​        ​print​(​"Hi!! Thanks for buying the hack"​) 
 ​        ​print​(​"----------Your play time-----------"​) 
 ​        ​print ("11:00 AM- 11:30 AM") 
 ​        ​print ("02:30 PM- 03:00 PM") 
 ​        ​print​("05:30 PM- 06:00 PM") 
 ​        ​print​("08:30 PM- 09:00 PM") 
 ​        ​print​(​"Please play on the given time, and "​) 
 ​        ​print​(​"If you think it is an error contact"​) 
 ​        ​print​(​" admin on telegram @smsn_knt "​) 
 ​elif​(today): 
 ​    ​banner​=​'figlet RXCE' 
 ​    ​system​(​banner​) 
 ​    ​print​(​"Hi!! Thanks for buying the hack"​) 
 
 ​    ​print​(​"Thank you!! for ur understanding"​) 
 ​    ​print​(​"----------Your play time-----------"​) 
 ​    ​print ("11:00 AM- 11:30 AM") 
 ​    ​print​("02:30 PM- 03:00 PM") 
 ​    ​print​("05:30 PM- 06:00 PM") 
 ​    ​print​("08:30 PM- 09:00 PM") 
 ​    ​print​(​"Please play on the given time, and "​) 
 ​    ​print​(​"If you think it is an error contact"​) 
 ​    ​print​(​" admin on telegram @smsn_knt "​) 
  
 
 
  
 
