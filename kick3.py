# -*- coding: utf-8 -*-

import linepy
from linepy import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,requests,urllib

cl = linepy.LINE()
cl.login(token="EpxnbHU86dks7N4CPjqa.ZpVP6+0qe0d9iIzuk+Um/G.G/LRdsTfpgCcSWa71yfa5qYxIH4DYK7pPWCcfEMF/lQ=")
cl.loginResult()



print("login success")
reload(sys)
sys.setdefaultencoding('utf-8')

KAC=[cl]
mid = cl.getProfile().mid
Bots = [mid,"uf6c337b7dc57d24351b192caf612b812"]
bot1 = cl.getProfile().mid
superadmin = "uf6c337b7dc57d24351b192caf612b812"
admin = "uf6c337b7dc57d24351b192caf612b812"

wait = {
    'contact':False,
    'autoJoin':False,
    'autoAdd':True,
    'leaveRoom':False,
    'timeline':False,
    "lang":"JP",
	"protect":True,
	"blacklist":{},
    "clock":False,


}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']
blacklistFile='blacklist.txt'
pendinglistFile='pendinglist.txt'
mulai = time.time()


user1 = mid
user2 = ""

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d ชั่วโมง %02d นาที %02d วินาที' % (hours, mins, secs)

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            invitor = op.param2
            if invitor in [superadmin]:
                cl.acceptGroupInvitation(op.param1)

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \nปลดแบน @" + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Invited Success \n➡ " + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait2["ricoinvite"] = False
                                          break


            elif msg.text is None:
                return


#-----------------------------------------------
#                Admin
#-----------------------------------------------
            elif msg.text in ["Reject","ลบรัน"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ปฎิเสธเรียบร้อย")
                    else:
                        cl.sendText(msg.to,"ลองดู")

#--------------------------------------------------------------------------------------------		
#-----------------------------------------------
#                READ POINT
#-----------------------------------------------						
				
            elif msg.text.lower() == 'บอท':
                eltime = time.time() - mulai
                van = "ระยะเวลาการทำงานของบอท :\n"+waktu(eltime)
                cl.sendText(msg.to,van)
				
            elif msg.text in ["Speed","Sp"]:
                if msg.from_ in admin:
                    start = time.time()
                    cl.sendText(msg.to, "กำลังตรวจสอบความเร็ว...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))


#-----------------------------------------------------------


            elif msg.text in ["บ๊าย"]:
                if msg.from_ in admin: 
                    if msg.toType == 2:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)							
                        except:
                            pass

#------------------------------------------------------------------------------------

        if op.type == 55:
            print("[NOTIFIED_READ_MESSAGE]")
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n|| " + Nama
                        wait2['ROM'][op.param1][op.param2] = "|| " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        G = random.choice(KAC).getGroup(op.param1)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
            elif op.param2 not in admin + Bots:
                random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
            else:
                pass
        if op.type == 59:
            print(op)


    except Exception as error:
        print(error)


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
