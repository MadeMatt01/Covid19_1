from db_funcs import *

file = open("C:/Users/Yomade/Desktop/univelcity/notepad_sql2/time_series_covid19.csv")
file = open("C:/Users/Yomade/Desktop/univelcity/notepad_sql2/time_series_covid19_confirmed_global.csv")
file = open("C:/Users/Yomade/Desktop/univelcity/notepad_sql2/time_series_covid19_deaths_global.csv")
#print(file.readlines(1))

countries_of_choice = ["Italy", "Japan", "Jordan", "Nigeria", "Norway"]
heading = file.readlines(1)

for line in file.readlines(): 
    line_data = line.split(",")
    country_name = line_data[1]
    #print(country_name)

    for line2 in file.readlines():
        line_data2 = line2.split(",")
        if line_data2 in countries_of_choice:
            globally = line_data2[3:]

            for line3 in file.readlines():
                line_data3 = line3.split(",")
                death_rise = line_data3[4:]
                    
                if line_data3 in countries_of_choice:
                    Ddeath = death_toll(death_rise)



                    if Ddeath:
                        for data in list(zip(line_data, heading[0].split(",")))[4:]:
                            #print(format_time(data[1]), data[1])    
                            write_case(Ddeath[0]['ID'], format_time(data[1]), death_toll(data[1]), data[0] )

                    else:
                        write_country(Ddeath, line_data[2], line_data[3])
                   

                #print(line_data)
                
"""
                    if country_name in countries_of_choice:
                        country_exists = check_country(country_name)
                        # print(country_exists)

                        if country_exists:

                            for data in list(zip(line_data, heading[0].split(",")))[4:]:
                                #print(format_time(data[1]), data[1])
                                
                                write_case(country_exists[0]['ID'], format_time(data[1]), death_toll(data[1]), data[0] )

                        else:
                            write_country(country_name, line_data[2], line_data[3])

                    #if line_data[1] in countries_of_choice:
                        #print(line_data)

"""


"""
    Italy
    Japan
    Jordan
    Nigeria
    Norway
"""  