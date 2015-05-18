def evolve(egg):
    if egg.next_identity != '' and egg.next_identity != 'kanto':
        egg.identity = egg.next_identity
        egg.next_identity = ''
        egg.steps_needed += 2000
        egg.save()
            
def message(egg):
    message = ""
    if egg.identity == 'egg':
        message += "You don't know how you came upon your egg but you love your egg already. "
        if egg.new_steps > 0:
            message += "Your egg wiggles gently in your hands. "
        if egg.steps_received/float(egg.steps_needed) > .8:
            message += "You notice your egg is warm. "
    else:
        message = "Your " + egg.identity + " looks at your expectantly."

    return message
