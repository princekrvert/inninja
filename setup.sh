#!/usr/bin/bash
# made by prince kumar 
# thanks subham bhaiya 
# date 22/10/2021
# install all the requirememt 
requirement(){
	apt update && apt upgrade
	apt-get install python 
	apt-get install python2
	apt-get install wget -y 
	apt-get install tor -y 
	apt-get install python3
	apt-get install python3-pip
	pip3 install requests --upgrade
	pip3 install requests[socks]
	pip3 install stem
	pip3 install instagram-py
	wget -O ~/instapy-config.json "https://git.io/v5DGy"
}
requirement

# make a banner for the this tool 
banner(){
    echo -e  "\e[32;1m"
    echo '
  _)               _)        _)        
  |  __ \   __ \   |  __ \   |   _` | 
  |  |   |  |   |  |  |   |  |  (   | 
 _| _|  _| _|  _| _| _|  _|  | \__,_| 
                         ___/         '
echo -e "\e[33;1m MADE BY PRINCE"
echo -e "\e[30;1m Babu bhaiya yee galat rasta hai👻"
}

# NOW TO EDIT THE TORCC FILE
os=$(uname -o)

if [ ${os} == "Android" ];then
	cd ~
	cd ..
	cd usr/etc/tor 
	sed -i '/ControlPort/s/^#//' torrc > /dev/null 2>&1
else
	cd ~
	cd ..
	cd etc/tor
	sed -i '/ControlPort/s/^#//' torrc > /dev/null 2>&1
fi
banner
#now uncomment the line 

