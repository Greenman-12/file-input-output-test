
seasons_dict = {}
show_list = []
file = input()

with open(file, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    for i in range(0,len(lines),2):
        season = int(lines[i])
        shows = lines[i + 1]
        
        if season in seasons_dict:
            seasons_dict[season].append(shows)
        else:
            seasons_dict[season] = [shows]
        if shows not in show_list:
            show_list.append(shows)

        
            
            
show_by_season = sorted(seasons_dict)
sorted_show_list = sorted(show_list)

with open('output_keys.txt', 'w')as output1:
    for season in show_by_season:
        shows = ';'.join(seasons_dict[season])
        output1.write(f'{season}: {shows}\n')

with open('output_titles.txt', 'w') as output2:
    for show in sorted_show_list:
        output2.write(f'{show}\n')