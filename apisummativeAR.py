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
def writeHTML(data, closingPrices, dates):
    myfile = open("playerAPI.html","w") # use "a" to "append"
    
    ############### CSS
    
    myfile.write("""
    <html>
	<link rel="stylesheet" href="style.css">



      <head>
        <title>API</title>




		<canvas id="myChart" width="300" height="200"></canvas>
		<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script

		<script>
		var ctx = document.getElementById('myChart').getContext('2d');
		var myChart = new Chart(ctx, {
		    type: 'bar',
		    data: {
		        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
		        datasets: [{
		            label: '# of Votes',
		            data: """ + "".join(str(closingPrices)) + """,
		            backgroundColor: [
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(54, 162, 235, 0.2)',
		                'rgba(255, 206, 86, 0.2)',
		                'rgba(75, 192, 192, 0.2)',
		                'rgba(153, 102, 255, 0.2)',
		                'rgba(255, 159, 64, 0.2)'
		            ],
		            borderColor: [
		                'rgba(255, 99, 132, 1)',
		                'rgba(54, 162, 235, 1)',
		                'rgba(255, 206, 86, 1)',
		                'rgba(75, 192, 192, 1)',
		                'rgba(153, 102, 255, 1)',
		                'rgba(255, 159, 64, 1)'
		            ],
		            borderWidth: 1
		        }]
		    },
		    options: {
		        scales: {
		            yAxes: [{
		                ticks: {
		                    beginAtZero: true
		                }
		            }]
		        }
		    }
		});
		</script>
      </head>

      <body>
 
        <h1> Welcome to My Financial Data Page </h1>

        <p>Go to <a href='https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line'>this API</a> for API Info.</p>

        <h1 style="background-color:DodgerBlue;">Here is the data you requested </h1>

        <p>Player name: """ + "".join(str(dates)) + """</p>
		<p>Player name: """ + "".join(str(closingPrices)) + """</p>

        <p style="font-family:verdana">This is a paragraph.</p>

        <p style="font-family:'Courier New'">This is another paragraph.</p>

      </body>

    </html>""")


    ################# CSS
    myfile.close()

def main():
	
	response = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line")
	
	if (response.status_code == 200):
		# data_as_str = response.decode()
		data = response.content
		data_as_str = data.decode()
		datajson = response.json()

		dataSymbol = datajson['symbol']
		dataPoints = datajson['historical']
		print(dataSymbol)



		dates = []
		closingPrices = []

		for point in dataPoints:
			print(f"Date: {point['date']} \nClose: {point['close']}\n")
			dates.append(point["date"])
			closingPrices.append(point["close"])

		writeHTML(data_as_str, dates, closingPrices)

	else:
		data = "Error has occured"
		writeHTML(data, [], [])

main()