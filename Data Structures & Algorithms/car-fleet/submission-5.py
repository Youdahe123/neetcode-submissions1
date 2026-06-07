class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack to hold the time of each fleet that reaches the target
        carFleets = []

        # zip position and speed together so they stay paired when sorting
        fleets = list(zip(position, speed))

        # sort by position descending — process closest car to target first
        # because a car can only be blocked by a car ahead of it
        fleets.sort(reverse=True)

        for i in fleets:
            # time = how long this car takes to reach the target
            # distance remaining = target - position, divide by speed
            time = (target - i[0]) / i[1]

            # if stack is empty, this is the first fleet, always append
            if not carFleets:
                carFleets.append(time)

            # if this car takes LONGER than the fleet ahead, it can never catch up
            # so it forms its own new fleet
            if time > carFleets[-1]:
                carFleets.append(time)

        # each time in the stack represents one fleet
        return len(carFleets)