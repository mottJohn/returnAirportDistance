# returnAirportDistance
The program will take an excel input of airport code in IATA format, and return an excel with the distance.

## Concepts
The http link is in the following format:

https://www.world-airport-codes.com/distance/?a1={from_destination}&a2={to_destination}&code=IATA

The program sends a http request, and extract the distance from html by [xPath](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms256086(v=vs.100)). (It is just like a link to the HTML tag. You can easily check it on Google Inspector).

## Possible Problems
* 404 forbidden
It seems that the page rejects GET requests that do not identify a User-Agent. Check [this](https://stackoverflow.com/questions/38489386/python-requests-403-forbidden)

You can check out how to find the User-Agent below
![alt text](https://github.com/mottJohn/returnAirportDistance/blob/master/user_agent.JPG)

* SSL errors
Have a look on [this](https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror)