from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        parsed_events = []
        
        for e in events:
            event_type = e[0]
            ts = int(e[1])
            data = e[2]
            
            priority = 0 if event_type == "OFFLINE" else 1
            
            parsed_events.append((ts, priority, event_type, data))
        
        parsed_events.sort(key=lambda x: (x[0], x[1]))
        
        mentions = [0] * numberOfUsers
        online_time = [0] * numberOfUsers
        
        for ts, _, event_type, data in parsed_events:
            if event_type == "OFFLINE":
                user_id = int(data)
                online_time[user_id] = ts + 60
            
            else:
                mention_str = data
                
                if mention_str == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                        
                elif mention_str == "HERE":
                    for i in range(numberOfUsers):
                        if online_time[i] <= ts:
                            mentions[i] += 1
                            
                else:
                    ids_tokens = mention_str.split()
                    for token in ids_tokens:
                        uid = int(token[2:])
                        mentions[uid] += 1
                        
        return mentions

