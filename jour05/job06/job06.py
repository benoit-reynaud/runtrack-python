def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40 and note % 5 >= 2.5:
            note_arrondie = round(note/5)*5
            notes_arrondies.append(note_arrondie)
        else:
            notes_arrondies.append(note)
    return notes_arrondies

notes = [67, 82, 45, 38, 93, 57, 41]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)