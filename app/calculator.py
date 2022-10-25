import json
import requests
import holidays
import math
from workalendar.oceania import Australia
from datetime import date
from datetime import datetime
from unittest import *
import os
import csv
import calendar


class fakefile:
    def __init__(self,contents):
        self.contents= list(contents)
    def read(self):
        return self.contents





class  Charge_configruation():

    def __init__(self, power, baseprice):
        self.power=power
        self.baseprice=baseprice

configuration1 = Charge_configruation(2, 5)
configuration2 = Charge_configruation(3.6, 7.5)
configuration3 = Charge_configruation(7.2, 10)
configuration4 = Charge_configruation(11, 12.5)
configuration5 = Charge_configruation(22, 15)
configuration6 = Charge_configruation(36, 20)
configuration7 = Charge_configruation(90, 30)
configuration8 = Charge_configruation(350, 50)

class Calculator():
    # you can choose to initialise variables here, if needed.
    def __init__(self):
        self.time=0
        pass

    # you may add more parameters if needed, you may modify the formula also.
    def cost_calculation(self, initial_state, final_state, capacity, is_peak, is_holiday, charge_configruation):
        if is_peak:
            base_price = 100
        else:
            base_price = 200

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = (final_state - initial_state) / 100 * capacity * (charge_configruation.baseprice/base_price)*surcharge_factor
        return cost

    def cost_calculation_partially(self, initial_state, final_state, capacity, is_peak, is_holiday, charge_configruation, duration):
        if is_peak:
            base_price = 100
        else:
            base_price = 200

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        cost = (final_state - initial_state) / 100 * capacity * (charge_configruation.baseprice/base_price)*surcharge_factor*(duration/(self.time/60))
        return cost

    def cost_requirement2(self, time, initial_state, final_state, capacity, clock, date, charge_configruation,
                          post_code):
        charge_perminutes = ((final_state - initial_state) / 100 * capacity) / 100
        cost = 0
        energyList = [date, self.calculate_solar_energy_day(post_code, date)]

        if is_peak:
            base_price = 100
        else:
            base_price = 200

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1
        si = self.get_solar_insolation(postcode, start_date)
        dl = self.get_day_light_length(post_code, start_date)
        solar_cost = si * 1 / dl * 50 * 0.2

        cost = (final_state - initial_state) / 100 * capacity * (
                    charge_configruation.baseprice / base_price) * surcharge_factor - solar_cost

        cost = (final_state - initial_state) / 100 * capacity * (charge_configruation.baseprice/base_price)*surcharge_factor-solar_cost
        return cost

    def cost_requirement3(self, initial_state, final_state, capacity, is_peak, is_holiday, charge_configruation,
                          post_code, start_date,start_time, end_time):
        if is_peak:
            base_price = 100
        else:
            base_price = 200

        if is_holiday:
            surcharge_factor = 1.1
        else:
            surcharge_factor = 1

        hour = self.get_duration(start_time, end_time)
        si = self.get_solar_insolation(postcode, start_date)
        dl = self.get_day_light_length(post_code, start_date)
        cc = self.get_cloud_cover(postcode, start_date, hour)
        solar_cost = si * 1 / dl * (1-cc/100)*50 * 0.2

        cost = (final_state - initial_state) / 100 * capacity * (
                    charge_configruation.baseprice / base_price) * surcharge_factor - solar_cost
        return cost



    # you may add more parameters if needed, you may also modify the formula.
    def time_calculation(self, initial_state, final_state, capacity, charge_configruation):
        self.time = (final_state - initial_state) / 100 * capacity / charge_configruation.power * 60

        return self.time

    # you may create some new methods at your convenience, or modify these methods, or choose not to use them.
    #dd-mm-yyyy
    def is_holiday(self, start_date):

        date = start_date.split("-")
        day = int(date[0].zfill(2))
        month = int(date[1].zfill(2))
        year = int(date[2].zfill(2))

        calendar = Australia()

        #calendar.is_working_day(date('2012-2-19'))

        au_holidays=holidays.Australia()
        if (start_date in au_holidays):
            is_holiday=True
        else:
            is_holiday=False


        return is_holiday


    def is_peak(self, start_time):
        # meridian=start_time[-2:]
        # if meridian=='PM' and start_time[:2]!='12':
        #     start_time=str(12+int(start_time[:2]))+start_time[2:]
        #     start_time = start_time[:-2]

        # if meridian=='AM' and start_time[:2]=='12':
        #     start_time='00'+start_time[2:]
        #     start_time = start_time[:-2]

        period = self.get_period(start_time)
        period = period.split('-')
        start_time_hour = float(period[0])
        end_time_hour = float(period[1])
        if (start_time_hour>=6 and end_time_hour<=18):
            is_peak=True
        else:
            is_peak=False

        return is_peak

    def is_peak_partially(self,start_time):
        period = self.get_period(start_time)
        period = period.split('-')
        is_peak_partially=False
        start_time_hour = float(period[0])
        end_time_hour = float(period[1])
        if start_time_hour<6 and end_time_hour>6 and end_time_hour<=18:
            is_peak_partially=True
        if start_time_hour>=6 and start_time_hour<18 and end_time_hour>18:
            is_peak_partially=True

        return is_peak_partially


    def peak_point(self, start_time):
        period=self.get_period(start_time)
        period=period.split('-')
        start_time_hour=float(period[0])
        end_time_hour=float(period[1])
        peak_point=0
        if(start_time_hour<6 and end_time_hour>6):
            peak_point=6
        if(start_time_hour<18 and end_time_hour>18):
            peak_point=18
        return peak_point

    def get_duration(self,start_time_hour,end_time_hour):
        duration=float(end_time_hour)-float(start_time_hour)
        return duration


    #the whole charge period
    def get_period(self, start_time):
        start_time_hour=self.toHour(start_time)
        time_hour=self.time/60
        end_time_hour=start_time_hour+time_hour
        period=str(start_time_hour)+'-'+str(end_time_hour)
        return period

    def get_locationId(self,postcode):
        result = requests.get('http://118.138.246.158/api/v1/location?postcode=' + str(postcode))
        json_data=result.json()[0]
        locationId=json_data['id']
        return locationId

    def get_solar_energy_period(self,postcode,start_date):
        sunrise_hour = self.get_sunrise_hour(postcode, start_date)
        sunset_hour = self.get_sunset_hour(postcode, start_date)
        period = self.get_period(start_time)
        period = period.split('-')
        start_time_hour = float(period[0])
        end_time_hour = float(period[1])
        if (start_time_hour > sunset_hour):
            return 0
        elif (end_time_hour < sunrise_hour):
            return 0

        if (start_time_hour < sunrise_hour and end_time_hour > sunrise_hour):
            start_time_hour = sunrise_hour
        elif (end_time_hour > sunset_hour and start_time_hour < sunset_hour):
            end_time_hour = sunset_hour

        period = str(start_time_hour) + '-' + str(end_time_hour)
        return period


    # to be acquired through API
    def get_solar_energy_duration(self, postcode,start_date):
        period= self.get_solar_energy_period(postcode,start_date)
        period=period.split('-')
        get_solar_energy_star=float(period[0])
        get_solar_energy_end=float(period[1])

        list_duration = []
        start_point=math.floor(get_solar_energy_star)
        end_point=math.floor(get_solar_energy_end)
        duration=get_solar_energy_star-start_point
        list_pair=[start_point,duration]

        list_duration.append(list_pair)

        duration=get_solar_energy_end-end_point
        list_pair=[end_point,duration]
        list_duration.append(list_pair)

        for i in range(start_point,end_point-1):
            i=i+1
            list_pair=[i,1]
            list_duration.append(list_pair)

        return list_duration



    def toHour(self,time):
        time = time.split(":")
        hour = int(time[0].zfill(2))
        minute = int(time[1].zfill(2))
        time_hour=hour+minute/60
        return time_hour


    def get_sunrise_hour(self,postcode, start_date):
        locationId = self.get_locationId(postcode)
        json_data = requests.get("http://118.138.246.158/api/v1/weather?location=" + locationId + "&date=" + start_date).json()
        sunrise = json_data["sunrise"]
        sunrise_hour = self.toHour(sunrise)
        return sunrise_hour

    def get_sunset_hour(self,postcode, start_date):
        locationId = self.get_locationId(postcode)
        response = requests.get("http://118.138.246.158/api/v1/weather?location=" + locationId + "&date=" + start_date).json()
        sunset = response["sunset"]
        sunset_hour = self.toHour(sunset)
        return sunset_hour

    # to be acquired through API
    def get_day_light_length(self, postcode, start_date):
        sunset_hour=self.get_sunset_hour(postcode,start_date)
        sunrise_hour=self.get_sunrise_hour(postcode,start_date)
        dl=sunset_hour-sunrise_hour
        return dl

    # to be acquired through API
    def get_solar_insolation(self, postcode, start_date):
        locationId = self.get_locationId(postcode)
        json_data = requests.get("http://118.138.246.158/api/v1/weather?location=" + locationId + "&date=" + start_date).json()
        si = json_data['sunHours']
        return si

    # to be acquired through API
    def get_cloud_cover(self,postcode, start_date, hour):
        locationId = self.get_locationId(postcode)
        json_data = requests.get("http://118.138.246.158/api/v1/weather?location=" + locationId + "&date=" + start_date).json()
        array_hours=json_data['hourlyWeatherHistory']
        json_hour=array_hours[hour]
        cc=json_hour['cloudCoverPct']
        return cc

    def calculate_solar_energy(self, si, du, dl, cc):
        solarEnergy = si * du / dl * (1 - cc / 100) * 50 * 0.2
        return solarEnergy

    def calculate_solar_energy_day(self, location, date):
        solarEnergy = [0] * 24
        sunrise_hour, sunset_hour = self.get_day_light_length(location, date)
        cc = self.get_duration(postcode, date)
        si = self.get_solar_insolation(postcode, start_date)
        di = self.get_day_light_length(location, date)
        if not len(cc) == 24:
            raise ValueError(cc, "the length is wrong")
        for j in range(24):
            solarEnergy[j] += si * (1 / dl) * (1 - cc[i]) * 50 * 0.2

        return solarEnergy


    def date(self, date):
        if len(date)>8:
            raise ValueError("Date input was too big")
        date = datetime.strpt(date, '%Y-%m-%d')
        month = date.month
        current_date = datetime.now()

        date_list = []
        if date <= current_date:
            raise ValueError(" input date is wrong")
        year = current_date.year if\
            date.month<current_date.month or(date.month == current_date.month and date.day<= current_date.day)\
                else current_date.year-1
        for k in range(3):
            year = k
            day = min(calendar.monthrange(date.year-k, date.month)[k], date.day)
            date_list .append(datetime(year, month, day).strftime('%Y-%m-%d'))
        return date_list







