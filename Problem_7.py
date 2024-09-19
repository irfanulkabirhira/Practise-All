def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        l = int(data[index])
        n = int(data[index+1])
        m = int(data[index+2])
        index += 3
        
        a = list(map(int, data[index:index+l]))
        index += l
        
        matrix = []
        position_map = {}
        
        # Reading matrix and building the position map
        for i in range(n):
            row = list(map(int, data[index:index+m]))
            matrix.append(row)
            for j in range(m):
                value = row[j]
                if value not in position_map:
                    position_map[value] = []
                position_map[value].append((i, j))
            index += m
        
        # Starting game simulation
        r_min, c_min = 0, 0
        player_turn = 0  # 0 for Tsovak, 1 for Narek
        winner = "T"  # Assume Tsovak wins unless proven otherwise
        
        for num in a:
            found = False
            if num in position_map:
                for (i, j) in position_map[num]:
                    if i >= r_min and j >= c_min:
                        r_min = i + 1
                        c_min = j + 1
                        found = True
                        break
                if found:
                    continue
            
            # If no valid cell was found
            if player_turn == 0:
                winner = "N"
            else:
                winner = "T"
            break
            
            # Switch turn
            player_turn = 1 - player_turn
        
        results.append(winner)
    
    # Output all results
    sys.stdout.write("\n".join(results) + "\n")

