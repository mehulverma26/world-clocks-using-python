from tkinter import *
import tkinter as tk
from time import strftime 
import time
from datetime import datetime
import pytz
root = Tk()
root.title("World Clock")
zone='Asia/kolkata'
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
lbl = Label(mainframe, font = ('calibri', 40, 'bold'), 
            background = 'purple', 
            foreground = 'white')
lbl.grid(row = 1, column = 1)
def time():
    global lbl
    world=pytz.timezone(zone)
    datetime_India=datetime.now(world)
    timee=datetime_India.strftime("%H:%M:%S")
    sring = timee
    lbl.config(text=sring)
    lbl.after(1000, time)
time()
tkvar = StringVar(root)
choices = { 'India','ADDIS','Johannesburg','London','San Francisco'}
tkvar.set('<select>')
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Select a country").grid(row = 2, column = 1)
popupMenu.grid(row = 3, column =1)
def change_dropdown(*args):
    global zone
    if tkvar.get()=="India":
        zone='Asia/kolkata'
    elif tkvar.get()=="ADDIS":
        zone='Africa/Addis_Ababa'
    elif tkvar.get()=='Johannesburg':
        zone='Africa/Johannesburg'
    elif tkvar.get()=='Abidjan':
        zone="Africa/Abidjan"
    elif tkvar.get()=='Accra':
        zone="Africa/Accra"
    elif tkvar.get()=='Algiers':
        zone="Africa/Algiers"
    elif tkvar.get()=='Asmara':
        zone="Africa/Asmara"
    elif tkvar.get()=='Asmera':
        zone="Africa/Asmera"
    elif tkvar.get()=='Bamako':
        zone="Africa/Bamako"
    elif tkvar.get()=='Bangui':
        zone="Africa/Bangui"
    elif tkvar.get()=='Banjul':
        zone="Africa/Banjul"
    elif tkvar.get()=='Bissau':
        zone="Africa/Bissau"
    elif tkvar.get()=='Blantyre':
        zone="Africa/Blantyre"
    elif tkvar.get()=='Brazzaville':
        zone="Africa/Brazzaville"
    elif tkvar.get()=='Bujumbura':
        zone="Africa/Bujumbura"
    elif tkvar.get()=='Cairo':
        zone="Africa/Cairo"
    elif tkvar.get()=='Casablanca':
        zone="Africa/Casablanca"
    elif tkvar.get()=='Ceuta':
        zone="Africa/Ceuta"
    elif tkvar.get()=='Conakry':
        zone="Africa/Conakry"
    elif tkvar.get()=='Dakar':
        zone="Africa/Dakar"
    elif tkvar.get()=='Dar_es_Salaam':
        zone="Africa/Dar_es_Salaam"
    elif tkvar.get()=='Djibouti':
        zone="Africa/Djibouti"
    elif tkvar.get()=='Douala':
        zone="Africa/Douala"
    elif tkvar.get()=='El_Aaiun':
        zone="Africa/El_Aaiun"
    elif tkvar.get()=='Freetown':
        zone="Africa/Freetown"
    elif tkvar.get()=='Gaborone':
        zone="Africa/Gaborone"
    elif tkvar.get()=='Harare':
        zone="Africa/Harare"
    elif tkvar.get()=='Juba':
        zone="Africa/Juba"
    elif tkvar.get()=='Kampala':
        zone="Africa/Kampala"
    elif tkvar.get()=='Khartoum':
        zone="Africa/Khartoum"
    elif tkvar.get()=='Kigali':
        zone="Africa/Kigali"
    elif tkvar.get()=='Kinshasa':
        zone="Africa/Kinshasa"
    elif tkvar.get()=='Lagos':
        zone="Africa/Lagos"
    elif tkvar.get()=='Libreville':
        zone="Africa/Libreville"
    elif tkvar.get()=='Lome':
        zone="Africa/Lome"
    elif tkvar.get()=='Luanda':
        zone="Africa/Luanda"
    elif tkvar.get()=='Lubumbashi':
        zone="Africa/Lubumbashi"
    elif tkvar.get()=='Lusaka':
        zone="Africa/Lusaka"
    elif tkvar.get()=='Malabo':
        zone="Africa/Malabo"
    elif tkvar.get()=='Maputo':
        zone="Africa/Maputo"
    elif tkvar.get()=='Maseru':
        zone="Africa/Maseru"
    elif tkvar.get()=='Mogadishu':
        zone="Africa/Mogadishu"
    elif tkvar.get()=='Monrovia':
        zone="Africa/Monrovia"
    elif tkvar.get()=='Nairobi':
        zone="Africa/Nairobi"
    elif tkvar.get()=='Ndjamena':
        zone="Africa/Ndjamena"
    elif tkvar.get()=='Niamey':
        zone="Africa/Niamey"
    elif tkvar.get()=='Nouakchott':
        zone="Africa/Nouakchott"
    elif tkvar.get()=='Ouagadougou':
        zone="Africa/Ouagadougou"
    elif tkvar.get()=='Porto-Novo':
        zone="Africa/Porto-Novo"
    elif tkvar.get()=='Sao_Tome':
        zone="Africa/Sao_Tome"
    elif tkvar.get()=='Timbuktu':
        zone="Africa/Timbuktu"
    elif tkvar.get()=='Tripoli':
        zone="Africa/Tripoli"
    elif tkvar.get()=='Tunis':
        zone="Africa/Tunis"
    elif tkvar.get()=='Windhoek':
        zone="Africa/Windhoek"
    elif tkvar.get()=='Windhoek':
        zone="Africa/Windhoek"
    elif tkvar.get()=='Adak':
        zone="America/Adak"
    elif tkvar.get()=='Anchorage':
        zone="America/Anchorage"
    elif tkvar.get()=='Anguilla':
        zone="America/Anguilla"
    elif tkvar.get()=='Antigua':
        zone="America/Antigua"
    elif tkvar.get()=='Araguaina':
        zone="America/Araguaina"
    elif tkvar.get()=='Buenos_Aires':
        zone="America/Argentina/Buenos_Aires"
    elif tkvar.get()=='Catamarca':
        zone="America/Argentina/Catamarca"
    elif tkvar.get()=='ComodRivadavia':
        zone="America/Argentina/ComodRivadavia"
    elif tkvar.get()=='Cordoba':
        zone="America/Argentina/Cordoba"
    elif tkvar.get()=='Jujuy':
        zone="America/Argentina/Jujuy"
    elif tkvar.get()=='La_Rioja':
        zone="America/Argentina/La_Rioja"
    elif tkvar.get()=='Mendoza':
        zone="America/Argentina/Mendoza"
    elif tkvar.get()=='Rio_Gallegos':
        zone="America/Argentina/Rio_Gallegos"
    elif tkvar.get()=='Salta':
        zone="America/Argentina/Salta"
    elif tkvar.get()=='San_Juan':
        zone="America/Argentina/San_Juan"
    elif tkvar.get()=='San_Luis':
        zone="America/Argentina/San_Luis"
    elif tkvar.get()=='Tucuman':
        zone="America/Argentina/Tucuman"
    elif tkvar.get()=='Ushuaia':
        zone="America/Argentina/Ushuaia"
    elif tkvar.get()=='Aruba':
        zone="America/Aruba"
    elif tkvar.get()=='Asuncion':
        zone="America/Asuncion"
    elif tkvar.get()=='Atikokan':
        zone="America/Atikokan"
    elif tkvar.get()=='Atka':
        zone="America/Atka"
    elif tkvar.get()=='Bahia':
        zone="America/Bahia"
    elif tkvar.get()=='Bahia_Banderas':
        zone="America/Bahia_Banderas"
    elif tkvar.get()=='Barbados':
        zone="America/Barbados"
    elif tkvar.get()=='Belem':
        zone="America/Belem"
    elif tkvar.get()=='Belize':
        zone="America/Belize"
    elif tkvar.get()=='Blanc-Sablon':
        zone="America/Blanc-Sablon"
    elif tkvar.get()=='Boa_Vista':
        zone="America/Boa_Vista"
    elif tkvar.get()=='Bogota':
        zone="America/Bogota"
    elif tkvar.get()=='Boise':
        zone="America/Boise"
    elif tkvar.get()=='Buenos_Aires':
        zone="America/Buenos_Aires"
    elif tkvar.get()=='Cambridge_Bay':
        zone="America/Cambridge_Bay"
    elif tkvar.get()=='Campo_Grande':
        zone="America/Campo_Grande"
    elif tkvar.get()=='Cancun':
        zone="America/Cancun"
    elif tkvar.get()=='Caracas':
        zone="America/Caracas"
    elif tkvar.get()=='Catamarca':
        zone="America/Catamarca"
    elif tkvar.get()=='Cayenne':
        zone="America/Cayenne"
    elif tkvar.get()=='Cayman':
        zone="America/Cayman"
    elif tkvar.get()=='Chicago':
        zone="America/Chicago"
    elif tkvar.get()=='Chihuahua':
        zone="America/Chihuahua"
    elif tkvar.get()=='Coral_Harbour':
        zone="America/Coral_Harbour"
    elif tkvar.get()=='Cordoba':
        zone="America/Cordoba"
    elif tkvar.get()=='Costa_Rica':
        zone="America/Costa_Rica"
    elif tkvar.get()=='Creston':
        zone="America/Creston"
    elif tkvar.get()=='Cuiaba':
        zone="America/Cuiaba"
    elif tkvar.get()=='Curacao':
        zone="America/Curacao"
    elif tkvar.get()=='Danmarkshavn':
        zone="America/Danmarkshavn"
    elif tkvar.get()=='Dawson':
        zone="America/Dawson"
    elif tkvar.get()=='Dawson_Creek':
        zone="America/Dawson_Creek"
    elif tkvar.get()=='Denver':
        zone="America/Denver"
    elif tkvar.get()=='Detroit':
        zone="America/Detroit"
    elif tkvar.get()=='Dominica':
        zone="America/Dominica"
    elif tkvar.get()=='Edmonton':
        zone="America/Edmonton"
    elif tkvar.get()=='Eirunepe':
        zone="America/Eirunepe"
    elif tkvar.get()=='El_Salvador':
        zone="America/El_Salvador"
    elif tkvar.get()=='Ensenada':
        zone="America/Ensenada"
    else: pass
tkvar.trace('w', change_dropdown)
root.mainloop()