import BoyClass
import json

def create_team():
    Boy = BoyClass.Boy()

    team_data_text = '\
        {\
            "Tiffany" : {"StartState":"LEFT_RUN", "x":100, "y":100},\
            "Yuna"    : {"StartState":"RIGHT_RUN", "x":200, "y":200},\
            "Sunny"   : {"StartState":"LEFT_STAND", "x":300, "y":300},\
            "Yuri"    : {"StartState":"RIGHT_STAND", "x":400, "y":400},\
            "Jessica" : {"StartState":"LEFT_RUN", "x":500, "y":500}\
        }\
    '

    player_state_table = {
        "LEFT_RUN" : Boy.LEFT_RUN,
        "RIGHT_RUN" : Boy.RIGHT_RUN,
        "LEFT_STAND" : Boy.LEFT_STAND,
        "RIGHT_STAND" : Boy.RIGHT_STAND
    }

    #team_data = json.loads(team_data_text)

    team_data_file = open('team_data.txt','r')
    team_data = json.load(team_data_file)
    team_data_file.close()

    team = []
    for name in team_data:
        player = BoyClass.Boy()
        player.name = name
        player.x = team_data[name]['x']
        player.y = team_data[name]['y']
        player.state = player_state_table[team_data[name]['StartState']]
        team.append(player)

    return team
