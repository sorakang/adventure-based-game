print('You are standing on a cliff that peers over the stormy ocean waves.')
print('Your hands, red and blistering from the cold, tightly hold the metal fence barrier around the cliff edge.')
print('You have lost the will to live.')
print('What is your name?')

name = input(' >')

if len(name) == 0:
    print('That\'s fine too, some people don\'t have names.')
    print('But this is an exercise in futility, so you will be named Quinn.')
    name = 'Quinn'

print('What exactly is the will to live?')
print('Are people born with the will to live from the day they are born, a fierce need instilled by our ancestors to continue humanity?')
print('Is it something that builds within the span of your life, each moment adding tiny ticks on a counter that determines your existence?')
print(f'You are {name}, but you are human.')
print('You crawl between the gap of the metal bars and face the seemingly unending ocean without any barriers.')
print('Your hands hold onto the metal bars behind you.')
print('You are free to say anything you\'d like, but they will likely fall to deaf ears.')

speech = input(' >')

if len(speech) == 0:
    print('I\'m glad you already understand.')
    print('There is nothing needed to be said.')

elif name.lower() in speech.lower() :
    print('But what use is it calling your own name?')
    print(f'{name}, that\'s you.')
    
else:
    print('Your words make no difference.')

print('Your cheeks tingle under the icy breeze and when you close your eyes you can hear the crashing waves below you almost amplify.')
print('It\'s a cold and empty morning.')
