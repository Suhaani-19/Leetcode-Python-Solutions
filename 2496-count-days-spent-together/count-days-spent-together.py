class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            # Sum days of previous months + current day
            return sum(days_in_months[:month - 1]) + day
        
        alice_arrive = date_to_day(arriveAlice)
        alice_leave = date_to_day(leaveAlice)
        bob_arrive = date_to_day(arriveBob)
        bob_leave = date_to_day(leaveBob)
        
        # Find the overlap interval
        overlap_start = max(alice_arrive, bob_arrive)
        overlap_end = min(alice_leave, bob_leave)
        
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        return 0