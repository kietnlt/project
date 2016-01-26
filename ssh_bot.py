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
    
def check_hosts():
    for host,result in execute(run_command,"uptime",hosts=env.hosts).iteritems():
        running_hosts[host] = result if result.succeeded else "Host down"
        
def get_hosts():
    selected_hosts = []
    for host in raw_input("Hosts:").split():
        selected_hosts.append(env.hosts[int(host)])
    return selected_hosts
    
def menu():
    for num,desc in enumerate(["List Host","Run Command","Open Shell","Exit"]):
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
            result = execute(run_command,cmd,hosts=execute(get_hosts));
            print result

        elif choice==2:
            host = int(raw_input("Host:"))
            execute(open_shell,hosts=env.hosts[host])
        for num,desc in enumerate(["List host","run command","open shell","exit"]):
            print "[" + str(num) + "]" + desc
        choice = int(raw_input('\n' + PROMPT))
        

if __name__ == "__main__":
    menu()
    
        
    
