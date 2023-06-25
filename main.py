# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import speed4
    a=['以太网']
    while 1:
        print(speed4.get_net_io(a[0], Step_Time=1.0)[0][5:])
        print(speed4.get_net_io(a[0],Step_Time=1.0)[1][5:])

