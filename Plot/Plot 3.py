# Get this figure: fig = py.get_figure("https://plot.ly/~sparky213/3/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~sparky213/3/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Plot 3", fileopt="extend")
# Get z data of first trace: z1 = py.get_figure("https://plot.ly/~sparky213/3/").get_data()[0]["z"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "z": ["14.05279633", "24.07420275", "5.444263238", "12.72083809", "23.09924898", "26.61196501", "11.30046436", "21.82454919", "26.62868635", "26.45641752", "14.62119421", "8.714041752", "27.93862067", "7.440629837", "21.62469689", "6.308703666", "11.33862424", "25.18076336", "25.95423574", "25.38014323", "24.94226998", "26.47716599", "5.957342668", "9.605635947", "25.1118626", "27.17603547", "11.90617831", "20.87723053", "27.19183147", "10.51368279", "21.87929669", "24.76149109", "26.35396997", "10.60337882", "28.08706696", "23.78759447", "20.07099013", "26.6869319", "24.35258559", "-5.036582188", "24.18911667", "26.77666361", "25.28040692", "27.12046628", "9.383473684", "6.675656823", "25.79264849", "24.73051884", "25.71448128", "24.46293199", "23.77366494", "25.61578443", "25.9521533", "11.43201375", "25.45765954", "27.37162576", "18.91282587", "7.736386456", "-17.98126527", "7.972721487", "28.81660253", "26.12904481", "25.59996081", "21.86997035", "22.74535387", "24.95268906", "24.92167781", "26.80265311", "4.990184827", "23.01235676", "7.958247454", "6.076773493", "6.763843177", "26.94435777", "25.03867178", "1.418817719", "12.88611864", "10.52051273", "25.73501176", "26.10709612", "4.983111111", "24.25472565", "27.54206129", "19.34404532", "8.269629328", "8.274791752", "26.71501308", "14.90015784", "-18.51531314", "26.75990224", "26.34821385", "26.99683434", "23.17349618", "11.04391599", "25.45589301", "26.76491501", "25.94827249", "26.34749924", "2.562114943", "24.75383359", "22.69405855", "9.810032077", "1.563264766", "23.99975712", "25.6927284", "17.6527831", "21.89285132", "9.557993381", "9.500551426", "19.76795825", "12.839139", "26.15106972", "11.97749949", "11.04391599", "19.49298523", "5.332643585", "24.10242823", "27.13303444", "26.73686535", "25.14230601", "3.296855906", "23.65273272", "5.474924134", "17.78782994", "13.72668179", "25.38127923", "22.39083299", "4.746958758", "6.046130855", "9.284889511", "22.4525331", "10.48845316", "22.76521272", "21.43108614", "25.83545041", "28.44535906", "18.60399542", "26.12904481", "27.62350541", "23.54082896", "26.35087403", "20.63037863", "9.060289206", "9.12165835", "-0.725644603", "10.31751527", "26.40170621", "17.7307169", "23.59619476", "20.4844952", "14.94036572", "9.634174134", "9.241696029", "22.70010819", "10.37123911", "26.00338677", "27.45626337", "26.74470831", "25.09487845", "2.209586768", "6.781834012", "26.99683434", "0.253856925", "21.45298912", "26.93416528", "20.66743919", "27.21637933", "23.13632933", "27.16345599", "26.29526127", "24.4508019", "23.28980789", "19.93597423", "26.44047249", "7.581949593", "14.79435845", "25.46825547", "26.82291446", "23.31811049", "8.872017821", "-5.395557026", "19.24442218", "26.62868635", "25.87042006", "26.66535642", "26.62868635", "4.466251399", "26.80771487", "26.33186249", "13.92720316", "25.79438617", "25.5688645", "27.97087097", "10.08544094", "26.74490553", "26.02609867", "26.5530532", "26.62868635", "7.625713849", "9.750869145", "26.62503699", "26.87708517", "17.27098292", "21.82392008", "1.401025102", "11.87413238", "13.72006365", "27.06731383", "27.09335943", "26.18912219", "-7.331602851", "18.83980726", "2.544753564", "7.093759165", "18.08056314", "21.96774108", "4.079850815", "22.34791097", "26.07481669", "25.96633272", "26.87580011", "23.23624785", "26.13641599", "20.08421436", "11.76430601", "14.88476324", "26.71998779", "23.03296871", "7.798253055", "27.72209632", "8.623923116", "8.789069246", "8.771299746", "17.20110707", "12.3823498", "25.04190122", "23.72147107", "26.35396997", "22.43193483", "26.25359673", "21.28295562", "21.11754725"], 
  "autocolorscale": False, 
  "colorscale": [
    [0, "rgb(37, 52, 148)"], [0.3, "rgb(8, 104, 172)"], [0.4, "rgb(44, 127, 184)"], [0.5, "rgb(65, 182, 196)"], [0.65, "rgb(161, 218, 180)"], [1, "rgb(255, 255, 204)], 
  "locationmode": "country names", 
  "locations": ["Afghanistan", "Africa", "Aland", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antigua And Barbuda", "Argentina", "Armenia", "Aruba", "Asia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Baker Island", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bonaire, Saint Eustatius And Saba", "Bosnia And Herzegovina", "Botswana", "Brazil", "British Virgin Islands", "Bulgaria", "Burkina Faso", "Burma", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Colombia", "Comoros", "Congo", "Congo (Democratic Republic Of The)", "Costa Rica", "Cote D'Ivoire", "Croatia", "Cuba", "CuraÃ§ao", "Cyprus", "Czech Republic", "Denmark", "Denmark (Europe)", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Europe", "Falkland Islands (Islas Malvinas)", "Faroe Islands", "Federated States Of Micronesia", "Fiji", "Finland", "France", "France (Europe)", "French Guiana", "French Polynesia", "French Southern And Antarctic Lands", "Gabon", "Gambia", "Gaza Strip", "Georgia", "Germany", "Ghana", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Heard Island And Mcdonald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Isle Of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kingman Reef", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Mali", "Malta", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands", "Netherlands (Europe)", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "North America", "North Korea", "Northern Mariana Islands", "Norway", "Oceania", "Oman", "Pakistan", "Palau", "Palestina", "Palmyra Atoll", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia", "Rwanda", "Saint Barthelemy", "Saint Kitts And Nevis", "Saint Lucia", "Saint Martin", "Saint Pierre And Miquelon", "Saint Vincent And The Grenadines", "Samoa", "San Marino", "Sao Tome And Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South America", "South Georgia And The South Sandwich Isla", "South Korea", "Spain", "Sri Lanka", "Sudan", "Suriname", "Svalbard And Jan Mayen", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor Leste", "Togo", "Tonga", "Trinidad And Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks And Caicas Islands", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United Kingdom (Europe)", "United States", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Virgin Islands", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"], 
  "locationssrc": "sparky213:2:45c0c0", 
  "name": "AverageTemperature ", 
  "reversescale": False, 
  "type": "choropleth", 
  "uid": "b5d108", 
  "zauto": True, 
  "zmax": 28.81660253, 
  "zmin": -18.51531314, 
  "zsrc": "sparky213:2:96e887"
}
data = Data([trace1])
layout = {
  "autosize": True, 
  "font": {"family": "Roboto"}, 
  "geo": {
    "coastlinecolor": "rgb(116, 115, 115)", 
    "countrycolor": "rgb(115, 113, 113)", 
    "projection": {
      "rotation": {
        "lat": 16.167716182, 
        "lon": 18.0118897962
      }, 
      "type": "orthographic"
    }, 
    "showcountries": True, 
    "showframe": True, 
    "showlakes": True, 
    "showland": False, 
    "showocean": False, 
    "showrivers": True
  }, 
  "hovermode": "closest", 
  "title": "Average Land Temperature in the globe (1850-2013)", 
  "titlefont": {"family": "Roboto"}
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)