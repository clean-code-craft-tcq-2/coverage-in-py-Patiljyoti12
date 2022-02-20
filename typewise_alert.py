#Infer breach
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

#Temperature breach
def classify_temperature_breach(value,coolingType):
    lowerLimit=0
    coolingType_dict={"PASSIVE":35,"HI_ACTIVE":45,"MED_ACTIVE":40}    #Cooling Type classification
    for type in coolingType_dict.keys():
        if type==coolingType:
            upperLimit=coolingType_dict[type]
    breachType=infer_breach(value,lowerLimit,upperLimit)
    return breachType
    

def check_and_alert(alertTarget,value,coolingType):
  breachType=classify_temperature_breach(value,coolingType)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)

#Send to Controller
def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')

#email notification based on breach type
def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
