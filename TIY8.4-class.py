#TIY8.4
'''
#8-9 Messages - list of short messages - pass list to function called show_messages
def show_messages(messagelist):
    for message in messagelist:
        print(message)

#===================================#
#      program below this line      #
#===================================#
messagelist = ["cool thanks", "and then just go over the code", "free for a call whenever you are", "have a good one","we will figure something out"]
show_messages(messagelist)
'''

'''
#8-10
#show_messages
def send_messages(messagelist):
    print(messagelist)
    sent_messages = []
    for message in messagelist:
        currentmessage = messagelist.pop()
        print(currentmessage)
        sent_messages.append(currentmessage)
    return sent_messages

#===================================#
#      program below this line      #
#===================================#
messagelist = ["cool thanks", "and then just go over the code", "free for a call whenever you are", "have a good one","we will figure something out"]
tempvar = send_messages(messagelist)
print("messages sent")
print("send messages list:")
print(messagelist)
print("sent messages list:")
#print(type(tempvar))
print(tempvar)
'''

#8-11 Archived messages - modify 8.10 to not wipe the passed list.

def send_messages(messagelist):
    print(messagelist)
    sent_messages = []
    for message in messagelist:
        print(message)
        sent_messages.append(message)
    return sent_messages

#===================================#
#      program below this line      #
#===================================#
messagelist = ["cool thanks", "and then just go over the code", "free for a call whenever you are", "have a good one","we will figure something out"]
tempvar = send_messages(messagelist)
print("messages sent")
print("send messages list:")
print(messagelist)
print("sent messages list:")
#print(type(tempvar))
print(tempvar)