start_time='5:00'
start_date='22-02-2021'
calculator = Calculator()
time=calculator.time_calculation(20,80,82,configuration5)
duration=time/60

is_peak=calculator.is_peak(start_time)
is_holiday=calculator.is_holiday(start_date)

is_peak_partially=calculator.is_peak_partially(start_time)
cost=0
if (is_peak_partially != True):
    cost=calculator.cost_calculation(20,80,82,is_peak,is_holiday,configuration5)
else:
    peak_point=calculator.peak_point(start_time)
    start_time_hour = calculator.toHour(start_time)
    if (peak_point==6):
        nonPeak_Duration=calculator.get_duration(start_time_hour,'6.0')
        nonPeak_cost=calculator.cost_calculation_partially(20,80,82,False,is_holiday,configuration5,nonPeak_Duration)

        peak_Duration=calculator.get_duration('6.0',start_time_hour+duration)
        peak_cost=calculator.cost_calculation_partially(20,80,82,True,is_holiday,configuration5,peak_Duration)
        cost=nonPeak_cost+peak_cost

print("time: "+str(time)+" min")
print("cost: $"+str(cost))
start_date='2021-02-22'
postcode='7250'

si=calculator.get_solar_insolation(postcode,start_date)
dl=calculator.get_day_light_length(postcode,start_date)

solarEnergy=0
list_duration=calculator.get_solar_energy_duration(postcode,start_date)
for i in list_duration:
    cc = calculator.get_cloud_cover(postcode, start_date, i[0])
    du = i[1]
    solarEnergy = calculator.calculate_solar_energy(si, du, dl, cc) + solarEnergy

print(solarEnergy)


