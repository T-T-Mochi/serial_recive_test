#coding utf-8
import serial
import re
import csv
import sys

def main():
    file_name = "hoge.csv"
    serial_name = "serial_name"
    serial_bigen =
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        with serial.Serial(serial_name,serial_bigen) as ser:

            while True:
                c = ser.readline()
                d = re.findall(r"[0-9]+", str(c))
                writer.writerow([index,d[0]])
                print(d[0])

            ser.close()

if __name__=="__main__":
    main()
    print("exit")
    sys.exit()
