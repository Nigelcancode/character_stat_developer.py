full_dot = '●'
empty_dot = '○'
def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return('The character name should be a string')

    if not character_name:
        return('The character should have a name')

    if len(character_name) > 10:
        return('The character name is too long')
    
    space = " "
    if space in character_name :
        return('The character name should not contain spaces')

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return('All stats should be integers')

    if strength < 1 or intelligence < 1 or charisma < 1:
        return('All stats should be no less than 1')

    if strength > 4 or intelligence > 4 or charisma > 4:
        return('All stats should be no more than 4')

    sum_of_points = strength + intelligence + charisma 
    
    if sum_of_points != 7:
        return('The character should start with 7 points')


    #these are loops that determine the score of strength
    final_score_strength = ''
    total_full_dots_strength = ''
    total_empty_dots_strength = ''
    no_full_dots_strength = 1

    while no_full_dots_strength <= strength:
            total_full_dots_strength += full_dot
            no_full_dots_strength +=1 

    for two in range(strength, 10):
            total_empty_dots_strength += empty_dot

    total_score_strength = total_full_dots_strength + total_empty_dots_strength

    #these are variables that will calculate the total score for intelligence
    no_full_dots_intel = 1
    total_full_dots_intel = ''
    total_empty_dots_intel = ''

    while no_full_dots_intel <= intelligence :
        total_full_dots_intel += full_dot
        no_full_dots_intel += 1

    for three in range(intelligence, 10):
        total_empty_dots_intel += empty_dot

    total_score_intel = total_full_dots_intel + total_empty_dots_intel

    #these are the variables for calculating the total score for charisma

    total_full_dots_char = ''
    no_full_dots_char = 1

    while no_full_dots_char <= charisma:
        total_full_dots_char += full_dot
        no_full_dots_char += 1
    
    total_empty_dots_char = ''
    for four in range(charisma, 10):
        total_empty_dots_char += empty_dot

    total_score_char = total_full_dots_char + total_empty_dots_char



    return(f'{character_name}\nSTR {total_score_strength}\nINT {total_score_intel}\nCHA {total_score_char}')
