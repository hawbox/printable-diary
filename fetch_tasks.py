#!/usr/bin/python
import trello
import trellokeys as keys
import ipdb
import os

def auth():
    client = trello.TrelloClient(keys.api_key,token=keys.oauth_token)

    #get all the boards
    boards = client.list_boards()
    #only want the tasks board
    board = filter(lambda x: x.name == 'tasks', boards)[0]
    return board

#fetch all cards in a list
def get_tasks(board,name):
    ret = []
    todo = filter(lambda x: x.name == name, board.all_lists())[0]
    cards = todo.list_cards()

    """
    print("%Matt's Diary")
    print("%")
    print("%")
    print("")
    """
    print('# Todo list')
    for card in cards:
        print( '* ' + card.name )
        ret.append(card.name)
        #ipdb.set_trace()

    return ret

if __name__ == '__main__':
    board = auth()
    get_tasks(board,'Doing')