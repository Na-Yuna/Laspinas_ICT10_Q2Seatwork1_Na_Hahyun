from pyscript import document

def candidate_checker(e):
    club_members = ["haruhi fujioka", "tamaki suoh", "hikaru hitachiin", "kaoru hitachiin", "mitsukuni haninozuka", "takashi morinozuka", "kyoya ootori"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = str(f_name).lower() + ' ' + str(l_name).lower()
    
    member_checker = candidate in club_members
    messages = (f'Sorry {candidate}, your name is not on the list.', 
                f'Congratulations {candidate}, you are a member of the Ouran High School Host Club!')

    document.getElementById('result').innerHTML = messages[member_checker]

