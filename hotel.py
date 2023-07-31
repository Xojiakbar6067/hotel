clients={}
free_rooms=[i for i in range(1,21)]
busy_room=[]

def add(name, room):

    if room in free_rooms:
        clients[name]=room
        free_rooms.remove(room)
        busy_room.append(room)
        print(f'клиент {name} добавлен в комнату {room}')
    else:
        print(f'комната под номером {room} нету в нашем отеле')
def delete(name_del):

    if name_del in clients.keys():
        print(f'клиент {name_del} удален из комнаты {clients[name_del]}')
        free_rooms.append(clients[name_del])
        busy_room.remove(clients[name_del])
        clients.pop(name_del)

    else:
        print(f'клиента под именем {name_del} нету у нас')
def show(show):


    if show==1:
        k=0
        for i,j in clients.items():
            k+=1
            print(f'{k}-{i} в {j}ом комнате ')
    elif show==2:
        for i in free_rooms:
            print(f'{i}-комната свободен')
    elif show==3:
        for i in busy_room:
            print(f'{i}-комната уже занято')
    else:
        print('выбрано не правилний команда')
while True:
    print('--------------------------','\n''1-добавит клиента','\n''2-удалит клиента','\n''3-покозат списки')
    operator=int(input('что хотите делат? '))
    if operator==1:
        add(name=input('имя клиента: ').title(),room=int(input('номер комнати: ')))
    elif operator==2:
        delete(name_del=input('имя клиента: ').title())
    elif operator==3:
        print('***********************','\n''1-покозат список клиентов', '\n''2-покозат свободные комнаты', '\n''3-покозат занятые комнаты')
        show(show=int(input('что показыват? ')))
    else:
        print('выбрано не правилний команда')