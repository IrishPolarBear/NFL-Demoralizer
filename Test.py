import socket
import urllib.request
import urllib.error

def main():
    #socket.SetDefaultTimeout(20)

   # url = 'http://www.google.com'
#
 #   response = urllib.request.urlopen(url)
  #  output = urllib.error.HTTPError
    
   # print (response)

    #print (output)
    #print ("Test")
    url = 'http://google.com/'
   # response = urllib.request.urlopen(url)
    #print (response)
    try :
        response = urllib.request.urlopen( url )
   #     print (response)
    except urllib.error.HTTPError as e:
        print ('the server couldn\'t fulfill the request. Reason:')
    except urllib.error.URLError as e:
        print ('We failed to reach a server. Reason:')
    else :
        html = response.read()
        print ('got response!')
      # do something, turn the light on/off or whatever
   
main()
    
