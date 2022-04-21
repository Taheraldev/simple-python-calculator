import sys
import os
import time
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop

numbers={}
cntr=0
flagOfDo=0
result=1
def handle(msg):
    global flagOfLevel
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='احسب📟', callback_data='1')]
    ])
    content_type, chat_type, chat_id = telepot.glance(msg)
#    print(msg)

    global flagOfDo
    global cntr
    global result
    if msg['text']=='/example':
        bot.sendPhoto(chat_id, photo='https://telegra.ph/botDifference-04-20')
    if msg['text']=='/homework':
        bot.sendPhoto(chat_id, photo='https://telegra.ph/btdifference-04-20')

    if msg['text']=='/laws':
        bot.sendMessage(chat_id,"قوانين  مستخدمة في بوت ""CALCULATOR Finite difference "
 "\nالفرق المحدود هو التناظرية المنفصلة للمشتق.\n"       
"\n 𝟏.𝐅𝐎𝐑𝐖𝐀𝐑𝐃 𝐃𝐈𝐅𝐅𝐄𝐑𝐄𝐍𝐂𝐄(طرح للأمام) \n"        
"\n 𝐹𝐼𝑅𝑆𝑇 𝐹𝑂𝑅𝑊𝐴𝑅𝐷 𝐷𝐼𝐹𝐹𝐸𝑅𝐸𝑁𝐶𝐸 \n"  
"\n∆ƒⱼ = ƒⱼ+₁ - ƒⱼ\n"      
"\n𝚂𝙴𝙲𝙾𝙽𝙳 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝙳𝙸𝙵𝙵𝙴𝚁𝙴𝙽𝙲𝙴\n"
"\n∆²ƒⱼ = ∆ƒⱼ+₁ - ∆ƒⱼ\n"
"\n𝐾ᵗʰ 𝐹𝑂𝑅𝑊𝐴𝑅𝐷 𝐷𝐼𝐹𝐹𝐸𝑅𝐸𝑁𝐶𝐸\n"
"\n∆ᵏƒⱼ = ∆ᵏˉ¹ƒⱼ+₁ - ∆ᵏˉ¹ƒⱼ\n"
"\nwhere(حيث) : K=1,2,3,.......\n"
"\n𝟐.𝐁𝐀𝐂𝐊𝐖𝐀𝐑𝐃 𝐃𝐈𝐅𝐅𝐄𝐑𝐄𝐍𝐂𝐄\n"
"\n 𝐹𝐼𝑅𝑆𝑇 𝙱𝙰𝙲𝙺𝚆𝙰𝚁𝙳 𝐷𝐼𝐹𝐹𝐸𝑅𝐸𝑁𝐶𝐸 \n"  
"\n∇ƒⱼ = ƒⱼ - ƒⱼ-₁\n"      
"\n𝚂𝙴𝙲𝙾𝙽𝙳 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝙳𝙸𝙵𝙵𝙴𝚁𝙴𝙽𝙲𝙴\n"
"\n∇²ƒⱼ = ∇ƒⱼ - ∇ƒⱼ-₁\n"
"\n𝐾ᵗʰ 𝙱𝙰𝙲𝙺𝚆𝙰𝚁𝙳 𝐷𝐼𝐹𝐹𝐸𝑅𝐸𝑁𝐶𝐸\n"
"\n∇ᵏƒⱼ = ∇ᵏˉ¹ƒⱼ - ∇ᵏˉ¹ƒⱼ-₁\n"
"\nwhere(حيث) : K=1,2,3,.......\n"
"\n {made by dev:@ta_ja199 🧑🏻‍💻}\n")

    if msg['text']=='/start':
        bot.sendMessage(chat_id," مرحبا بك في بوت التحليلات الهندسية" 
"\n𝙲𝙰𝙻𝙲𝚄𝙻𝙰𝚃𝙾𝚁 𝙵𝙸𝙽𝙸𝚃𝙴 𝙳𝙸𝙵𝙵𝙴𝚁𝙴𝙽𝙲𝙴(حاسبة الفرق المحدود)\n" 
"\n شرح عن الموضوع والقوانين الممستخدمة اضغط : /laws   \n" 
"\n  مثال عن موضوع الفرق المحدود : /example   \n" 
"\n  واجب بيتي عن موضوع الفرق المحدود : /homework   \n" 
"\n 【made by  dev:@ta_ja199 🧑🏻‍💻】\n"
"\n f(x)j= when(عندما) j=0,1,2,3,4\n"
"\n هيا لنبدا 👇👇\n"
"\n〔 (f(x)j= when(عندما) j=0 )الان أرسل قيمة 〕\n")
        flagOfDo=1
        cntr=0
        return
        
    numbers[cntr]=float(msg['text'])
    
    if cntr==9:
        bot.sendMessage(chat_id,'اضغط احسب لعرض النتائج⌛',reply_markup=keyboard)
        cntr=0
        result=0
    
    if result==1:
        if flagOfDo==1:
            bot.sendMessage(chat_id,'(f(x)j= when(عندما) j=1 ):ارسل  قيمة ')
            flagOfDo=2
            cntr=1
            return
    if result==1:
        if flagOfDo==2:
            bot.sendMessage(chat_id,'(f(x)j= when(عندما) j=2 ):ارسل  قيمة')
            flagOfDo=3
            cntr=2
            return  
    if result==1:
        if flagOfDo==3:
            bot.sendMessage(chat_id,'(f(x)j= when(عندما) j=3 ):ارسل  قيمة')
            flagOfDo=4
            cntr=3
            return  
    if result==1:
        if flagOfDo==4:
            bot.sendMessage(chat_id,'(f(x)j= when(عندما) j=4 ):ارسل  قيمة')
            flagOfDo=5
            cntr=4
            return
    if result==1:
        if flagOfDo==5:
            bot.sendMessage(chat_id,'(xo):ارسل  قيمة')
            flagOfDo=6
            cntr=5
            return            
    if result==1:
        if flagOfDo==6:
            bot.sendMessage(chat_id,'(x1):ارسل  قيمة')
            flagOfDo=7
            cntr=6
            return   
    if result==1:
        if flagOfDo==7:
            bot.sendMessage(chat_id,'(x2):ارسل  قيمة')
            flagOfDo=8
            cntr=7
            return 
    if result==1:
        if flagOfDo==8:
            bot.sendMessage(chat_id,'(x3):ارسل  قيمة')
            flagOfDo=9
            cntr=8
            return  
    if result==1:
        if flagOfDo==9:
            bot.sendMessage(chat_id,'(x4):ارسل  قيمة')
            flagOfDo=0
            cntr=9
            return                          
        else:
            bot.sendMessage(chat_id,'(f(x)j= when(عندما) j=0 )الان أرسل قيمة')
            flagOfDo=1
            return
