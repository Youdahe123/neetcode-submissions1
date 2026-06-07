class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## a res stack that holds car fleets
        carFleets = []
        # going to loop over both postiion and speed at the same time
        # then do distance/speed = time to see how long it takes if tis larger that the last thing added to the stack we append if not we dont add it
        # we have to also sort in decending arrary 
        fleets = list(zip(position,speed)) ## postion , speed
        fleets.sort(reverse=True)
        for i in fleets:
            time = (target - i[0] ) / i[-1]
            if not carFleets:
                carFleets.append(time)
            
            if time > carFleets[-1]:
                carFleets.append(time)
        
        return len(carFleets)