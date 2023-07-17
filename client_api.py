import requests

#Version: 1.0

###SETUP###
#Import API: "import assets.APIs.client_api as ca"
#Use "response = ca.check_database_api(server_ipaddress,server_port,server_subdomain,email,password)"
#Ment to be used with Remote Account Database


def check_database_api(server_ipaddress,server_port,server_subdomain, email, password):
    #Sets up URL
    url = (str('http://')+str(server_ipaddress)+str(':')+str(server_port)+str('/')+str(server_subdomain))

    #Sets up Data
    data = {'email': email,'password': password}

    #Sends request to the Remote Account Database Server
    request = requests.post(url, data=data)

    #Returns response
    #If correct signin, sends AUTH Code
    #If failed signin, sends failed code
    return request.text