#     bot.sendMessage(chat_id, message)
def on_callback_query(msg):
	
    query_id, from_id, query_data=telepot.glance(msg, flavor='callback_query')    
    #    print(msg)
    global result
    global numbers

    if query_data=='0':
        bot.sendMessage(from_id,'لتحديث بوت اضغط /start',reply_markup=keyboard)
        numbers={}
        
    elif query_data=='1':
        bot.sendMessage(from_id,'\n 𝟏.𝐅𝐎𝐑𝐖𝐀𝐑𝐃 𝐃𝐈𝐅𝐅𝐄𝐑𝐄𝐍𝐂𝐄 ✔''\n j=0,1,3,4\n Xj=' + str(numbers[5]) + ' , ' + str(numbers[6]) +' , '+ str(numbers[7])+ ' , '+str(numbers[8]) + ' , ' +str(numbers[9]) +'\n➖➖➖➖➖➖➖➖➖\n step(1,4) :\n〰️〰️〰️〰️〰️〰️〰️〰️〰️\n ∆ƒⱼ = ƒⱼ+₁ - ƒⱼ \n〰️〰️〰️〰️〰️〰️〰️〰️〰️\nj=0 , ∆f₀ = ƒ₁- f₀ = ' + str(round(numbers[1]-numbers[0], 3)) +'\nj=1 , ∆ƒ₁ = ƒ₂ - ƒ₁= ' + str(round(numbers[2]-numbers[1] , 3)) + '\nj=2 ,  ∆ƒ₂ = ƒ₃ - ƒ₂= ' +str(round(numbers[3]-numbers[2] , 3)) + '\nj=3 , ∆ƒ₃=ƒ₄-ƒ₃= ' + str(round(numbers[4]-numbers[3] , 3))+ '\nj=4 , ∆ƒ₄=ƒ₅-ƒ₄= ' + str(-1*numbers[4]) +'\n➖➖➖➖➖➖➖➖➖\n step(2,4) :\n〰️〰️〰️〰️〰️〰️〰️〰️〰️\n ∆²ƒⱼ = ∆ƒⱼ+₁ - ∆ƒⱼ \n〰️〰️〰️〰️〰️〰️〰️〰️〰️\nj=0 , ∆²f₀=∆ƒ₁-∆f₀=' + str(round((numbers[2]-numbers[1])-(numbers[1]-numbers[0]) , 3)) +'\nj=1 , ∆²ƒ₁=∆ƒ₂-∆ƒ₁='+str(round((numbers[3]-numbers[2])-(numbers[2]-numbers[1]) ,3))+'\nj=2 , ∆²ƒ₂ = ∆ƒ₃- ∆ƒ₂ = '+ str(round((numbers[4]-numbers[3])-(numbers[3]-numbers[2]) ,3))+'\n➖➖➖➖➖➖➖➖➖\n step(3,4) :\n〰️〰️〰️〰️〰️〰️〰️〰️〰️\n ∆³ƒⱼ = ∆ƒⱼ+₁ - ∆ƒⱼ \n〰️〰️〰️〰️〰️〰️〰️〰️〰️ \nj=0 , ∆³f₀ = ∆²ƒ₁- ∆²f₀ = ' + str(round((numbers[3]-numbers[2])-(numbers[2]-numbers[1])-((numbers[2]-numbers[1])-(numbers[1]-numbers[0])) ,3))+'\nj=1 , ∆³ƒ₁ = ∆²ƒ₂- ∆²ƒ₁ = '+ str(round((numbers[4]-numbers[3])-(numbers[3]-numbers[2])-((numbers[3]-numbers[2])-(numbers[2]-numbers[1])) ,3)) +'\n➖➖➖➖➖➖➖➖➖\n step(4,4) :\n〰️〰️〰️〰️〰️〰️〰️〰️〰️\n ∆⁴ƒⱼ = ∆³ƒⱼ+₁ - ∆³ƒⱼ \n〰️〰️〰️〰️〰️〰️〰️〰️〰️\nj=0 , ∆⁴f₀ =∆³ƒ₁ - ∆³f₀ = '+str(round((numbers[4]-numbers[3])-(numbers[3]-numbers[2])-((numbers[3]-numbers[2])-(numbers[2]-numbers[1]))-((numbers[3]-numbers[2])-(numbers[2]-numbers[1])-((numbers[2]-numbers[1])-(numbers[1]-numbers[0]))) ,3)))       
        bot.sendMessage(from_id,'\n 𝟐.𝐁𝐀𝐂𝐊𝐖𝐀𝐑𝐃 𝐃𝐈𝐅𝐅𝐄𝐑𝐄𝐍𝐂𝐄 ✔''\n➖➖➖➖➖➖➖➖➖\n step(1,4) :\n〰️〰️〰️〰️ 〰️〰️〰️〰️〰️\n ∇ƒⱼ = ƒⱼ+₁ - ƒⱼ \n〰️〰️〰️〰️〰️〰️〰️〰️〰️ \nj=0 , ∇f₀ = f₀- ƒ₁= ' + str(round(numbers[0]-numbers[1], 3)) +'\nj=1 , ∇ƒ₁ = ƒ₁ -ƒ₀= ' + str(round(numbers[1]-numbers[0] , 3)) + '\nj=2 ,  ∇ƒ₂ = ƒ₂ - ƒ₁= ' +str(round(numbers[2]-numbers[1] , 3)) + '\nj=3 , ∇ƒ₃= ƒ₃- ƒ₂= ' + str(round(numbers[3]-numbers[2] , 3))+ '\nj=4 , ∇ƒ₄ =ƒ₄ - ƒ₃= ' + str(round(numbers[4]-numbers[3] , 3)) +'\n➖➖➖➖➖➖➖➖➖\n step(2,4) :\n〰️〰️〰️〰️〰️〰️〰️〰️〰️\n ∇²ƒⱼ=∇ƒⱼ - ∇ƒⱼ-₁ \n〰️〰️〰️〰️〰️〰️〰️〰️〰️ \nj=0 , ∇²f₀=∇f₀-∇ƒ₁=' + str(round((numbers[0]-numbers[1])-(numbers[1]-numbers[0]) , 3)) +'\nj=1 , ∇²ƒ₁ = ∇ƒ₁- ∇f₀ = '+str(round((numbers[1]-numbers[0])-(numbers[0]-numbers[1]) ,3))+'\nj=2 , ∇²ƒ₂ = ∇ƒ₂- ∇ƒ₁ = '+ str(round((numbers[2]-numbers[1])-(numbers[1]-numbers[0]) ,3))+'\nj=3 , ∇²ƒ₃ = ∇ƒ₃-∇ƒ₂ = '+ str(round((numbers[3]-numbers[2])-(numbers[2]-numbers[1]) ,3))+'\nj=4 , ∇²ƒ₄ = ∇ƒ₄ - ∇ƒ₃ = '+ str(round((numbers[4]-numbers[3])-((numbers[3]-numbers[2])) ,3))+'\n➖➖➖➖➖➖➖➖➖\n step(3,4) :\n〰️〰️〰️〰️〰️〰️〰️〰️〰️\n ∇³ƒⱼ=∇²ƒⱼ - ∇ƒⱼ-₁ \n〰️〰️〰️〰️〰️〰️〰️〰️〰️ \nj=0 , ∇³f₀ = ∇²f₀ -∇²f-₁ = ' + str(round((numbers[0]-numbers[1])-(numbers[1]-numbers[0])-((numbers[1]-numbers[0])-(numbers[0]-numbers[1])) ,3))+'\nj=1 , ∇³ƒ₁ = ∇²ƒ₁- ∇²f₀ = '+ str(round((numbers[1]-numbers[0])-(numbers[0]-numbers[1])-((numbers[0]-numbers[1])-(numbers[1]-numbers[0])) ,3)) +'\nj=2 , ∇³ƒ₂ = ∇²ƒ₂ - ∇²ƒ₁ = '+ str(round((numbers[2]-numbers[1])-(numbers[1]-numbers[0])-((numbers[1]-numbers[0])-(numbers[0]-numbers[1])) ,3)) +'\nj=3 , ∇³ƒ₃ = ∇²ƒ₃ - ∇²ƒ₂ = '+ str(round((numbers[3]-numbers[2])-(numbers[2]-numbers[1])-((numbers[2]-numbers[1])-(numbers[1]-numbers[0])) ,3)) +'\nj=4 , ∇³ƒ₄ = ∇²ƒ₄ - ∇²ƒ₃ = '+ str(round((numbers[4]-numbers[3])-(numbers[3]-numbers[2])-((numbers[3]-numbers[2])-(numbers[2]-numbers[1])) ,3)) +'\n➖➖➖➖➖➖➖➖➖\n step(4,4) :\n〰️〰️〰️〰️〰️〰️〰️〰️〰️\n ∇⁴ƒⱼ = ∇³ƒⱼ - ∇³ƒⱼ-₁ \n〰️〰️〰️〰️〰️〰️〰️〰️〰️ \nj=0 , ∇⁴f₀ = ∇³f₀- ∇³ƒ₁ = '+str(round((numbers[0]-numbers[1])-(numbers[1]-numbers[0])-((numbers[1]-numbers[0])-(numbers[0]-numbers[1]))-((numbers[1]-numbers[0])-(numbers[0]-numbers[1])-((numbers[0]-numbers[1])-(numbers[1]-numbers[0]))) ,3))+'\nj=1 , ∇⁴ƒ₁ = ∇³ƒ₁ - ∇³f₀ = '+str(round((numbers[1]-numbers[0])-(numbers[0]-numbers[1])-((numbers[0]-numbers[1])-(numbers[1]-numbers[0]))-((numbers[0]-numbers[1])-(numbers[1]-numbers[0])-((numbers[1]-numbers[0])-(numbers[0]-numbers[1]))) ,3))+'\nj=2 , ∇⁴ƒ₂ = ∇³ƒ₂ - ∇³ƒ₁ = '+str(round((numbers[2]-numbers[1])-(numbers[1]-numbers[0])-((numbers[1]-numbers[0])-(numbers[0]-numbers[1]))-((numbers[1]-numbers[0])-(numbers[0]-numbers[1])-((numbers[0]-numbers[1])-(numbers[1]-numbers[0]))) ,3))+'\nj=3 , ∇⁴ƒ₃ = ∇³ƒ₃ - ∇³ƒ₂ = '+str(round((numbers[3]-numbers[2])-(numbers[2]-numbers[1])-((numbers[2]-numbers[1])-(numbers[1]-numbers[0]))-((numbers[2]-numbers[2])-(numbers[1]-numbers[0])-((numbers[1]-numbers[0])-(numbers[0]-numbers[1]))) ,3))+'\nj=4 , ∇⁴ƒ₄ = ∇³ƒ₄ - ∇³ƒ₃ = '+str(round((numbers[4]-numbers[3])-(numbers[3]-numbers[2])-((numbers[3]-numbers[2])-(numbers[2]-numbers[1]))-((numbers[3]-numbers[2])-(numbers[2]-numbers[1])-((numbers[2]-numbers[1])-(numbers[1]-numbers[0]))) ,3)))
        bot.sendMessage(from_id,'لحل سوال اخر اضغط /start')
        result=1
        numbers={}
        
    else:
        bot.sendMessage(from_id,'أعد المحاولة')
        result=1
        bot.sendMessage(from_id,'لتحديث بوت اضغط /start')
       	   
API_TOKEN = os.environ.get("API_TOKEN")

bot = telepot.Bot(API_TOKEN)
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)
