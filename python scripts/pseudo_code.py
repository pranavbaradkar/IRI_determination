#get the vertical acceleration data 
acceleration [. . . . . . . . ]
# pass acceleration data to low pass filter
time[. . . . . . . . . . . . ]

#code to find speed at each point
initial_speed = current_speed
delta_t = t_current  - t_prev
curr_acc = acc[i]
current_speed = initial_speed + (curr_acc) * delta_t 

#code to find dispacement 

initial_dis = current_disp 
delta_t = t_current  - t_prev
curr_speed = ("call above algorithm")
current_disp = initial_dis + (initial_speed + current_speed)/2 * delta_t ; 

#code to find horizontal displacement

#use the above same code and find horizontal displacement 
#pass both the displacement data through low pass filter 
#map horizontal and vertical displacement to give road profile


