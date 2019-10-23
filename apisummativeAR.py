'''
myapi.py 
- simple program to demo using a web API with requests Python module
- secondary function to demo how to write out received data to an HTML file 
'''

import requests
import json
import pprint

# Find APIs at - https://apilist.fun/
# some will require an API key, boo hiss!

# cool geo example
# https://geo-info.co/?ref=apilist.fun
# example - https://geo-info.co/43.65,-79.40

# cool funny example
# https://funtranslations.com/api/chef
# https://api.funtranslations.com/translate/chef.json?text=I%20like%20upper%20canada%20college

# For any indentation errors, make sure there are no tabs (\t) by doing 
# a full replace of \t with 4 actual spaces

'''

def writeHTML(data):
    myfile = open("myapi.html","w")
    myfile.write("<h1>JSON file returned by API call</h1>")
    myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
    myfile.write(data)
    myfile.close()
'''
def writeHTML(data):
    myfile = open("playerAPI.html","w") # use "a" to "append"
    
    ############### CSS
    
    myfile.write("""
    <html>

    <style>
 
    	 padding-top: 60px;
		  background-color:aquamarine;
		  font-family: sans-serif;
		  align: center;
		 }
        h1,h2 {
		  color: black;
		  text-align: center;
          padding-left: 15px;
            padding-right: 15px;
		}
		
        h3,h4 {
            border:0px solid black;
            margin: 5px auto;
            padding: 10px;
            padding-left: 35px;
            padding-right: 35px;
            text-align: center;
            color: black
            
        }

    </style>


      <head>
        <title> MY PAGE </title>
      </head>

      <body>
 
        <h1> Welcome to My Financial Data Page </h1>
        <button type="button">Click Me!</button>
        <button type="button">Click Me!</button>

        <p>Go to <a href='https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line'>The Sports DB</a> for API Info.</p>

        <h1 style="background-color:DodgerBlue;">Here is graph of the dates you requested</h1>

        <p>Player name: """+ data+"""</p>

        <p style="font-family:verdana">This is a paragraph.</p>

        <p style="font-family:'Courier New'">This is another paragraph.</p>

      </body>

    </html>""")


    ################# CSS
    myfile.close()

def main():
    # use API to get place info
    response = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line")

    # if API call is correct
    if (response.status_code == 200):

        data = response.content # response comes in as byte data type
        data_as_str = data.decode()    # decode to str
        writeHTML(data_as_str)  # call function to write string data to HTML file

        # load as a JSON to access specific data more easily
        datajson = response.json()
        data = datajson['historical']
        
        for point in data:
            print(f"Date: {point['date']} \nClose: {point['close']}\n")
        
    else:
        data = "Error has occured"
        writeHTML(data)

main()