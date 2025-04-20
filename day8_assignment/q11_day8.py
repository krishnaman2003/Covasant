from flask import Flask, request, jsonify, make_response
import json, os, random

app = Flask(__name__)
@app.route("/w/<string:city>", methods=['GET'])
def get_weather(city):
    req_format = request.args.get("format", "json").lower()
    current_temp = random.randint(10, 90)
    condition_text = random.choice(["Clear", "Mostly Sunny", "Partly Cloudy", "Breezy", "Cloudy"])
    forecast_list = []
    for i in range(5):
        day_temp = random.randint(current_temp - 15, current_temp + 15)
        forecast_list.append({
            "code": str(random.randint(20, 35)),
            "date": f"{(20+i):02d} Apr 2025", 
            "day": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"][i % 7],
            "high": str(max(day_temp, current_temp + random.randint(-5, 10))),
            "low": str(min(day_temp, current_temp - random.randint(0, 10))),
            "text": random.choice(["Clear", "Mostly Sunny", "Partly Cloudy", "Breezy", "Cloudy"])
        })
    weather_data = {
        "query": {
            "count": 1,
            "created": "2025-04-20T13:00:00Z",
            "lang": "en-IN",
            "results": {
                "channel": {
                    "location": {
                        "city": city,
                        "country": "Unknown",
                        "region": " Unknown"
                    },
                    "item": {
                         "title": f"Conditions for {city}, Unknown",
                         "condition": {
                            "code": str(random.randint(20, 35)),
                            "date": "Sun, 20 Apr 2025 01:00 PM",
                            "temp": str(current_temp),
                            "text": condition_text
                         },
                         "forecast": forecast_list,
                         "description": f"<![CDATA[Random weather for {city}]]>"
                    }
                }
            }
        }
    }
    if req_format == "xml":
        xml_output = f"""<?xml version="1.0"?>
<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="{weather_data['query']['created']}" yahoo:lang="{weather_data['query']['lang']}">
<results>
<channel>
    <yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="{weather_data['query']['results']['channel']['location']['city']}" country="{weather_data['query']['results']['channel']['location']['country']}" region="{weather_data['query']['results']['channel']['location']['region']}"/>
    <item>
        <title>{weather_data['query']['results']['channel']['item']['title']}</title>
        <yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="{weather_data['query']['results']['channel']['item']['condition']['code']}" date="{weather_data['query']['results']['channel']['item']['condition']['date']}" temp="{weather_data['query']['results']['channel']['item']['condition']['temp']}" text="{weather_data['query']['results']['channel']['item']['condition']['text']}"/>"""

        for forecast in weather_data['query']['results']['channel']['item']['forecast']:
             xml_output += f"""
        <yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="{forecast['code']}" date="{forecast['date']}" day="{forecast['day']}" high="{forecast['high']}" low="{forecast['low']}" text="{forecast['text']}"/>"""

        xml_output += f"""
        <description>{weather_data['query']['results']['channel']['item']['description']}</description>
    </item>
</channel>
</results>
</query>"""
        response = make_response(xml_output)
        response.headers['Content-Type'] = 'application/xml;'
        return response
    else:
        return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)