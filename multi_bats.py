import sys
import subprocess
import json

class BAT(): 
    def __init__ (self):

        self.charge = 0.0
        self.capacity = {}
        self.status = subprocess.getoutput ("dir /sys/class/power_supply")
        self.status = self.status.split()[1:]
        try:
            f = open("bats.json",)
            self.json = json.load(f)
        except FileNotFoundError:
            self.json = False
            print("No such file or directory: " + "bats.json")

        #read json to object
        for i in self.status:
            if not int((subprocess.getoutput ("cat /sys/class/power_supply/" + i + "/energy_now"))) == 0:
                self.capacity[i] = (subprocess.getoutput ("cat /sys/class/power_supply/" + i + "/energy_full"))
            else:
                # if reference json for that BAT's capcity is present -> use it
                if i in self.json:
                    self.capacity[i] = self.json[i]

            #update values 
            with open("bats.json", "w") as f:
                    json.dump(self.capacity, f)



                

            

    def battery (self):
        print("batteries: ", self.status)
        print("capacity: ", self.capacity)

    def percentage (self):
        self.total = 0
        for i in self.capacity:
            self.total += int(self.capacity[i])
            self.charge += int(subprocess.getoutput ("cat /sys/class/power_supply/"+ i + "/energy_now"))
        print ("{:4.2f}".format(100 * (self.charge / self.total)))


def main(sys):
    a = BAT()

    if sys.argv[1] == "info":
        a.battery()

    elif sys.argv[1] == 'percent':
        a.percentage()

if __name__ == "__main__":
    main(sys)
