def evolve(egg):
    if egg.next_identity != '' and egg.next_identity != 'kanto':
        egg.identity = egg.next_identity
        egg.next_identity = ''
        egg.steps_needed += 2000
        egg.save()
            
