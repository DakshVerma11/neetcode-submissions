class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        veh = [0] * 1001 

        for num_passengers, start, end in trips:
            veh[start] += num_passengers  
            veh[end] -= num_passengers   
        current_load = 0
        for passengers_change in veh:
            current_load += passengers_change
            if current_load > capacity:
                return False
                
        return True
