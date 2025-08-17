def fine_calculator(area,speed):
    area_types=['urban','motorway','expressway']
    if not isinstance(area,str): return 'Invalid Area Type'
    elif area not in area_types: return 'Invalid Area Value'

    if not isinstance(speed,float) and not isinstance(speed,int): return 'Invalid Speed Type'
    speed=float(speed)
    if speed<=0: return 'Invalid Speed Value'
    if area=='urban' and speed<=50:
        return 0
    elif area=='expressway' and speed<=100:
        return 0
    elif area=='motorway' and speed<=120:
        return 0
    elif area=='urban' and speed >50:
        return round(1.0*(100*(speed-50)/50)**2.0)
    elif area=='motorway' and speed >120:
        return round(0.5*(100*(speed-120)/120)**2.0)
    elif area=='expressway' and speed >100:
        return round(0.8*(100*(speed-100)/100)**2.0)

print(fine_calculator('motorway',180))
print(fine_calculator('urban',60))
print(fine_calculator('expressway',120))
# print(fine_calculator('motorway',0j))

# #i test che implemento devono iniziare tutti con la parola test all'inizio
# print(fine_calculator('expressway',99))
# print(fine_calculator('urban',40))
# print(fine_calculator('motorway',110))


# print(fine_calculator('motorway','c'))
# print(fine_calculator('motorway',[50]))
        
# print(fine_calculator('motorway',0j))
        
# print(fine_calculator('motorway',{50}))
        
# print(fine_calculator('motorway',(50,)))
        
# print(fine_calculator('motorway',''))
       
    
# print(fine_calculator('motorway',-2))
        
# print(fine_calculator('motorway',0))
       

# print(fine_calculator(2,80))

# print(fine_calculator(['area'],50))

# print(fine_calculator(0j,50))
        
# print(fine_calculator({'area'},50))
        
# print(fine_calculator(('area',),50))
        
# print(fine_calculator(5.8,50))
       

# print(fine_calculator('cacca',50))       
# print(fine_calculator('Urban',50))       
# print(fine_calculator('Motorway',50))       
# print(fine_calculator('Expressway',50))     
# print(fine_calculator('',50)) 

      
