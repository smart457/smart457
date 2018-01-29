import os, shlex, subprocess
import re
import string
import commands
import sys
import time
import ConfigParser
import smtplib

import traceback
import shutil
import simplejson
#!/usr/bin/python

istring = "ica/003275" 
with open("/Users/siva/Documents/test.json") as json_file:
    json_data = simplejson.load(json_file)


for x in xrange(1,20504):
     ourResult = json_data['items'][x]
     #print ourResult['item_unique']
     if  ourResult['item_unique'] == istring:
    	if (ourResult['metadata']['project'] or ourResult['metadata']['Project']):
    	   print true
    	if (not string1):
    	 string1 = ourResult['metadata']['Project']
    	string2= ourResult['metadata']['type']
    	
    	print string1[0]
    	print string2[0]
    	
projectmapping = {  "151" : "DASe\Ukraine\Chersonesos\Site151",
					"8"   : "DASe\Ukraine\Chersonesos\Site151",
					"Amastuola" : "skip",
					"Ancient City" : "Chersonesos: DASe\Ukraine\Chersonesos\AncientCity",
					"Apollonia Museum" : "skip",
					"Bezymyannaya (BEZ)" : "DASe\Ukraine\Chersonesos\BEZ",
					"Capo Alfiere" : "DASe\Italy\Croton\CA\field",
					"Capo Cimiti" : "DASe\Italy\Croton\CROTSUR\field",
					"Capo Colonna" : "DASe\Italy\Croton\CROTSUR\field",
					"Chora" : "Chersonesos: DASe\Ukraine\Chersonesos\Chora",
					"Croton" : "DASe\Italy\Croton\CROTSUR\field",
					"Fattoria Fabrizio (FF)" : "DASe\Italy\Metaponto\FF\field",
					"Fattoria Stefan (FTS)" : "DASe\Italy\Metaponto\FS\field",
					"Fondi" : "DASe\Ukraine\Chersonesos\Museum",
					"Fusco Necropolis" : "skip",
					"Herakleia" : "skip",
					"Herakleian Peninsula" : "skip",
					"Incoronata (IC)" : "DASe\Italy\Metaponto\IC\field",
					"Incoronata Greca (IC)" : "DASe\Italy\Metaponto\IC\field",
					"Incoronata Indigena (IC)" : "DASe\Italy\Metaponto\IC\field",
					"Kiev- Archaeological Institute" : "DASe\Ukraine\Kiev\ArchInstitute",
					"Kiev- Historical Museum" : "DASe\Ukraine\Kiev\HistoricalMuseum",
					"Kiev- Lavra/ Mus. of Historic Treasures" : "DASe\Ukraine\Kiev\Lavra",
					"Lago del Lupo" : "skip",
					"Metaponto" : "DASe\Italy\Metaponto\METAPONTO\field\people_places",
					"Montesaglicoso (MS)" : "DASe\Italy\Metaponto\METAPONTO\field\people_places",
					"Museum" : "DASe\Ukraine\Chersonesos\Museum",
					"National Preserve of Tauric Chersonesos (NPTC)" : "DASe\Ukraine\Chersonesos\Museum",
					"Pantanello" : "DASe\Italy\Metaponto\PZ\field ",
					"Pantanello (PZ)" : "DASe\Italy\Metaponto\PZ\field",
					"Pizzica" : "DASe\Italy\Metaponto\PZ\field",
					"Pizzica (1999)" : "DASe\Italy\Metaponto\PZ99\field",
					"Puglia" : "skip",
					"Saldone (SS)" : "DASe\Italy\Metaponto\SAL\field",
					"San Biagio (SB)" : "DASe\Italy\Metaponto\SAL\field",
					"San Giovanni" : "DASe\Italy\Croton\CROTSUR\field",
					"Sant'Angelo (SA)" : "DASe\Italy\Metaponto\SAV\field",
					"Sant'Angelo Grieco (SAG)" : "DASe\Italy\Metaponto\SAG\field",
					"Sant'Angelo Vecchio (SAV)" : "DASe\Italy\Metaponto\SAV\field",
					"Sevastopol" : "skip",
					"SHAP" : "DASe\Ukraine\Kiev\SHAP",
					"Site 132" : "DASe\Ukraine\Chersonesos\Chora",
					"Site 150 South" : "DASe\Ukraine\Chersonesos\Chora",
					"Site 151" : "DASe\Ukraine\Chersonesos\Site151",
					"Torre Bugiafro" : "DASe\Italy\Croton\CROTSUR\excavations\torre_bugiafro",
					"Torre Cannone" : "DASe\Italy\Croton\CROTSUR\field",
					"VA" : "DASe\Italy\Metaponto\SAV\field",
					}
print "Value : %s" %  projectmapping.get(string1[0])			

typemapping = { "Chart/Data Plot" : "field\charts\mounted_slides",
				"Map/Plan/Section" : "field\maps\mounted_slides",
				"Object" : "field\finds\mounted_slides",
				"People/Places Photo" : "field\people_places\mounted_slides",
				"Reconstruction" : "field\drawings\mounted_slides",
				"Site Photo" : "field\site\mounted_slides", 
				}
				
print "Value : %s" %  typemapping.get('People/Places Photo')					
    #for rs in ourResult:
#print rs['year']

