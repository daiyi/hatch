def evolve(egg):
    if egg.next_identity != '' and egg.next_identity != 'kanto':
        egg.identity = egg.next_identity
        egg.next_identity = ''
        egg.steps_needed += 2000
        egg.save()

def message(egg, user):

    if user == egg.incubator.owner.username:
        egg.pronoun = 'you'
        egg.possessive = 'your'
    else:
        egg.pronoun = egg.incubator.owner.username
        egg.possessive = egg.pronoun + "'s"

    if egg.identity == 'egg':
        if egg.pronoun == 'you':
            egg.subtitle = 'love your egg. sing to your egg. walk your egg.'
            egg.message = "You don't know how you came upon your egg, but you love your egg already. "
            if egg.new_steps > 0:
                egg.message += "Your egg wiggles gently in your hands. "
            if egg.steps_received/float(egg.steps_needed) > .8:
                egg.message += "You notice your egg is warm. "
        else:
            egg.message = "The egg seems pleased."
    else:
        egg.message = egg.possessive + " " + egg.identity + " looks at you expectantly."

    return egg
