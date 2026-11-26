class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position,speed),key=lambda car: car[0])
        st = []
        for i in range(len(pos_speed)-1,-1,-1):
            time_taken = (target - pos_speed[i][0]) / pos_speed[i][1]
            if len(st) == 0:
                st.append(time_taken)
            else:
                if st[-1] < time_taken:
                    st.append(time_taken)

        return len(st)
            
