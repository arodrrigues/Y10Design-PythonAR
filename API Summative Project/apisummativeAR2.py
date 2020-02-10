# Eli Preston
# Upper Canada College
# This program displays the stock closing prices of APPLE from 2014 to 2019 in a bar graph using Chart js.

import requests
import json
import pprint



def writeHTML(data, closingPrices, dates):
    myfile = open("SummativeAR.html","w")
    myfile.write("""
    
    <!DOCTYPE html>
    <html>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <head>
    
    <title>API Home Page</title>
    
    <link rel="stylesheet" href="style.css">
    <link rel='icon' href='favicon (1).ico' type='image/x-icon'/ >

    <p class="headingtext"> The below graph shows Apple closing prices from 1989 to present day.</p>
    
    """)


    bgColors = []
    for date in dates:
        if date[:4] == "2000":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2001":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2002":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2003":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2004":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2005":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2006":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2007":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2008":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2009":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2010":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2011":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2012":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2013":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2014":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2015":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2016":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2017":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2018":
            bgColors.append("'rgba(0, 255, 0, 1)'")
        elif date[:4] == "2019":
            bgColors.append("'rgba(0, 255, 0, 1)'")


    twothousand = []
    twothousandone = []
    twothousandtwo = []
    twothousandthree = []
    twothousandfour = []
    twothousandfive = []
    twothousandsix = []
    twothousandseven = []
    twothousandeight = []
    twothousandnine = []
    twothousandten = []
    twothousandeleven = []
    twothousandtwelve = []
    twothousandthirteen = []
    twothousandfourteen = []
    twothousandfifteen = []
    twothousandsixteen = []
    twothousandseventeen = []
    twothousandeighteen = []
    twothousandnineteen = []

    index = 0
    for yr in dates:
        if yr[:4] == "2000":
            print('2000')
            twothousand.append(closingPrices[index])
        elif yr[:4] == "2001":
            print('2001')
            twothousandone.append(closingPrices[index])
        elif yr[:4] == "2002":
            print('2002')
            twothousandtwo.append(closingPrices[index])
        elif yr[:4] == "2003":
            print('2003')
            twothousandthree.append(closingPrices[index])
        elif yr[:4] == "2004":
            print('2004')
            twothousandfour.append(closingPrices[index])
        elif yr[:4] == "2005":
            print('2005')
            twothousandfive.append(closingPrices[index])
        elif yr[:4] == "2006":
            print('2006')
            twothousandsix.append(closingPrices[index])
        elif yr[:4] == "2007":
            print('2007')
            twothousandseven.append(closingPrices[index])
        elif yr[:4] == "2008":
            print('2008')
            twothousandeight.append(closingPrices[index])
        elif yr[:4] == "2009":
            print('2009')
            twothousandnine.append(closingPrices[index])
        elif yr[:4] == "2010":
            print('2010')
            twothousandten.append(closingPrices[index])
        elif yr[:4] == "2011":
            print('2011')
            twothousandeleven.append(closingPrices[index])
        elif yr[:4] == "2012":
            print('2012')
            twothousandtwelve.append(closingPrices[index])
        elif yr[:4] == "2013":
            print('2013')
            twothousandthirteen.append(closingPrices[index])
        elif yr[:4] == "2014":
            print('2014')
            twothousandfourteen.append(closingPrices[index])
        elif yr[:4] == "2015":
            print('2015')
            twothousandfifteen.append(closingPrices[index])
        elif yr[:4] == "2016":
            print('2016')
            twothousandsixteen.append(closingPrices[index])
        elif yr[:4] == "2017":
            print('2017')
            twothousandseventeen.append(closingPrices[index])
        elif yr[:4] == "2018":
            print('2018')
            twothousandeighteen.append(closingPrices[index])
        elif yr[:4] == "2019":
            print('2019')
            twothousandnineteen.append(closingPrices[index])
        index += 1
    
    # print(twothousandone)
    # print(twothousandtwo)
    # print(twothousandthree)
    # print(twothousandfour)
    # print(twothousandfive)
    # print(twothousandsix)
    # print(twothousandseven)
    # print(twothousandeight)
    # print(twothousandnine)
    # print(twothousandten)
    # print(twothousandeleven)
    # print(twothousandtwelve)
    # print(twothousandthirteen)
    # print(twothousandfourteen)
    # print(twothousandfifteen)
    # print(twothousandsixteen)
    # print(twothousandseventeen)
    # print(twothousandeighteen)
    # print(twothousandnineteen)

    print(len(dates))
    print(len(closingPrices))
    print(len(bgColors))


    myfile.write("""

     <!DOCTYPE html>
    <html>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <head>
    
    <title>API Home Page</title>
    
    <link rel="stylesheet" href="../HTML/homestyle.css">
    <link rel='icon' href='favicon (1).ico' type='image/x-icon'/ >


        
        <canvas id="myChart" width="300" height="200"></canvas>
        <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
        <script>
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
        
            type: 'bar',
            data: {
                labels: """ + "".join(str(dates)) + """,
                datasets: [{
                    label: 'Closing Prices of Apple From 1989 (In $$$)',
                    
                    data: """ + "".join(str(closingPrices)) + """,
                    backgroundColor: [""" + ",".join(bgColors) + """],
                  
                    borderColor: [
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
            },
            options: {     
                layout: {
                    padding: {
                        left: 50,
                        right: 50,
                        top: 50,
                        bottom: 50
                    }
                }
            }
        });
        </script>
        </head>
        <body>
            

            
        </body>
    </html>
    """)
    myfile.close()



def main():
    response = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/AAPL?serietype=line")

    if (response.status_code == 200):
      
        data = response.content
        data_as_str = data.decode()
        datajson = response.json()
        
        dataSymbol = datajson['symbol']
        dataPoints = datajson['historical']
        # print(dataSymbol)



        closingPrices = []
        dates = []


        for point in dataPoints:
            # print(f"Date: {point['date']} \nClose: {point['close']}\n")
            closingPrices.append(point["close"])
            dates.append(point["date"])

            
        writeHTML(data_as_str, closingPrices, dates)

    else:
        data = "Error has occured"
        writeHTML(data, [], [])

main()