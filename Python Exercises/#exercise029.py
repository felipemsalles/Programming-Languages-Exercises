# exercise029

speed = float(input('Enter the speed of the car: '))
traffic_ticket = 7 * (speed - 80)
if speed > 80.00:
    print(f'You were fined because of your overspeed: ${traffic_ticket:.2f}')
else:
    print('Keep respecting our traffic laws, you are saving lives!')