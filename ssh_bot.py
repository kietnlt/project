from fabric.api import *

PROMPT = '>'
for line in open("creds.txt","r").readlines():
    host,passw = line.split()
    env.hosts.append(host)
    env.passwords[host] = passw
    
def run_command(command):
    try:
        with hide('running','stdout','stderr'):
            if command.strip()[0:5] == "sudo":
                results = sudo(command)
            else:
                results = run(command)
    except:
        results = 'Error'
    return results
        
def get_hosts():
    host = int(raw_input("Host:"))
    return host
    
def menu():
    for num,desc in enumerate(["List Host","Run Command","Check Host","Exit"]):
        print "[" + str(num) + "]" + desc
    choice = int(raw_input('\n' + PROMPT))
    
    while(choice!=3):
        '''list_hosts()'''
        if choice ==0:
            print "List avaiable host"
            num=0
            for host in env.hosts:
                temp =  host[host.find("@",0)+1:]
                print "[" + str(num) + "]" + temp[:temp.find(":",0)]
                num = num+1
                
               
        elif choice ==1:
            cmd = raw_input("Command:")
            result = execute(run_command,cmd,hosts=env.hosts)
            for host in env.hosts:
                print host,"||",
                print result[host]
        

        elif choice==2:
            result =  execute(run_command,"uptime",hosts=env.hosts)
            for host in env.hosts:
                print host, "||",
                print result[host]
                
         
        
        
        print '-'*80
        for num,desc in enumerate(["List host","run command","Check Host","exit"]):
            print "[" + str(num) + "]" + desc
        choice = int(raw_input('\n' + PROMPT))
        print '-'*80
        

if __name__ == "__main__":
    menu()
    print '*'*80
    
        
    
