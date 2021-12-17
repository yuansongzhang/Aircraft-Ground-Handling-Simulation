# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Aircraft import Aircraft
from Algorithm import Algorithm
from vehicle import Vehicle1

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('hi')
    
def main():
    aircraft = Aircraft()
    vehicle = Vehicle1()
    algorithm = Algorithm()
    Object = [aircraft,vehicle,algorithm]
    triggeringTimestamp = 100
    
    for obj in Object:
        if obj.event.triggeringTimestamp < triggeringTimestamp:
            triggeringTimestamp = obj.event.triggeringTimestamp
            event = obj.event
            
        event.update()
        event.execute()
    
    
    

