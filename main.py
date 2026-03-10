from pyscript import display, document

def intrams_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value

    if registration != 'registered':
        display('Not eligible: student is not registered for Intrams. Ask your PE teacher regarding the online registration.', target='output')

    elif clearance != 'cleared':
        display('Not eligible: medical clearance required. Go to the clinic and secure your clearance.', target='output')

    elif section == 'emerald':
        display('Congratulations! You are part of the Blue Bears!', target='output')
        document.getElementById("image").innerHTML = '<img src="blue bears.jpg" width="200">'

    elif section == 'ruby':
        display('Congratulations! You are part of the Red Bulldogs!', target='output')
        document.getElementById("image").innerHTML = '<img src="red bulldogs.jpg" width="200">'

    elif section == 'sapphire':
        display('Congratulations! You are part of the Green Hornets!', target='output')
        document.getElementById("image").innerHTML = '<img src="green hornets.jpg" width="200">'

    else:
        display('Congratulations! You are part of the Yellow Tigers!', target='output')
        document.getElementById("image").innerHTML = '<img src="yellow tigers.jpg" width="200">'