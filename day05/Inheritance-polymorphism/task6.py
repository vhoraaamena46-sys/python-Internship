class Notification:
    def send(self):
        print("This is notification")
    
        
class EmailNotification(Notification):
    def send(self):
        print("This is Email Ntification")        
        
class SNSNotification(Notification):
    def send(self):
        print("This is SNS Ntification")        
             
c1=Notification()
c2=EmailNotification()
c3=SNSNotification()             

lst=[c1,c2,c3]

for i in lst:
    i.send()