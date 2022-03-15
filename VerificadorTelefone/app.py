import phonenumbers
from phonenumbers import geocoder

phone = input('Digite o numero de telefone a ser verificado. Ex: +551140048922: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))