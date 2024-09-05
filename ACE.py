Ntoken='6316657310:AAHl3CgzoppCiYMKVE2h75j358zZ4HyOsk4'

chat_id= 5489161720

#message='hello'

#chat_url='https://api.telegram.org/bot6316657310:AAHl3CgzoppCiYMKVE2h75j358zZ4HyOsk4/sendMessage?chat_id=5489161720&text=welcome


import requests

#upurl='https://api.telegram.org/bot6316657310:AAHl3CgzoppCiYMKVE2h75j358zZ4HyOsk4/getUpdates'

#chat_url = ''

url = 'https://api.telegram.org/bot6316657310:AAHl3CgzoppCiYMKVE2h75j358zZ4HyOsk4/'


def get_updates(url):

  resp = requests.get(url+'getUpdates?').json()
  return resp['result']

data = get_updates(url)

#def get_message(data):
 

message = data[-1]['message']['text'].lower()

chat_id = data[-1]['message']['from']['id']


name= data[-1]['message']['from']['first_name']

#f_name=data[-1]['message']['from']['last_name']

#message = data[-1]['message']['text']['first_name'].lower()
#print(name)

def send_message(chat_id, message):

    if message in ['hii','hi','hii','helo','hey','hello','excuse me','hlo']:
     reply = 'Hi "'+name+'", how can i help you?\n'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in['help','i need help','i dont know how to use','help me','can you help me','i want some help']:
     reply = 'Please,explain your problem.I will give the solution'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in['how many types of crops are available','what are the types of crops you know','list of crops','how many type of crops are available','types of crops','types of crop']:
     reply ='1.Cereal Crops(Wheat,Rice,Maize,Corn,Barley,Oats,Rye)\n2.Pulse Crops(Chick peas,beans).\n3.Oil seed crops(soyabeans,sunflower,canola,cotton seed,flaxseed)\4.Root and tuber crops(Potatoes,sweet potatoes,carrots)\n5. Fruit crops(Apples,mangoes,oranges etc).\n6.Vegetable crops(Tomatoes,Broccoli,cucumbers\n7.Industrial crops(Tobacco,rubber,jute)\n8.Fiber crops(cotton,hemp,flax)\n 9. Medicinal and Aromatic crops(Lavender,mint)\n10. Spice crops(Black pepper,cardamom,cloves,turmeric\n11. Beverage crops(Coffee,Tea,Cocoa)\n12. Nuts(Almonds,Walnut,cashew nuts)\n13. Forage crops(Alfalfa,Clover)\n14. Cover crops(Pye,Buck Wheat)\n15.Catch crops(Radish,Turnip)\n16. Aquatic crops(Water spanich).\n17. Flower(Rose,Lavender).\n18. Herbs(Basil,Rosemary).\n19. Gourds(Pumpkins).\n20.Suger corps(Sugar beets).\n'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['ya sure','sure','ya']:
     reply  = 'tell me!'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['what can you do','what you can do','what you do','use','is there any use','what is the use','whats the use']:
     reply = 'I will give the basic aid/solution to your problem'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['Problem solved,thank you','Ok','Problme cleared','No doubt','Thank you','Thank you very much','Thanks']:
     reply = 'Your welcome !'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['why should i trust','why should i trust you','should i trust you']:
     reply = 'It depends on yourself ,it is just a bot that provides the  accurate solution to your problem'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['is the information correct','is information true']:
     reply= 'this information is bought from the expert sites\n you can trust or can check in google'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['Which tractor is best and most powerful','good tractor','best tractor','powerful tractor','Good tractor']:
     reply = 'There is a vast list of the best and most powerful tractors, including the John Deere 6120 B 4WD, Preet 10049,4WD,and others.\n still there are several other good like in Mahindra company'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['ok bye','bye','see you','good bye','tata','byee','see you bye']:
     reply = 'thank you for visiting us ! Hope it is helpful '
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['good morning']:
     reply= 'good morning!'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['good afternoon']:
     reply= 'good afternoon!'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['good night']:
     reply = 'good night!'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['who created this bot','created by','who develpoed this','who did this','who created you?','who created you']:
     reply= 'This chat bot is created by team ACE of MLR institute of technology .\n'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['ok','kk','okk','Okay','Ok','OK','okay','OKAY']:
     reply = 'Yeah ! '
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['why it is used','why should we use ','what us its use','why should we use you','why should we use you?']:
     reply = 'Instead of  searching in google we made it easy to you to get the basic solution for your problem'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['how are you','hw r u','how are you doing','How are you']:
     reply = 'As I am bot I will always be fine👍, What about you?'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['i am fine','fine','good','doing well','Iam fine','Doing well','well and good','iam fine']:
     reply = 'Thats good!'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['what does it give','what it give','Use of this bot']:
     reply = 'This is  a bot that will give you the information about the solution related to agriculture and farming'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in ['How many different types of farming methods are there in India?','Types of farming?','types of farming','farming methods','Farming methods']:
     reply='Organic farming, subsistence farming, commercial farming are popular farming methods used in India. \n However, depending on geographical conditions, production demand, level of technology and labour, farming can be based on ley farming, horticulture, agroforestry, etc.'
     response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
     return response
    
    elif message in['What are the types of agricultural practices','Types of agriculture practices','List of agriculture practices']:
      reply = ' Mixed farming, shifting agriculture, intensive farming, crop rotation, plantation agriculture, arable farming are few popular types of agriculture practices.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['How many crop seasons are there in India','crop seasons in India','Crop seasons']:
      reply = 'There are three season crops such as: \n 1) Zaid\n 2) Rabi\n 3) Kharif .'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What is the Kharif season and examples','Kharif season','Kharif season and examples','kharif season']:
      reply = 'The Kharif season in India starts in June and ends in October.\n Example:Rice,maize etc'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What is the Rabi season and examples','Rabi season','Rabi seasons and examples','rabi season']:
      reply = 'Rabi crops are grown in winter between October to November.\n Barley, Oats, Wheat, Pulses are few examples of Rabi crops.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What is the Zaid season and examples','Zaid season','Zaid seasons and examples','zaid season']:
      reply = 'They are summer season crops, grown for short periods between March to June.\n Example:Water melon etc'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in[' why maintaining healthy soil is important?','importance of healthy soil','maintainance of healthy soil?']:
      reply = ' A healthy soil is important as it provides essential nutrients, oxygen, water, and root support to crop producing plants. '
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['what are pesticides and ferilizers','pesticides and fertilizers']:
      reply = 'Pesticides are chemical substances or mixtures that are used to control, repel, or eliminate pests that can damage crops and reduce yields.\n Fertilizers are substances added to soil or plants to provide essential nutrients that support plant growth and development\n'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What are organic pesticides','About organic pesticides','Organic pesticides']:
      reply = ' Organic pesticides are derived from botanical and mineral sources. They contain less chemicals and are less threatening than chemical-based pesticides.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What are the government initiatives in the agriculture sector?','Government schemes','government schemes for agriculture','government schemes']:
      reply = '1)Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)\n 2) Soil Health Card Scheme\n 3) Pradhan Mantri Fasal Bima Yojana (PMFBY)\n 4) Rashtriya Krishi Vikas Yojana (RKVY)\n 5) Kisan Credit Card (KCC) Scheme\n 6) National Mission for Sustainable Agriculture (NMSA)\n 7) Paramparagat Krishi Vikas Yojana (PKVY)\n 8) Pradhan Mantri Kisan Sampada Yojana (PMKSY)\n These are just a few examples of the various government schemes on farming in India.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Which crops are grown in the rainy season?','list of crops grown in rainy season','Rainy season crops']:
      reply = 'Kharif crops, also known as monsoon crops are grow in the rainy season such as Rice, Maize, Sorghum, Bajra, Soybean, Cotton, and others.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What is the lifespan of coconut trees?','Lifespan of coconut trees']:
      reply = ' Coconut trees can survive up to 60-80 years, providing a yield to almost three generations of farmers.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What are the basic needs for farming?','needs of farming','Needs of farming']:
      reply = 'Natural resources like air, nutrients, land, water, and sunlight are essential for farming.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What is Ploughing?','Ploughing?']:
      reply = 'Ploughing is the process of tossing the uppersoil to bring fresh nutrients to the surface. The process also helps bury crops remains and weed.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What is threshing?','Threshing']:
      reply = 'Threshing is the process of separating edible part of grains from chaff or straw.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in[' Which are the best tractors under 5 lakh rupees in India?','Tractors under five lakhs?','Tractors under 5 lakhs?']:
      reply = ' Mahindra 265 DI, Sonalika DI 734 (S1) and  Force ORCHARD DELUXE are the top-class tractors under 5 lakh rupees in India.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Which soil is most suitable for agriculture?','Soil for agriculture?']:
      reply = 'Different soil types are found with unique physical, chemical and biological aspects. For example, alluvial soil is believed to be the most fertile soil with potassium and is appropriate for crops like sugarcane, paddy and others.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Which food does India export the most?','mostly exported food?']:
      reply = 'Rice is the most exported agricultural product from India.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of corn','Growing of corn ?','information about corn ?','corn','Corn']:
      reply = ' Soil: Well-drained loamy or sandy soil.\n - Weather: Prefers warm temperatures between 60-95°F (15-35°C) and a frost-free growing season of 60-100 days.\n- Water: Requires regular watering, around 1-1.5 inches per week. - Harvesting: Typically harvested 70-90 days after planting when the ears are fully developed and the husks have dried.\n Pesticides: Common pesticides used for corn include herbicides to control weeds like atrazine and glyphosate, insecticides like neonicotinoids for pests such as corn rootworms and corn borers, and fungicides to manage diseases like gray leaf spot and rust.\n  Fertilizers: Nitrogen-based fertilizers are commonly used for corn, such as ammonium nitrate or urea. Phosphorus and potassium fertilizers are also essential, typically applied before planting or as a side dressing during the growing season.\n - Season: Corn is primarily a summer crop, and the sowing season varies depending on the region. In many parts of India, corn is sown during the monsoon season, between June and July.\n For brief information please type (Briefly about growth of corn)'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of wheat','Growing of Wheat ?','information about wheat ?','wheat','Wheat']:
      reply = ' Wheat: \n - Soil: Well-drained loamy soil with a pH range of 6.0-7.5.\n - Weather: Grows best in cool temperatures between 50-70°F (10-20°C) during the growing season.\n - Water: Moderate water requirements, around 1 inch per week. Additional irrigation may be necessary in dry conditions.\n - Harvesting: Harvested when the crop reaches maturity and the grains have dried, typically around 110-130 days after planting.\n - Pesticides: For wheat, herbicides are commonly used to control weeds, such as glyphosate or 2,4-D. Insecticides may be used to manage pests like aphids or Hessian flies, and fungicides to control diseases like powdery mildew or Fusarium head blight.\n - Fertilizers: Nitrogen-based fertilizers, such as ammonium nitrate or urea, are commonly used for wheat. Phosphorus and potassium fertilizers are also applied based on soil test results and crop nutrient requirements.\n - Season: Wheat is a winter season crop in most parts of India. The sowing season for wheat begins around November and December, depending on the region and local climatic conditions.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of rice','Growing of rice ?','information about rice ?','rice','Rice']:
      reply = ' Rice:\n - Soil: Requires clayey or loamy soil with good water retention capacity.\n - Weather: Thrives in tropical and subtropical regions with high temperatures (70-100°F or 20-38°C) and high humidity.\n- Water: Rice is a water-intensive crop and requires flooding during the growing season. Generally, it needs an inch or more of water per week.\n- Harvesting: Timing depends on the variety, but typically takes place around 100-150 days after planting. Harvesting involves cutting the stalks and drying the rice grains.\n - Pesticides: In rice cultivation, herbicides are crucial for weed control, with commonly used ones including pre-emergent herbicides like pendimethalin and post-emergent herbicides like 2,4-D.\n Insecticides may be used to manage pests like rice stem borers or rice planthoppers, and fungicides to control diseases like blast or sheath blight.\n - Fertilizers: Nitrogen fertilizers are important for rice production, typically applied in split doses throughout the growing season. Phosphorus and potassium fertilizers are also used based on soil fertility levels.\n - Season: Rice is predominantly a kharif (monsoon) crop in India. The sowing season for rice starts with the onset of the monsoon rains, typically between June and July.\n For Brief inormation please type (Briefly about growth of rice)'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of soybeans','Growing of soybeans ?','information about soybean ?','soybean','Soybean']:
      reply = ' Soybeans:\n- Soil: Well-drained loamy soil with a pH range of 6.0-7.5.\n - Weather: Grows well in warm temperatures between 68-86°F (20-30°C) and requires a frost-free period of 100-150 days.\n - Water: Moderate water requirements, around 1 inch per week. Soybeans have relatively good drought tolerance.\n - Harvesting: Typically harvested when the pods have turned brown and the seeds inside have reached maturity, which is around 100-150 days after planting.\n - Pesticides: Herbicides are commonly used in soybean farming to control weeds, with popular options including glyphosate, dicamba, or glufosinate. Insecticides may be used to manage pests like soybean aphids or bean leaf beetles, and fungicides for diseases like soybean rust or white mold.\n - Fertilizers: Soybeans can fix nitrogen from the atmosphere through a symbiotic relationship with nitrogen-fixing bacteria. However, phosphorus and potassium fertilizers may still be required based on soil test results and crop nutrient needs.\n - Season: Soybeans are typically sown during the kharif season. The ideal sowing time for soybeans is around June and July, coinciding with the monsoon season.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of tomatoes','Growing of tomatoes ?','information about tomatoes ?','tomato','Tomato']:
      reply = 'Tomatoes:\n - Soil: Well-drained, fertile soil with organic matter. pH range of 6.0-7.0 is ideal.\n - Weather: Prefers warm temperatures between 70-85°F (21-29°C) and a frost-free growing season of 60-90 days.\n - Water: Regular watering is essential, aiming for 1-2 inches per week. Avoid overwatering to prevent disease.\n - Harvesting: Varies based on the variety, but generally tomatoes are ready to be harvested 60-80 days after transplanting. Harvest when the fruits have reached desired ripeness and color.\n - Pesticides: Herbicides are generally not recommended for tomatoes due to their sensitivity, but hand weeding or mulching can help control weeds. Insecticides may be used to manage pests like aphids, tomato hornworms, or whiteflies. Fungicides can be employed for diseases such as early blight or powdery mildew.\n - Fertilizers: Tomatoes require balanced fertilization, typically using a complete fertilizer such as a 10-10-10 or 14-14-14 formulation. Additional calcium may be applied to prevent blossom-end rot, a common disorder in tomatoes.- Season: Tomatoes can be grown in different seasons based on the cultivation method. In many regions, tomatoes are grown as summer crops, with the sowing season starting around February or March. However, with controlled greenhouse cultivation, tomatoes can be grown throughout the year.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of potatoes','Growing of potatoes ?','information about potatoes ?','potato','Potato']:
      reply = 'Potatoes:\n - Soil: Well-drained sandy or loamy soil with a pH range of 5.0-6.0.\n - Weather: Prefers cool temperatures between 60-70°F (15-21°C) during the growing season and a frost-free period of 90-120 days.\n  - Water: Requires consistent soil moisture, about 1-2 inches of water per week. Avoid overwatering to prevent diseases.\n - Harvesting: Harvested when the foliage has died back, usually around 90-120 days after planting. Dig up the tubers carefully to avoid damage.\n  - Pesticides: Herbicides like metribuzin or linuron may be used for weed control in potatoes. Insecticides can help manage pests such as Colorado potato beetles or aphids. Fungicides are used to control diseases like late blight or early blight.\n - Fertilizers: Potatoes have specific nutrient requirements, including nitrogen, phosphorus, and potassium. Balanced fertilizers like a 10-10-10 or 14-14-14 formulation are commonly used. Additional applications of potassium and calcium may be necessary.\n  - Season: Potatoes are generally grown as a winter season crop in many parts of India. The sowing season for potatoes typically begins in October or November, depending on the region and local climate.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of carrots','Growing of carrots ?','information about carrots ?','carrot','Carrot']:
      reply = 'Carrots:\n - Soil: Loose, well-drained sandy or loamy soil with a pH range of 6.0-6.8.\n - Weather: Grows best in cool temperatures between 60-75°F (15-24°C). Carrots can tolerate light frosts.\n - Water: Requires consistent moisture, especially during the germination period. Aim for 1 inch of water per week.\n - Harvesting: Depending on the variety, carrots can be harvested 60-80 days after sowing. Harvest when the roots have reached the desired size and color.\n  - Pesticides: For weed control in carrots, herbicides like linuron or pendimethalin can be used. Insecticides may be applied to manage pests such as carrot rust flies or aphids. Fungicides are utilized to control diseases like cavity spot or leaf blight.\n - Fertilizers: Carrots benefit from well-balanced fertilizers, typically with a higher phosphorus content for root development. A fertilizer formulation like 10-20-20 is commonly used, and soil amendments like compost or well-rotted manure can improve soil fertility.\n  - Season: Carrots are predominantly grown as a cool-season crop in India. The ideal sowing time for carrots is during the winter months, starting from October to December.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of apples','Growing of apples ?','information about apples ?','apple','Apple']:
      reply = ' Apples:- Soil: Well-drained loamy soil with a pH range of 6.0-7.0.\n - Weather: Varies depending on the apple variety, but generally prefers cool to mild temperatures during the growing season. Most varieties require a certain amount of winter chilling hours.\n - Water: Regular watering is essential, especially during dry periods. Provide about 1-2 inches of water per week.\n - Harvesting: Timing depends on the apple variety, but harvest usually takes place in late summer to early fall. Apples are harvested when they have reached maturity, usually indicated by their color and firmness.\n  - Pesticides: Apple orchards require various pesticides to manage pests and diseases. Insecticides like carbaryl or spinosad can be used for pests like codling moths or apple maggots. Fungicides are important for disease control, including products for apple scab or powdery mildew.\n - Fertilizers: Apple trees have specific nutrient requirements, including nitrogen, phosphorus, and potassium. Fertilizers are typically applied in early spring and late fall, with formulations like 10-10-10 or 14-14-14. Foliar fertilization may also be done during the growing season.\n  - Season: Apples are typically grown as a temperate fruit crop, primarily in the hilly regions of India. The sowing of apple trees or their grafting is done during the winter season when the trees are dormant, usually around November to February.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of peanuts','Growing of peanuts ?','information about peanuts ?','peanut','Peanut']:
      reply = ' Peanuts:\n - Soil: Well-drained sandy soil with a pH range of 5.8-6.2.\n - Weather: Requires a warm climate with temperatures between 70-90°F (21-32°C) during the growing season. Frost-free conditions are necessary.\n - Water: Peanuts require consistent moisture, especially during flowering and pod development. Aim for 1-2 inches of water per week.\n - Harvesting: Harvesting occurs when the plants have reached maturity, usually around 120-150 days after planting. Dig up the entire plant and allow the peanuts to dry before shelling.\n - Pesticides: Herbicides like imazethapyr or pendimethalin can be used for weed control in peanut fields. Insecticides may be applied to manage pests such as thrips or spider mites. Fungicides are used for diseases like leaf spot or white mold.\n - Fertilizers: Peanuts require a balanced fertilization approach. Nitrogen is typically the most important nutrient, and phosphorus and potassium are also necessary. Soil testing can help determine the specific nutrient needs for peanuts.\n  - Season: Peanuts are commonly grown as a kharif (monsoon) crop in India. The sowing season for peanuts starts around June and July, coinciding with the monsoon rains.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of grapes','Growing of grapes ?','information about grapes ?','grapes','Grapes']:
      reply = ' Grapes:\n - Soil: Well-drained loamy soil with a pH range of 5.5-7.0.\n - Weather: Thrives in warm to hot temperatures between 60-90°F (15-32°C). Different grape varieties have specific climate requirements.\n - Water: Regular watering is important, especially during fruit development. Aim for 1 inch of water per week.\n - Harvesting: Harvesting time varies depending on the grape variety and intended use (table grapes or wine production). Grapes are typically harvested when they have reached the desired sugar content and flavor. - Pesticides: Herbicides like glyphosate or paraquat are commonly used for weed control in vineyards. Insecticides may be applied for pests such as grape berry moths or leafhoppers. Fungicides are important for diseases like powdery mildew or downy mildew.\n - Fertilizers: Grapevines require balanced fertilization, typically with nitrogen, phosphorus, and potassium. Soil testing and leaf analysis can help determine the specific nutrient requirements. Organic amendments like compost or cover crops can also be beneficial.\n - Season: Grapes are mostly grown as a summer season crop in India. The sowing or planting of grapevines typically takes place during the winter months, from December to February. The actual fruiting and harvesting of grapes occur in the summer months, usually between March and June.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['best pesticides','What are the best pesticides','list of best pesticides','good pesticides','Good pesticides','pesticides','Pesticides']:
      reply = ' As a bot I do not have any personal opinions, but I can provide you with information on commonly used pesticides.It is important to note that the best pesticides can vary depending on several factors, including the specific crop being grown, the pest or disease issues present, and the soil conditions.\n -Integrated Pest Management (IPM): This is not a specific pesticide but rather an approach that combines various pest control methods to minimize the use of chemical pesticides. IPM focuses on using biological, mechanical, and cultural controls alongside targeted pesticide applications when necessary.\n -Neem Oil: A natural pesticide derived from the neem tree, which is effective against a wide range of pests and insects.\n -Pyrethrin: A botanical insecticide derived from chrysanthemum flowers, commonly used against various insects.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['best fertilizers','What are the best fertilizers','list of best fertilizers','good fertilizers','Good fertilizers','fertilizers','Fertilizers']:
      reply = 'As a bot I do not have any personal opinions, but I can provide you with information on commonly used fertilizers.It is important to note that the best fertilizers can vary depending on several factors, including the specific crop being grown, the pest or disease issues present, and the soil conditions.\n Organic Fertilizers: Examples include compost, manure, bone meal, fish emulsion, and seaweed extract. Organic fertilizers release nutrients slowly and improve soil structure and water retention.\n -Synthetic Fertilizers: These are chemical fertilizers with specific nutrient formulations, such as NPK (nitrogen, phosphorus, and potassium). They provide nutrients quickly to plants but may lead to nutrient imbalances if not used correctly.\n -Controlled-Release Fertilizers: These fertilizers provide a slow and steady release of nutrients over an extended period, reducing the risk of over-fertilization and nutrient leaching.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['best pesticides and fertilizers','What are the best pesticides and fertilizers','list of best pesticides and fertilizers','good pesticidesand fertilizers','Good pesticides and fertilizers','pesticides and fertilizers','Pesticides and fertilizers']:
      reply = 'As a bot I do not have any personal opinions, but I can provide you with information on commonly used pesticides and fertilizers. It is important to note that the "best" pesticides and fertilizers can vary depending on several factors, including the specific crop being grown, the pest or disease issues present, and the soil conditions.\n *Pesticides:\n -Integrated Pest Management (IPM): This is not a specific pesticide but rather an approach that combines various pest control methods to minimize the use of chemical pesticides. IPM focuses on using biological, mechanical, and cultural controls alongside targeted pesticide applications when necessary.\n -Neem Oil: A natural pesticide derived from the neem tree, which is effective against a wide range of pests and insects.\n -Pyrethrin: A botanical insecticide derived from chrysanthemum flowers, commonly used against various insects.\n Fertilizers:\n -Organic Fertilizers: Examples include compost, manure, bone meal, fish emulsion, and seaweed extract. Organic fertilizers release nutrients slowly and improve soil structure and water retention.\n -Synthetic Fertilizers: These are chemical fertilizers with specific nutrient formulations, such as NPK (nitrogen, phosphorus, and potassium). They provide nutrients quickly to plants but may lead to nutrient imbalances if not used correctly.\n -Controlled-Release Fertilizers: These fertilizers provide a slow and steady release of nutrients over an extended period, reducing the risk of over-fertilization and nutrient leaching. '
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of cotton','Growing of cotton ?','information about cotton ?','cotton','Cotton']:
      reply = 'Soil: Well-drained sandy loam or clay loam soil with good moisture retention.\n -Weather: Cotton thrives in warm to hot temperatures between 60-95°F (15-35°C). Frost-free conditions are necessary.\n -Water: Cotton is a moderately water-intensive crop. It requires about 1-2 inches of water per week, depending on the growth stage and local climate conditions.\n -Duration of Harvesting: Harvesting of cotton usually occurs from 150-180 days after sowing, depending on the variety and growing conditions. Harvest when the bolls have matured and opened.\n -Pesticides are chemicals used to control pests, such as insects, weeds, and diseases, that can harm cotton plants and reduce yields. Some commonly used pesticides in cotton farming include insecticides, herbicides, and fungicides.\n -Fertilizers are substances applied to the soil or sprayed on plants to provide essential nutrients that may be lacking for healthy cotton growth. The primary nutrients required by cotton plants are nitrogen, phosphorus, and potassium (NPK). Fertilizers can be organic (e.g., manure) or synthetic (e.g., chemical fertilizers).\n -The cotton-growing season varies depending on the region and climate. Cotton is a warm-season crop, and its cultivation typically begins in the spring or early summer, as it requires warm temperatures to germinate and grow'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of sugarcane','Growing of sugarcane ?','information about sugarcane ?','sugarcane','Sugarcane']:
      reply = ' Sugarcane:\n -Soil: Well-drained fertile soil with good organic matter content. Sandy-loam soils are also suitable.\n -Weather: Sugarcane prefers a tropical to subtropical climate with temperatures between 75-95°F (24-35°C). It can tolerate light frost but grows best in frost-free conditions.\n -Water: Sugarcane is a water-intensive crop, requiring about 2-3 inches of water per week, especially during the peak growing season.\n -Duration of Harvesting: Sugarcane is harvested at different times depending on the variety and the intended use (sugar production or as fodder). It can take around 10-18 months to mature for harvest.\n -Insecticides: Sugarcane can be susceptible to various insect pests that can damage the crop. Common insecticides used in sugarcane farming include:Chlorpyrifos,Imidacloprid\n -Fertilizers in Sugarcane Farming:\n -Nitrogen (N): Nitrogen is essential for sugarcane growth and plays a crucial role in promoting vegetative development and sucrose accumulation. Common nitrogen fertilizers used include urea and ammonium sulfate.\n -Season: Sugarcane is a tropical and subtropical crop that prefers warm temperatures. The growing season for sugarcane typically begins in the late spring or early summer and continues through the monsoon season and into the fall months. Sugarcane requires a long growing period, and the harvesting season usually spans several months, starting from late autumn and extending through winter in many regions.\n'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of Chickpeas','Growing of Chickpeas ?','information about Chickpeas ?','chickpeas','Chickpeas']:
      reply = 'Chickpeas (Garbanzo Beans):\n -Soil: Well-drained sandy-loam soil with a pH range of 6.0-8.0.\n -Weather: Chickpeas prefer cool temperatures between 60-75°F (15-24°C) during the growing season.\n -Water: Chickpeas have moderate water requirements. Provide about 1-1.5 inches of water per week, particularly during flowering and pod development stages.\n -Duration of Harvesting: Chickpeas are typically harvested around 90-120 days after planting when the pods have fully developed and the seeds have matured.\n -Pesticides in Chickpea Farming:\n  Pesticides are used in chickpea farming to control various pests and diseases that can affect crop health and yield. Some common pests and diseases that can impact chickpeas include aphids, caterpillars, powdery mildew, Ascochyta blight, and Fusarium wilt. Specific pesticides will vary depending on the region and the predominant pest and disease pressures.\n -Fertilizers in Chickpea Farming:\n  Fertilizers are used to provide essential nutrients to the chickpea plants, ensuring healthy growth and optimal yields. Chickpeas have specific nutrient requirements, including nitrogen, phosphorus, potassium, and micronutrients.\n Growing Season for Chickpeas:\n Chickpeas are cool-season crops and prefer moderate temperatures for optimal growth. '
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of tea','Growing of tea ?','information about tea ?','tea','Tea']:
      reply = 'Tea: -\n -Soil: Well-drained acidic soils with a pH range of 4.5-5.5 are suitable for tea cultivation.\n -Weather: Tea grows best in regions with a subtropical to temperate climate, with temperatures between 55-85°F (13-29°C). It requires a good amount of rainfall.\n -Water: Tea requires consistent moisture, especially during dry periods or during the establishment phase.\n -Duration of Harvesting: The harvesting time for tea leaves varies depending on the tea plants age and the desired tea type. Generally, tea leaves are plucked every 7-10 days during the growing season.\n -Season: Tea is primarily grown in regions with a subtropical to temperate climate. The tea-growing season depends on the specific type of tea and the geographical location. In many tea-producing regions, the growing season typically starts in spring and extends through the summer months. Harvesting of tea leaves may occur multiple times during the growing season, especially for high-quality teas like first flush and second flush.\n -Pesticides in Tea Farming:\n Pesticides are used in tea farming to control pests and diseases that can impact the tea plants and reduce yields. Tea bushes are susceptible to various pests, including mites, caterpillars, and tea leafhoppers, as well as diseases like anthracnose and gray mold.\n -Fertilizers in Tea Farming:\n Fertilizers are used to provide essential nutrients to the tea plants, as tea plantations are often grown in nutrient-depleted soils. The primary nutrients required for tea cultivation are nitrogen (N), phosphorus (P), and potassium (K).'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Requirements of growth of coffee','Growing of coffee ?','information about coffee ?','coffee','Coffee']:
      reply = ' Coffee:\n -Soil: Well-drained sandy-loam or laterite soils with a pH range of 6.0-6.5.\n -Weather: Coffee plants thrive in a tropical climate with temperatures between 60-70°F (15-24°C) and an annual rainfall of 60-100 inches.\n -Water: Coffee requires consistent moisture, particularly during flowering and berry development.\n -Duration of Harvesting: Coffee cherries are harvested when they are ripe, usually taking place over several months, depending on the coffee variety and local climate conditions.Pesticides: Coffee plants are susceptible to pests like coffee berry borer, leaf rust, and mealybugs.\n -Fertilizers: Coffee plants require a balanced fertilizer regimen to promote healthy growth and fruiting.\n -Season: Coffee is usually grown in tropical regions with specific altitude and temperature requirements. The coffee-growing season varies based on the type of coffee and the region. In general, the coffee season starts in late fall or early winter, depending on the location.\n'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['what is drip irrigation','What is drip irrigation','Drip irrigation','drip irrigation']:
      reply = 'Drip Irrigation:\n -Suitable for: Vegetables, fruits, orchards, vineyards, and row crops like tomatoes and cucumbers.\n -Description: Drip irrigation delivers water directly to the plant root zone through a network of tubes, pipes, and emitters. It provides precise water application, reducing water wastage and ensuring efficient water use.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    

    elif message in['What is sprinkler irrigation','what is sprinkler irrigation','sprinkler irrigation','Sprinkler irrigation']:
      reply = 'Sprinkler Irrigation:\n -Suitable for: Most crops, including grains, vegetables, fruits, and pastures.\n -Description: Sprinkler irrigation involves spraying water over the crops like rain. It can be used for overhead watering or through center pivot systems. Sprinklers are adaptable and can be adjusted based on crop and field requirements.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What is flood irrigation','what is flood irrigation','flood irrigation','Flood irrigation']:
      reply = 'Flood Irrigation:\n -Suitable for: Crops like rice and wheat, and flat fields without slope.\n -Description: Flood irrigation involves flooding the fields with water, allowing it to flow over the entire field evenly. It is commonly used in rice paddies and can provide good water coverage for certain crops.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['furrow irrigation','Furrow irrigation','what is furrow irrigation','What is furrow irrigation']:
      reply = 'Furrow Irrigation:\n -Suitable for: Crops with well-defined rows or beds, such as corn, cotton, and soybeans.\n -Description: Furrow irrigation involves creating small channels or furrows along the rows of crops. Water is then directed into these furrows, providing water to the root zone of the plants.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['What is subsurface irrigation','what is subsurface irrigation','subsurface irrigation','Subsurface irrigation']:
      reply = 'Subsurface Irrigation:\n -Suitable for: Crops with shallow root systems, such as strawberries and some vegetables.\n -Description: Subsurface irrigation delivers water below the soil surface directly to the root zone. It reduces evaporation and minimizes water contact with the foliage, preventing diseases.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['pivot irrigation','Pivot irrigation','What is pivot irrigation','what is pivot irrigation ?','what is pivot irrigation']:
      reply = 'Pivot Irrigation:\n -Suitable for: Crops like corn, soybeans, alfalfa, and potatoes.\n -Description: Pivot irrigation uses wheeled systems to rotate around a central point, delivering water through sprinklers or drip lines. It covers a large area efficiently and is commonly used in large-scale farming.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['center pivot irrigation','Center Pivot irrigation','Center pivot irrigation','what is center pivot irrigation?','What is center pivot irrigation?','what is center pivot irrigation']:
      reply = 'Center Pivot Irrigation:\n -Suitable for: Large-scale field crops like grains, alfalfa, and potatoes.\n -Description: Center pivot irrigation involves a rotating arm mounted on wheels, moving in a circular pattern to irrigate crops. It is suitable for flat or gently sloping terrain.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['types of irrigation','Types of irrigation','What are the types of irrigation ?','What are the types of irrigation?','what are the types of irriigation']:
      reply = 'Types of irrigation are:\n 1) Drip irrigation\n 2) Sprinkler irrigation\n 3) Flood irrigation\n 4) Furrow irrigation\n 5) Subsurface irrigation\n 6) Pivot irrigation\n 7) Center Pivot irrigation\n These are the types of irrigation .'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['cycle of growing of a crop','Cycle of agriculture','cycle of agriculture','process of agriculture','Process of agriculture','process of Agriculture']:
      reply = 'Land Preparation:\n -Clear the field of any previous crop residues and weeds.\n -Plow or till the soil to break it up and create a fine seedbed.\n -Level the field to ensure even distribution of water during irrigation.\n\nSeed Selection and Sowing:\n -Choose high-quality, certified wheat seeds suitable for your region and growing conditions.\n -Determine the appropriate time for sowing based on your location and climate. Wheat is usually sown in the fall or winter for winter wheat and in the spring for spring wheat.\n -Plant the seeds at the recommended depth, typically around 1-2 inches, depending on soil moisture and temperature.\n\nFertilization:\n -Conduct a soil test to determine the nutrient requirements of the soil.\nApply appropriate fertilizers based on the soil test results and the specific growth stage of the wheat crop.\n -Common fertilizers for wheat include nitrogen (N), phosphorus (P), and potassium (K).\n\nIrrigation:\n -Provide sufficient water to the wheat crop, especially during critical growth stages like tillering, booting, and heading.\n -The amount and frequency of irrigation will depend on the local climate, soil moisture, and the wheat growth stage.\n\nWeed Control:\n -Monitor the wheat field regularly for weed infestations.\n -Implement weed control measures, such as manual weeding or herbicide application, to minimize weed competition with the wheat plants.\n\nDisease and Pest Management:\n -Monitor the crop for signs of diseases and pests, such as rust, smut, aphids, and Hessian fly.\n -Apply appropriate fungicides or insecticides if necessary to protect the crop from diseases and pests.\n\nGrowth Stage Monitoring:\n -Monitor the wheat plants growth stages to make timely management decisions.\n -Different growth stages include germination, tillering, booting, heading, flowering, and grain development.\n\nHarvesting:\n -Harvest the wheat crop when it reaches maturity and the grain has dried to the desired moisture content.\n -Use a combine harvester or other appropriate machinery to efficiently harvest the wheat.\n\nPost-Harvest Handling:\n -Dry the harvested wheat to reduce its moisture content and prevent spoilage.\n -Store the harvested wheat in suitable storage facilities to protect it from pests and moisture.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Briefly about growth of rice','briefly about growth of rice']:
      reply = 'Land Preparation: Level the field and create a flooded paddy to hold water during cultivation.\n\nSeed Selection and Sowing: Use high-quality rice seeds suitable for your region. Directly sow the seeds in the flooded field or transplant young seedlings.\n\nFertilization: Apply balanced fertilizers, especially nitrogen, phosphorus, and potassium, to promote healthy growth.\n\nIrrigation: Maintain a consistent water level in the paddy field throughout the growth period, especially during the reproductive stages.\n\nWeed Control: Monitor and control weeds, either manually or through herbicide application, to prevent competition with rice plants.\n\nDisease and Pest Management: Regularly scout for diseases and pests like blast, sheath blight, and stem borers, and apply appropriate treatments when necessary.\n\nGrowth Stage Monitoring: Monitor the growth stages, such as vegetative, reproductive, and ripening stages, to manage water and nutrient requirements efficiently.\n\nHarvesting: Harvest the rice crop when the grains have fully matured and the water has drained from the field.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Briefly about growth of corn','briefly about growth of corn']:
      reply = 'Crop: Corn (Maize):\n\n Land Preparation: Plow and cultivate the field to create a suitable seedbed.\n\n Seed Selection and Sowing: Choose high-quality corn seeds and plant them at the appropriate depth, spacing, and planting arrangement.\n\n Fertilization: Apply nitrogen, phosphorus, and potassium fertilizers at different growth stages to support corn nutrient requirements.\n\n Irrigation: Provide sufficient water, especially during critical growth stages like pollination and grain filling.\n\n Weed Control: Manage weeds through manual weeding or herbicide application to prevent competition with corn plants.\n\n Disease and Pest Management: Monitor and control pests and diseases like corn borers, armyworms, and rusts to protect the crop.\n\n Growth Stage Monitoring: Monitor the growth stages, such as germination, vegetative growth, tasseling, and grain development, to make timely management decisions.\n\n Harvesting: Harvest corn when the kernels are mature and dry, typically when the husks have turned brown.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Briefly about growth of cotton','briefly about growth of cotton']:
      reply = 'Crop: Cotton:\n\n Land Preparation: Prepare the field by plowing and tilling to create a suitable seedbed.\n\n Seed Selection and Sowing: Use high-quality cotton seeds and plant them at the recommended spacing.\n\n Fertilization: Apply nitrogen, phosphorus, and potassium fertilizers to promote cotton plant growth and fiber production.\n\n Irrigation: Provide adequate water during critical growth stages, especially flowering and boll development.\n\n Weed Control: Control weeds to prevent competition with cotton plants, using manual or herbicidal methods.\n\n Disease and Pest Management: Monitor and manage pests and diseases like bollworms, aphids, and cotton leaf curl virus.\n\n Growth Stage Monitoring: Monitor the growth stages, such as vegetative growth, flowering, and boll development, to make timely management decisions.\n\n Harvesting: Harvest cotton when the bolls have opened and the cotton fibers are mature.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['types of tractor tools used','What are the types of tractor tools used?','What are the types of tractor tools used','what are the types of tractor tools used','tractor tools','Tractor tools','types of tractor tools','Types of tractor tools']:
      reply = 'types of tractor tools used :\n\n -Tractor tools, also known as tractor implements or attachments, are essential agricultural equipment that can be attached to the back or front of a tractor to perform various tasks. These tools are designed to increase the efficiency and productivity of farming operations. Here are some common types of tractor tools used in agriculture:\n\n -Plow: Used for primary tillage, a plow helps turn and loosen the soil to prepare it for planting.\n\n -Harrow: A harrow is used for secondary tillage to break up clods, level the soil, and incorporate crop residues.\n\n -Cultivator: This tool is used for weed control and soil aeration. It helps remove weeds and break up the topsoil without turning it over.\n\n -Seed Drill: A seed drill is used for precise and uniform seeding of seeds in the soil at the desired depth.\n\n -Planter: Similar to a seed drill, a planter is used to plant seeds in rows with precision and uniformity.\n\n -Sprayer: Tractor-mounted sprayers are used to apply pesticides, herbicides, and fertilizers to crops.\n\n -Fertilizer Spreader: This tool is used to distribute fertilizers evenly across the field.\n\n -Rotary Tiller: A rotary tiller is used for secondary tillage to break up the soil and prepare a seedbed.\n\n -Mower: Tractor-mounted mowers are used for cutting grass, hay, or crops.\n\n -Bale Spear: This attachment is used to lift and transport bales of hay or straw.\n\n -Front-end Loader: A front-end loader is used for loading and moving materials like soil, gravel, and farm inputs.\n\n -Backhoe: A backhoe attachment is used for digging and excavating tasks.\n\n -Post Hole Digger: This tool is used to dig holes for fence posts or other purposes.\n\n -Disc Harrow: A disc harrow is used for seedbed preparation and weed control.\n\n -Ridger: A ridger is used to create ridges or furrows for planting certain crops.\n\n -Rake: Tractor-mounted rakes are used for gathering hay or forage materials.\n\n -Rotary Cutter: Also known as a brush hog or bush hog, a rotary cutter is used for cutting thick vegetation and overgrown areas.\n\n -Subsoiler: A subsoiler is used to break up compacted soil layers beneath the surface.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['how to protect crops','protection of crops','how do we protect crops','How do we protect crops','How to protect crops','protection of crops','How do we protect crops ?','How to protect crops ?','crop protection','Crop protection']:
      reply = 'protection of crops during agriculture:\n\n -Protection of crops during agriculture is essential to ensure optimal growth, minimize losses due to pests and diseases, and achieve a successful harvest. Several practices and methods are employed to protect crops effectively. Here are some common strategies for crop protection:\n\n -Integrated Pest Management (IPM): IPM is a holistic approach to managing pests that involves using multiple techniques to reduce pest populations while minimizing the impact on beneficial organisms and the environment. It includes practices like crop rotation, biological control (using natural enemies of pests), trap crops, and judicious use of pesticides when necessary.\n\n -Crop Rotation: Planting different crops in sequence on the same field helps break pest cycles, improves soil health, and reduces the buildup of pests and diseases.\n\n -Biological Control: Encouraging the presence of natural predators and beneficial insects that feed on pests can help control pest populations naturally.\n\n -Pesticides: When used, pesticides should be applied judiciously and in accordance with recommended guidelines to minimize harm to beneficial organisms and the environment. Integrated pest management emphasizes using pesticides only when necessary and choosing the least toxic options.\n\n -Disease-resistant Varieties: Planting disease-resistant crop varieties can significantly reduce the risk of crop diseases and the need for chemical control.\n\n -Good Agricultural Practices (GAPs): Following recommended agricultural practices, such as proper planting density, appropriate spacing, and timely irrigation, helps promote healthy plant growth and reduces susceptibility to pests and diseases.\n\n -Weed Control: Managing weeds through mechanical methods, mulching, and appropriate herbicides prevents weed competition with crops and conserves soil moisture.\n\n -Physical Barriers: Installing physical barriers like nets, screens, or fences can protect crops from birds, insects, and larger pests.\n\n -Irrigation Management: Proper irrigation practices help prevent overwatering, which can lead to waterlogged soils and increased susceptibility to diseases.\n\n -Monitoring and Early Detection: Regularly inspecting crops for signs of pests, diseases, and nutrient deficiencies allows for early detection and timely intervention.\n\n -Fertility Management: Ensuring proper nutrient balance and fertilization helps maintain plant health and reduces the risk of disease and pest infestations.\n\n -Weather Monitoring: Monitoring weather conditions helps anticipate potential threats, such as heavy rains causing waterlogging or extreme temperatures stressing the plants.\n\n -Post-harvest Protection: Proper storage and handling after harvesting help minimize post-harvest losses due to pests, diseases, and environmental factors.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['livestock management','Livestock management','animal maintainance','How to maintain agricultural animals','Animal maintainance','Animal management','animal management','how to maintain animals','How to maintain animals']:
      reply = 'Livestock care involves providing proper management, nutrition, health, and welfare for animals raised on farms or in agricultural settings. It is essential to ensure the well-being of livestock for their health, productivity, and overall quality of life. Here are some key aspects of livestock care:\n\nHousing and Shelter:\n -Provide clean, well-ventilated, and adequately sized shelters for animals to protect them from adverse weather conditions, extreme temperatures, and predators.\n -Design the housing to promote comfort and minimize stress for the animals.\n\nNutrition:\n -Offer a balanced and appropriate diet for each type of livestock, considering their age, weight, breed, and specific nutritional requirements.\n -Provide access to clean and fresh water at all times.\n -Monitor feed intake and adjust rations as needed to maintain optimal health and growth.\n\nHealth Care:\n -Establish a regular health care program that includes vaccinations, deworming, and preventive measures against common diseases.\n -Conduct routine health checks to identify and address any health issues promptly.\n -Isolate and treat sick animals to prevent the spread of diseases.\n\nSanitation and Hygiene:\n -Maintain clean and sanitary conditions in the livestock area to prevent the buildup of waste and reduce the risk of disease transmission.\n -Regularly clean water troughs, feeding areas, and animal bedding.\n\nHandling and Transportation:\n -Handle livestock gently and calmly to reduce stress and prevent injuries.\n -Ensure proper handling and transportation procedures are followed to maintain the well-being of animals during transportation.\n\nPasture Management (for grazing animals):\n -Provide access to well-managed pastures with suitable forage to support the nutritional needs of grazing animals.\n -Practice rotational grazing to prevent overgrazing and maintain healthy pastureland.\n\nEnvironmental Enrichment:\n -Provide environmental enrichment to prevent boredom and promote natural behaviors in livestock. This can include toys or objects for play, perches for birds, or scratching posts for animals.\n\nRecord Keeping:\n -Maintain accurate records of individual animals, including health and vaccination history, breeding records, and any specific care requirements.\n\nAnimal Behavior:\n -Understand the natural behavior of each species and breed, and accommodate their needs in the farm management practices.\n\nContinual Learning:\n -Stay updated on best practices and advancements in livestock care through attending workshops, training programs, and collaborating with experts in the field.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['pest and disease management','Pest and disease management','control of pest and disease','pest control','Pest control']:
      reply = 'Pest and disease management: Effective pest and disease management is crucial in agriculture to protect crops and ensure optimal yields. Integrated Pest Management (IPM) is a holistic approach that combines various strategies to control pests and diseases while minimizing the impact on the environment. Here are key components of pest and disease management:\n\nPrevention:\n -Use disease-resistant or pest-resistant crop varieties whenever possible.\n -Implement crop rotation to break pest and disease cycles and maintain soil health.\n -Practice good sanitation to remove crop residues and weeds that can harbor pests and diseases.\n\nMonitoring:\n -Regularly monitor crops for signs of pests, diseases, and nutrient deficiencies.\n -Set up traps or use pheromones to monitor and identify pest populations.\n\nCultural Control:\n -Adjust planting dates and spacing to minimize exposure to pests and diseases.\n -Implement proper irrigation and water management to avoid conditions that promote disease development.\n -Provide balanced nutrition to enhance plant health and resistance to pests and diseases.\n\nBiological Control:\n -Introduce natural predators or parasitoids to control pest populations.\n -Use beneficial microorganisms that antagonize or compete with pathogens.\n\nMechanical and Physical Control:\n -Use physical barriers, such as nets or row covers, to protect crops from pests.\n -Handpick and remove pests when feasible.\n -Use traps or barriers to prevent pests from reaching crops.\n\nChemical Control (As a Last Resort):\n -If necessary, use pesticides selectively and in combination with other management strategies.\n -Choose pesticides with lower toxicity to non-target organisms.\n -Apply pesticides at the right time and rate according to label instructions.\n\nResistance Management:\n -Rotate the use of different classes of pesticides to reduce the risk of pest resistance.\n -Use chemical control only when pest populations exceed the economic threshold.\n\nTimely Action:\n -Act quickly when pests or diseases are detected to prevent outbreaks and minimize damage.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['market prices','Market prices','latest market prices','Latest market prices']:
      reply = 'The market prices of vegetables per kg are:\n -Amaranth leaves - 17.00-23.00\n -Amla - 84.00-116.00\n -Ash gourd - 29.00-40.00\n -Baby corn - 66.00-91.00\n - Banana flower - 17.00-23.00\n - Beetroot - 49.00-68.00\n -Capsicum - 48.00-66.00\n - Bitter gourd - 41.00-56.00\n - Bottle gourd - 28.00-38.00\n - Butter beans - 56.00-78.00\n - Broad beans -48.00-66.00\n - Cabbage - 26.00-36.00\n - Carrot - 50.00-69.00\n - Cauliflower - 30.00-41.00\n - Cluster beans - 48.00-66.00\n - Coconut - 41.00-56.00\n - Colacasia leaves - 18.00-25.00\n - Colacasia roots - 31.00-43.00\n - Coriander leaves - 13.00-18.00\n - Corn - 36.00-50.00\n - Cucumber - 34.00-46.00\n - Curry leaves - 30.00-41.00\n - Dill leaves - 18.00-25.00\n - Drumstcks - 60.00-83.00\n - Brinjal - 34.00-46.00\n - Brinjal(Big) - 36.00-50.00\n - Elephant yam - 29.00-40.00\n - Fenugreek leaves - 14.00-20.00\n - Green bean - 82.00-112.00\n - Garlic - 157.00-216.00\n - Ginger - 198.00-272.00\n - Green chilli - 115.00-158.00\n - Green onion - 49.00-68.00\n - Green peas - 98.00-135.00\n - Ivy gourd - 31.00-43.00\n - Lemon - 56.00-78.00\n - Mango - 36.00-50.00\n - Mint leaves - 6.00-8.00\n - Mushroom - 109.00-150.00\n - Mustard leaves - 16.00-21.00\n - Okra (Ladies finger) - 46.00-63.00\n - Onion(Big) - 37.00-51.00\n - Onion(Small) - 64.00-87.00\n - Plantain(raw banana) - 14.00-20.00\n - Potato - 37.00-51.00\n - Pumpkin - 24.00-33.00\n - Radish - 42.00-58.00\n - Ridge gourd - 40.00-54.00\n - Shallot(pearl onion) - 40.00-54.00\n - Snake gourd - 42.00-58.00\n - Sorrel leaves - 13.00-18.00\n - Spinach - 12.00-17.00\n - Sweet potato - 46.00-63.00\n - Tomato - 104.00-144.00\n These are the current vegetables prices.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['']:
      reply = 'Rice is the most exported agricultural product from India.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Which food does India export the most?','mostly exported food?']:
      reply = 'Rice is the most exported agricultural product from India.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    
    elif message in['Which food does India export the most?','mostly exported food?']:
      reply = 'Rice is the most exported agricultural product from India.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response
    else:
      reply='Sorry, I dont understand what you said.Please try anything.'
      response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
      return response




send_message(chat_id, message)

#print(data[-1]['message']['text'])

#print(data[-1]['message']['from']['id'])

#print(data[-1]['message']['from']['first_name'])


update_id = None

def get_updates(url,offset):
 url = url + 'getUpdates?timeout=100'
 if offset:
  url = url+'&offset={}'.format(offset+1)
  result = requests.get(url).json()
  return result
 
 
 while True:
  print("....")
  updates = get_updates(url,offset=update_id)
  print(updates)
  if updates:
   for item in updates:
    update_id = item['update_id']
    try:
     message =item['message']['text'].lower()
     c_id = item['message']['from']['id']
     send_message(url,message,c_id)
    except:
     message = None
